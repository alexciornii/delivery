import os
import shutil

import requests
from apps.market.models import Category, SubCategory, Product
from bs4 import BeautifulSoup
from django.core.files import File
from django.core.management.base import BaseCommand
from prj.settings import BASE_DIR

STOP_WORDS = ['ООО', 'ТОВ', 'ТД', 'ЧП', 'ТМ', 'Украин']
tmp_file_path = '%s/tmp.png' % BASE_DIR


def get_products(category, subcategory, url):
    print(f'Downloading from {url}')
    result = requests.get(url, verify=False)
    soup = BeautifulSoup(result.text, 'html.parser')
    for item in soup.findAll('div', {'class': 'company_pic'}):
        img = item.find('img')
        in_stop = False
        for w in STOP_WORDS:
            if img.get('title').find(w) > -1:
                in_stop = True
        if img.get('src').find('no_image') > -1:
            in_stop = True

        if not in_stop:
            print(img.get('title'))
            pr = Product()
            pr.category = category
            pr.name = img.get('title')
            pr.subcategory = subcategory
            img_url = 'https://gastronoma.net/%s' % img.get('src')
            img_response = requests.get(img_url, stream=True, verify=False)
            with open(tmp_file_path, 'wb') as out_file:
                shutil.copyfileobj(img_response.raw, out_file)
            with open(tmp_file_path, 'rb') as img_file:
                print(img_file)
                pr.image.save('product.png', File(img_file), save=True)
            pr.save()


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Clearing DB')
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
        Product.objects.all().delete()
        try:
            shutil.rmtree('%s/media/category' % BASE_DIR)
            shutil.rmtree('%s/media/subcategory' % BASE_DIR)
        except:
            pass

        url = 'https://gastronoma.net'
        print('Start importing from %s' % url)
        result = requests.get(url, verify=False)
        soup = BeautifulSoup(result.text, 'html.parser')

        content = soup.find('div', {'class': 'body_20'})
        for img in content.findAll('img'):
            c = Category()
            c.name = img.get('alt')
            img_url = 'https://gastronoma.net/%s' % img.get('src')
            img_response = requests.get(img_url, stream=True, verify=False)
            with open(tmp_file_path, 'wb') as out_file:
                shutil.copyfileobj(img_response.raw, out_file)
            with open(tmp_file_path, 'rb') as img_file:
                print(img_file)
                c.image.save('cat.png', File(img_file), save=True)

            print('Saving %s ...' % c.name)

            for subcat in img.find_parent('tr').find('div').findAll('a'):
                sc = SubCategory()
                sc.name = subcat.text
                sc.category = c

                sc.save()
                get_products(c, sc, subcat.get('href'))
            c.save()
        os.remove(tmp_file_path)

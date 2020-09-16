from django.urls import path
from django.urls import include
from apps.market.views.auth import AuthView
from apps.market.views.auth import hello
from apps.market.views.product import ProductListView


urlpatterns = [
    path('userLogin', AuthView.as_view()),
    path('hello', hello),
    path('product_list', ProductListView.as_view())
]

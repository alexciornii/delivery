import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-car',
  templateUrl: './car.component.html',
  styleUrls: ['./car.component.css']
})
export class CarComponent implements OnInit {

  model:string;
  speed:number;
  name:string;
  colors:Colors;
  options:string[];
  isEdit:boolean = false;

  constructor() { }

  ngOnInit(): void {
    this.name = 'Audi';
    this.speed = 235;
    this.model = 'RS6';
    this.colors = {
      car: 'White',
      salon: 'Black',
      wheels: 'Silver'
    };
    this.options = ['ABS', 'Autopilot', 'Autoparking'];
  }

  carSelect(carName): void {
    if (carName == 'bmw') {
      this.bmwSelect();
    } else if (carName == 'audi') {
      this.audiSelect();
    } else if (carName == 'mercedes') {
      this.mercedesSelect();
    }
    
  }

  bmwSelect(): void {
    this.name = 'BMW';
    this.speed = 280;
    this.model = 'M5';
    this.colors = {
      car: 'Blue',
      salon: 'White',
      wheels: 'Silver'
    };
    this.options = ['ABS', 'Autopilot', 'Autoparking'];
  }

  audiSelect() {
    this.name = 'Audi';
    this.speed = 360;
    this.model = 'RS6';
    this.colors = {
      car: 'Black',
      salon: 'White',
      wheels: 'Silver'
    };
    this.options = ['ABS', 'Autopilot', 'Autoparking'];
  }

  mercedesSelect() {
    this.name = 'Mercedes';
    this.speed = 200;
    this.model = 'C180';
    this.colors = {
      car: 'Silver',
      salon: 'Black',
      wheels: 'Silver'
    };
    this.options = ['ABS', 'Autopilot', 'Autoparking']; 
  }

  addOpt(option) {
    this.options.unshift(option);
    return false;
  }

  deleteOption(option) {
    for(let i = 0; i < this.options.length; i++) {
      if (this.options[i] == option) {
        this.options.splice(i, 1);
        break;
      }
    }
  }

  showEdit() {
    this.isEdit = !this.isEdit;
  }
}

interface Colors {
  car:string,
  salon:string,
  wheels:string
}

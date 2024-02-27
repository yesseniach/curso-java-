import { Component } from '@angular/core';
import { Manufacturer } from './models/manufacturer.models';
import { Product } from './models/product.models';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [DatePipe],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Hola mundo';

  nombres: string[] = ['noemi', 'aitor', 'judith']

  //nombre variable: TipoDato[] = valor
  manufacturers: Manufacturer[] = [];

  products: Product[] = [
    {
      id: 1,
      title: 'producto 1',
      available: false,
      price: 49.99,
      publishDate: new Date(2015,3,15), 
      manufacturer: {
        id: 1,
        name: 'Ford',
        startYear: 1960
      }
    },
    {
      id: 2,
      title: 'producto 2',
      available: true,
      price: 39.99,
      publishDate: new Date(), // fecha actual
      manufacturer: {
        id: 1,
        name: 'Toyota',
        startYear: 1960
      }
    },
  ];
 }

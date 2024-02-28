import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Product } from '../models/product.models';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [HttpClientModule, RouterLink],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css'
})
export class ProductListComponent implements OnInit{

  products: Product[] = []; //rellenar este array con productos del backend

  constructor(private http: HttpClient) {}

  ngOnInit(): void { //este método se ejecuta automaticamente cuando entras en la pantalla
   
    //traer los productos del backend: crea y ejecuta una petición HTTPbcontra un controlador Backend
    let backend = 'https://fakestoreapi.com/products';
    this.http.get<Product[]>(backend).subscribe(products => this.products = products);

  }

}


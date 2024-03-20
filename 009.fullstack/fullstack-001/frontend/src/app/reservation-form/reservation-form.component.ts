import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { Book } from '../model/book.model';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-reservation-form',
  standalone: true,
  imports: [HttpClientModule, ReactiveFormsModule,],
  templateUrl: './reservation-form.component.html',
  styleUrl: './reservation-form.component.css'
})
export class ReservationFormComponent implements OnInit {
  
  book: Book | undefined;
  
  reservationForm = new FormGroup({
    startDate: new FormControl(new Date()),
    finishDate: new FormControl(new Date())
  });

  bookPrice = 0; // precio del libro por dia
  shipPrice = 0; // precio  envío
  extraPrice = 0; // precio extra por servicios extra
  totalPrice = 0; // suma de los anteriores

  constructor(
    private httpClient: HttpClient,
    private activatedRoute: ActivatedRoute
  ) {}


  ngOnInit(): void {
    this.activatedRoute.params.subscribe(params => {

      const id = params['id'];
      if(!id){
        return;// si no hay id entonces no llamamos al backend
      }

      //traer el book
      this.httpClient.get<Book>('http://localhost:8080/books/' + id)
      .subscribe(book => this.book = book);

    });
  }

  calculatePrice () {

    this.bookPrice = 10;
    this.shipPrice = 4.99;
    this.extraPrice = 5;
    this.totalPrice = 20;
  }
}

import { Component, OnInit } from '@angular/core';
import { Book } from '../model/book.model';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { RouterLink } from '@angular/router';
import { NgbAlertModule } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-book-list',
  standalone: true,
  imports: [HttpClientModule, RouterLink, NgbAlertModule],
  templateUrl: './book-list.component.html',
  styleUrl: './book-list.component.css'
})
export class BookListComponent implements OnInit{
[x: string]: any;

  books: Book[] = [];
  showDeleteBookMessage: boolean = false

  constructor(private httpClient: HttpClient) {}

  ngOnInit(): void {
    this.loadBooks();
  }
  delete(book: Book) {
    const url = 'http://localhost:8080/books/' + book.id;
    this.httpClient.delete(url).subscribe(response => {
      this.loadBooks();
      this.showDeleteBookMessage = true;
    }); // recarga los libros despues de borrar
  }
  hideDeleteBookMessage(){
    this.showDeleteBookMessage= false;
  }

  private loadBooks() {
    const url = 'http://localhost:8080/books';
    this.httpClient.get<Book[]>(url).subscribe(books => this.books = books);
  }
}
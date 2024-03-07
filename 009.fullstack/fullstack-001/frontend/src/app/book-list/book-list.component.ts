import { Component, OnInit } from '@angular/core';
import { Book } from '../model/book.model';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-book-list',
  standalone: true,
  imports: [HttpClientModule],
  templateUrl: './book-list.component.html',
  styleUrl: './book-list.component.css'
})
export class BookListComponent implements OnInit{

   books: Book[] = [];

   constructor(private httpClient: HttpClient) {}
   
  ngOnInit(): void {
    
    const url = 'http://localhost:8080/books'
    this.httpClient.get<Book[]>(url).subscribe(books => this.books = books);
  }
}

import { Component, OnInit } from '@angular/core';
import { Author } from '../model/author.model';
import { Book } from '../model/book.model';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-author-detail',
  standalone: true,
  imports: [RouterLink, HttpClientModule, DatePipe],
  templateUrl: './author-detail.component.html',
  styleUrl: './author-detail.component.css'
})
export class AuthorDetailComponent implements OnInit{
  
  author: Author | undefined;
  books: Book[] = [];

  constructor(
    private httpClient: HttpClient,
    private activatedRoute: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.activatedRoute.params.subscribe(params => {

      const id = params['id'];
      if(!id) return;

      //traer el author
      this.httpClient.get<Author>('http://localhost:8080/authors/' + id)
      .subscribe(author => this.author = author);

      //traer los libros del author
      this.httpClient.get<Book[]>('http://localhost:8080/books/filter-by-author/' + id)
      .subscribe(books => this.books = books);

    });
  }

}

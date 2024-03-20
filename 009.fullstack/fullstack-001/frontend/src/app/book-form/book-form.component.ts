import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { Book } from '../model/book.model';
import { ActivatedRoute, Router } from '@angular/router';
import { Author } from '../model/author.model';
import { Editorial } from '../model/editorial.model';

@Component({
  selector: 'app-book-form',
  standalone: true,
  imports: [ReactiveFormsModule, HttpClientModule],
  templateUrl: './book-form.component.html',
  styleUrl: './book-form.component.css'
})
export class BookFormComponent implements OnInit {

/*
  bookForm = this.fb.group({
    id: [0],
    isbn: [''],
    price: [0.0],
    author: this.fb.group({
      id: [0],
      fullName: [''],
      country: [''],
      active: [false]
    })
  });
*/
bookForm = new FormGroup({
  id: new FormControl<number>(0),
  title: new FormControl<string>(''),
  isbn: new FormControl<string>(''),
  price: new FormControl<number>(0.0),
  published: new FormControl<boolean>(false),
  releaseDate: new FormControl<Date>(new Date()),
  author: new FormControl(),
  editorial: new FormControl()
});

  isUpdate: boolean = false; // por defecto estamos en CREAR no en ACTUALIZAR
  authors: Author[] = []; // array de autores para asociar un autor al libro
  editorials: Editorial[] = [];

  constructor(
      private fb: FormBuilder,
      private httpClient: HttpClient,
      private router: Router,
      private activatedRoute: ActivatedRoute) {
    }

    ngOnInit(): void {
      //cargar autores de backend para el selector de autores en el formulario
      this.httpClient.get<Author[]>('http://localhost:8080/authors')
        .subscribe(authors => this.authors = authors);

      this.httpClient.get<Editorial[]>('http://localhost:8080/editorials')
        .subscribe(editorials => this.editorials = editorials); 

      this.activatedRoute.params.subscribe(params => {
        const id = params['id'];
        if(!id) return;

        this.httpClient.get<Book>('http://localhost:8080/books/' + id).subscribe(bookFromBackend => {
          // cargar el libro obtenido en el formulario bookForm
          this.bookForm.reset({
            id: bookFromBackend.id,
            title: bookFromBackend.title,
            isbn: bookFromBackend.isbn,
            price: bookFromBackend.price,
            published: bookFromBackend.published,
            releaseDate:bookFromBackend.releaseDate,
            author: bookFromBackend.author,
            editorial: bookFromBackend.editorial
          });

          // marcar boolean true isUpdate
          this.isUpdate = true;

        });
      });
    }

    save () {
      const book: Book = this.bookForm.value as Book;
      console.log(book);

      if (this.isUpdate) {
        const url = 'http://localhost:8080/books/' + book.id;
        this.httpClient.put<Book>(url, book).subscribe(bookFromBackend => {
          this.router.navigate(['/books', bookFromBackend.id, 'detail']);
        });

      } else {
        const url = 'http://localhost:8080/books';
        this.httpClient.post<Book>(url, book).subscribe(bookFromBackend => {
          this.router.navigate(['/books', bookFromBackend.id, 'detail']);
        });
      }
    }

    /*
    Función para los selectores del formulario.
    Permite recargar un objeto en un selector
    */
    compareObjects(o1: any, o2: any): boolean {
      //console.log("comparando Objetos", o1, o2);

      if(o1 && o2) {
        return o1.id === o2.id;
      }

      return o1 === o2;
    }

}











/* save() {
      
      //Opción 1: Extraer los valores del formulario manualmente uno por uno
      const book: Book = {
        id: this.bookForm.get('id')?.value ?? 0,
        isbn: this.bookForm.get('isbn')?.value ?? '',
        price: this.bookForm.get('price')?.value ?? 0.0
      }
      console.log(book);
      
      //Opción 2: Equivalente a lo anterioi pero en una sola linea de codigo
      const book2: Book = this.bookForm.value as Book;
      //console.log(book2);

      const url = 'http://localhost:8080/books';

      //Opción1
      this.httpClient.post<Book>(url, book).subscribe(bookFromBackend => {
        console.log(bookFromBackend);
        //navegar hacia el detail o el listado
        //this.router.navigate(['/books']);
        //Navegar hacia detail
        this.router.navigate(['/books', bookFromBackend.id, 'detail']);
      },error => {
        console.log(error);
        window.alert("Datos incorrectos");
      });

      //Opción 2: para resolver el tachado(deprecated)
      this.httpClient.post<Book>(url, book).subscribe({
        next: (bookFromBackend) => this.router.navigate(['/books', bookFromBackend.id, 'detail']),
        error: (error) => window.alert("Datos incorrectos"),
      })

      /*
       this.httpClient.post<Book>(url, book).subscribe({
        //si todo va bien se ejecuta next
        next: () => {},
        //si todo va mal se ejecuta error
        error: () => {},
      });
      */
            
    
    
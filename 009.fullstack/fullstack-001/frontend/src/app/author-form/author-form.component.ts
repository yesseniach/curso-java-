import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-author-form',
  standalone: true,
  imports: [HttpClientModule, RouterLink, ReactiveFormsModule],
  templateUrl: './author-form.component.html',
  styleUrl: './author-form.component.css'
})
export class AuthorFormComponent implements OnInit {

  authorForm = new FormGroup({
    fullName: new FormControl('')
  });
  photoFile: File | undefined;
  photoPreview: string | undefined;
  
  constructor(private httpClient: HttpClient) {}  
  
  ngOnInit(): void {

  }
  onFileChange(event: Event) {
    let target = event.target as HTMLInputElement; // este target es el input de tipo file donde se carge el archivo
    
    if(target.files === null  || target.files.length == 0){
      return; //no se procesa ningun archivo
    } 

    this.photoFile = target.files[0];

    // Opcional: Previsualizar la imagen por pantalla
    let reader = new FileReader();
    reader.onload = event => this.photoPreview = reader.result as string; 
    reader.readAsDataURL(this.photoFile);

  }

  save(){

  }

}

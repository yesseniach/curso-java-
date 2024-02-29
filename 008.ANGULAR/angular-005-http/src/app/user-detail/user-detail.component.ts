import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { User } from '../models/user.model';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-user-detail',
  standalone: true,
  imports: [HttpClientModule],
  templateUrl: './user-detail.component.html',
  styleUrl: './user-detail.component.css'
})
export class UserDetailComponent implements OnInit {

  user: User | undefined;

  constructor(
    private httpClient: HttpClient,
    private activatedRoute: ActivatedRoute
    ) {}

  ngOnInit(): void {

    this.activatedRoute.params.subscribe(params => {
      const id = params['id'];

      const backendUrl = 'https://fakestoreapi.com/users/' + id;
      this.httpClient.get<User>(backendUrl).subscribe(userFromBackend => {
        //guardar respuesta backend
        this.user = userFromBackend;

      });
    });
   
  }
  
}

import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { Register } from '../model/register.model';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [ReactiveFormsModule, HttpClientModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {

  //no necesita FormBuilder
  registerForm = new FormGroup({
    id: new FormControl(''),
    phone: new FormControl(''),
    password: new FormControl('')
  });

  save() {
    const register: Register = {
      email: this.registerForm.get('email')?.value ?? '',
      phone: this.registerForm.get('phone')?.value ?? '',
      password: this.registerForm.get('password')?.value ?? ''
    }
    console.log(register);
    //enviar registro a backend

    //limpiar el formulario
    this.registerForm.reset();
  }

}

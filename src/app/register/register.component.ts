import { HttpClient, HttpResponseBase } from '@angular/common/http';
import { ReadPropExpr } from '@angular/compiler';
import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
// import { FormBuilder, FormGroup, Validators } from '@angular/forms';
// import { MatSnackBar } from '@angular/material/snack-bar';
// import { Route,Router } from '@angular/router';
// import { LoginComponent } from '../login/login.component';
// import { ProserviceService } from '../proservice.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  register:any=FormGroup;
  url1 = 'http://localhost:5000/api/register'
}

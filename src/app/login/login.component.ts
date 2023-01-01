import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import {MatSnackBar, MatSnackBarModule} from '@angular/material/snack-bar';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { ProserviceService } from '../proservice.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  login:any =FormGroup;
  users:any=[];
  url = 'http://localhost:5000/api/readusers';
  constructor(private fb:FormBuilder,private router: Router,private proser: ProserviceService,private http: HttpClient, private snb: MatSnackBar){}

  ngOnInit(): void {

    this.login = this.fb.group({
      email:["",Validators.compose([Validators.required,Validators.email])],
      password:["",Validators.compose([Validators.required,Validators.minLength(7)])]

    })

    this.http.get<any>(this.url).subscribe((data:any) => {
      this.users = data['data'];
      console.log(this.users);
    });
    
  }

  onlogin(data:any){

    if(data.email)
    {
      this.users.forEach((item:any) =>{
      if(item.email == data.email && item.password == data.password){
        console.log(data)
        this.snb.open("Logged Successfully", 'close', {duration: 4000});
        this.router.navigate(['home'])
      }
      else {
        localStorage.clear();
      }
      });
    }
  }

  goToSignup(){
    this.router.navigate(['register']);
  }
}

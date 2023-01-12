import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Chart, registerables } from 'chart.js';
import { Router } from '@angular/router';

@Component({
  selector: 'app-display',
  templateUrl: './display.component.html',
  styleUrls: ['./display.component.css']
})
export class DisplayComponent implements OnInit {
 
  templist:any=[];
  passengers:any=[];
  forevalue:any=[];
  dates: any =[];
  ms:any=[];
  schar=false
  smet=false


  constructor(private http:HttpClient,private route:Router) { Chart.register(... registerables)}
 
  ngOnInit(): void {
    let nurl = "http://localhost:5000/api/get_data"
  
  }
  formetrics()
  {
    this.smet=true
    this.schar=false
  }
  onback()
  {
    this.route.navigate(['home'])
  }
  routelogout()
  {
    this.route.navigate(['signup'])
  }
}
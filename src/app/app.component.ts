import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'sfa';
  constructor(private route:Router){}
  onEnter()
  {
    this.route.navigate(['signup']);
  }
}

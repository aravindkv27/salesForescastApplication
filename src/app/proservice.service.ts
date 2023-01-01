import { Injectable } from '@angular/core';
import { environment } from 'src/environment/environment';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class ProserviceService {
  constructor(private http: HttpClient) { }

  // getUser()
  // {
  //   return this.http.get();
  // }

  // addUser(data: any){
  //     return this.http.post(this.baseurl,data)
  // }
}

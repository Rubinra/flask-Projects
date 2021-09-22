import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {  Order } from '../model/order.model';
import{Observable} from 'rxjs';

const baseUrl = 'http://localhost:8084/';

@Injectable({
  providedIn: 'root'
})
export class OrderService {

  constructor(private http:HttpClient) { }

  
}

import { Injectable } from '@angular/core';
import{HttpClient} from '@angular/common/http';
import{Observable} from 'rxjs';
import { Products } from '../model/product.model';


const baseUrl = 'http://localhost:8084/listproducts';

@Injectable({
  providedIn: 'root'
})

export class ProductserviceService {

constructor(private http: HttpClient) { }

getProducts(): Observable<any> {
  return this.http.get(baseUrl);
}

}

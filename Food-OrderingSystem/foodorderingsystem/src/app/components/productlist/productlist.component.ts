import { Component, OnInit } from '@angular/core';
import { Products } from '../../model/product.model';
import {ProductserviceService } from '../../services/productservice.service';
import { ActivatedRoute, Router } from '@angular/router';


@Component({
  selector: 'app-productlist',
  templateUrl: './productlist.component.html',
  styleUrls: ['./productlist.component.css']
})

export class ProductlistComponent implements OnInit 
{

  products?: Products[];

  constructor(private productService:ProductserviceService, private route: ActivatedRoute,private router: Router) { }

  ngOnInit(): void 
  {
  this.getProducts();  
  }

  getProducts(): void {
    this.productService.getProducts()
      .subscribe(
        data => {
          this.products = data;
        },
        error => {
          console.error(error);
        });
        
  }


}

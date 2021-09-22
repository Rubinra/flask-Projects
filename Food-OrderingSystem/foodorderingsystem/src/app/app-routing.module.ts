import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { OrderComponent } from './components/order/order.component';
import { ProductlistComponent } from './components/productlist/productlist.component';
import { RegistrationComponent } from './components/registration/registration.component';

const routes: Routes =
 [
  { path: '', component:LoginComponent },
  { path: 'products', component: ProductlistComponent },
  { path: 'order', component: OrderComponent },
  { path: 'navbar', component: NavbarComponent },
  { path: 'register', component: RegistrationComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {User} from '../../models/user';

@Component({
  selector: 'login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {


  router:Router;
  name:String;
  password:String;
  constructor(router:Router) {
    this.router=router;
    
   }

  ngOnInit() {
  }
public onSubmit(){
  console.log('form submit clicked..');
  this.router.navigateByUrl('/dashboard');
  
}
}

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  router:Router;
  constructor(router:Router) {
    this.router=router;
   }

  ngOnInit() {
  }
  public onSubmit(){
    console.log("registered");
    this.router.navigateByUrl('/dashboard');
  }
}

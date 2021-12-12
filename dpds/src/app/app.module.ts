import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { GoogleChartsModule } from 'angular-google-charts';
 
import { AppComponent } from './app.component';
import { LoginComponent } from '../app/components/login/login.component';
import { SignupComponent } from '../app/components/signup/signup.component';
import { MainComponent } from '../app/components/main/main.component';
import { RouterModule,Routes} from '@angular/router'; 
import { HttpModule} from '@angular/http';
import {FormsModule} from '@angular/forms';
import {UserService} from './services/user.service';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { SendIdService } from './send-id.service';


const approutes:Routes = [
  {
    path:'',
    component: MainComponent
  },
  {
    path:'login',  
    component: LoginComponent
  },
  {
    path: 'login/signup',
    component: SignupComponent
  },
  {
    path: 'signup',
    component: SignupComponent
  },
  
  {
    path: 'dashboard',
    component: DashboardComponent
  },
  
  {
    path: 'logout',
    component: MainComponent
  },
]



@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    MainComponent,
    DashboardComponent
    
  ],
  imports: [
    GoogleChartsModule.forRoot(),
    BrowserModule,
    HttpClientModule,
    HttpModule,
    FormsModule,
    RouterModule.forRoot(approutes)
  ],
  providers: [UserService,SendIdService],
  bootstrap: [AppComponent]
})




export class AppModule { 
 }

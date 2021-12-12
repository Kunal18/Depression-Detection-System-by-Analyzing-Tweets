import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from './models/user';
@Injectable()
export class SendIdService {
  _url = 'http://127.0.0.1:5000/processid';
  constructor(private _http: HttpClient) { }

  senddata(tid){
    console.log("from services",this._url,tid);
    return this._http.post<any>(this._url,tid);
  }

}

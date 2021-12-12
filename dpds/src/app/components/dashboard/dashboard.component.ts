import { Component, OnInit } from '@angular/core';
import { SendIdService } from '../../send-id.service';

@Component({
  selector: 'dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {


  
    title: string;
    type: string;
    data: Array<Array<string | number | {}>>;
    roles: Array<{ type: string, role: string, index?: number }>;
    columnNames?: Array<string>;
    options?: {};
    height:number;
    width:number;




  em_c:string[];
  graph:boolean;
  gdata:any[];
  constructor(private _sendIdService: SendIdService) { 
    // this.em_c=[];
     this.graph=false;
     
  }
  
  ngOnInit() {  
  }

  gotResult : Boolean = false;
  name : String[];

  onAnalyze(twitter_id){
    this.gotResult = false;
    this.em_c=[];
    this.gdata = [];
    //console.log(this.em_c);
    //this.graph=false;
    var tid = { "id" : twitter_id }
    console.log(tid);
    this._sendIdService.senddata(tid)
    .subscribe(
      (data) => {
        this.gotResult = true;
        
        //console.log(data);
        //for (var i in data) { console.log(data[i].t,data[i].r); }
        //data = JSON.stringify(data);
        this.name = data;
        console.log(this.name);
        for (var i in data)
        {
          //this.em_c[i]=data[i].c;
          this.gdata[i] = [ i,data[i].c];
        }
        console.log("emc",this.em_c[0]);
        this.graph=true;
        if (this.graph==true)
        {
          this.graphy();
        }
        
      },
      
      (error) => {
        return console.log('error in component', error);
      }
    )

    
      
}
graphy(){
this.type = 'LineChart';
// this.data = [
//   ["1st",  +this.em_c[0]],
//   ["2nd",  +this.em_c[1]],
//   ["3rd",  +this.em_c[2]],
//   ["4th",  +this.em_c[3]],
  
// ];
this.data = this.gdata;
console.log("grpph",this.data)
this.columnNames = ["Timeline", "Sentiment"];
this.options = {  
  curveType:"function" ,
  hAxis: {
      title: 'Timeline'
  },
  vAxis:{
      title: 'Sentiments'
  },
};
this.width = 550;
this.height = 400;
}


}




  


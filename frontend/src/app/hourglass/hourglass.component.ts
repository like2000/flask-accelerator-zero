import {Component, Injectable, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-hourglass',
  templateUrl: './hourglass.component.html',
  styleUrls: ['./hourglass.component.css']
})
@Injectable()
export class HourglassComponent implements OnInit {

  serverData: JSON;

  constructor(private httpClient: HttpClient) {
  }

  ngOnInit(): void {
  }

  getData(): void {
    const url = 'http://flask-accelerator-zero.herokuapp.com/data';
    this.httpClient.get(url).subscribe(value => {
      this.serverData = value as JSON;
    });
    console.log('From angular!');
    console.log(this.serverData);
  }
}

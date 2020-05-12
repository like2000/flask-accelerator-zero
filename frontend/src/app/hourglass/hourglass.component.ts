import {Component, Injectable, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-hourglass',
  templateUrl: './hourglass.component.html',
  styleUrls: ['./hourglass.component.css']
})
@Injectable()
export class HourglassComponent implements OnInit {

  serverData;

  // serverData: JSON;

  constructor(private httpClient: HttpClient) {
  }

  ngOnInit(): void {
  }

  getData(): void {
    const url = 'https://accelerator-zero.herokuapp.com/data';
    this.httpClient.get(url).subscribe(value => {
      this.serverData = value as JSON;
    });
    this.serverData = [
      {Start: 1, Stop: 2, Period: 3}
    ];
    console.log('From angular!');
    console.log(this.serverData);
  }
}

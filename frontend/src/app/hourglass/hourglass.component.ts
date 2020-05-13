import {Component, Injectable, OnInit, Type} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {MatTableDataSource} from '@angular/material/table';

interface HourGlassElement {
  start: string;
  stop: string;
  period: string;
}


@Component({
  selector: 'app-hourglass',
  templateUrl: './hourglass.component.html',
  styleUrls: ['./hourglass.component.css']
})
@Injectable()
export class HourglassComponent implements OnInit {


  hourGlassElement = {};

  serverData: JSON;
  dataSource: MatTableDataSource<HourGlassElement>;

//   ngOnInit() {
//   this.yourService.getData()
//     .subscribe((data: Type[]) => {
//       this.data = data;
//       this.dataSource = new MatTableDataSource(data);
//     });
// }

  constructor(private httpClient: HttpClient) {
  }

  ngOnInit(): void {
  }

  getData(): void {
    const url = 'https://accelerator-zero.herokuapp.com/data';
    this.httpClient.get(url).subscribe(value => {
      this.serverData = value as JSON;
      this.dataSource = new MatTableDataSource();
    });
    // this.serverData = [
    //   {Start: 1, Stop: 2, Period: 3}
    // ];
    console.log(JSON.stringify(this.serverData));
    console.log('From angular!');
  }
}

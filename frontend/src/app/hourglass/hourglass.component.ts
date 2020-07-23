import {Component, Injectable, OnInit, Type, ViewChild} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {MatTableDataSource} from '@angular/material/table';
import {NONE_TYPE} from '@angular/compiler';
import {MatPaginator} from '@angular/material/paginator';

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


  serverData: JSON;
  dataSource: MatTableDataSource<any>;
  @ViewChild(MatPaginator) paginator: MatPaginator;


  constructor(private httpClient: HttpClient) {
  }

  ngOnInit(): void {
    this.dataSource = new MatTableDataSource<any>();
    this.dataSource.paginator = this.paginator;
    this.getData();
  }

  getData(): void {
    // const url = 'http://127.0.0.1:5000/moment/newData';
    const url = 'https://accelerator-zero.herokuapp.com/moment/newData';
    this.httpClient.get(url).subscribe((value: any[]) => {
      // value = [
      //   {username: 'bruce', email: 'li', password_hash: 'Holla'},
      //   {username: 'mei', email: 'li', password_hash: 'You'}
      // ];
      this.dataSource.data = value;
      this.serverData = value as unknown as JSON;
      // this.dataSource.paginator = this.paginator;
    });
    console.log(this.serverData);
    console.log('From angular!');
  }
}

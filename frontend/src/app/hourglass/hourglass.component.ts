import {Component, Injectable, OnInit, Type, ViewChild} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {MatTableDataSource} from '@angular/material/table';
import {MatPaginator} from '@angular/material/paginator';

interface HourGlassElement {
  start: string;
  stop: string;
  period: string;
}

// const host = 'localhost';
const host = 'accelerator-zero.herokuapp.com';

@Component({
  selector: 'app-hourglass',
  templateUrl: './hourglass.component.html',
  styleUrls: ['./hourglass.component.css']
})

@Injectable()
export class HourglassComponent implements OnInit {

  background: any;
  serverData: JSON;
  dataSource: MatTableDataSource<any>;
  @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(private httpClient: HttpClient) {
  }

  ngOnInit(): void {
    this.background = 'primary';

    this.dataSource = new MatTableDataSource<any>();
    this.dataSource.paginator = this.paginator;
    this.showData();
  }

  showData(): void {
    const url = 'http://' + host + ':5000/chronograph/new_data';
    this.httpClient.get(url).subscribe((value: any[]) => {
      this.dataSource.data = value;
      // this.dataSource.paginator = this.paginator;
      this.serverData = value as unknown as JSON;
    });
  }

  newData(): void {
    const url = 'http://' + host + ':5000/chronograph/new_data';
    this.httpClient.get(url).subscribe((value: any[]) => {
      this.dataSource.data = value;
      // this.dataSource.paginator = this.paginator;
      this.serverData = value as unknown as JSON;
    });
  }
}

import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {HourglassComponent} from './hourglass/hourglass.component';
import {AlbumComponent} from './album/album.component';


const routes: Routes = [
  {
    path: 'home',
    component: HourglassComponent
  },
  {
    path: 'album',
    component: AlbumComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}

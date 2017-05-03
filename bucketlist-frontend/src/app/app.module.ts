import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { BucketlistsComponent } from './pages/bucketlists/bucketlists.component';
import { BucketlistComponent } from './pages/bucketlist/bucketlist.component';

import { BucketlistService } from './bucketlist.service';

const appRoutes: Routes = [
  { path: 'bucketlists', component: BucketlistsComponent },
  { path: 'bucketlists/:id', component: BucketlistComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    BucketlistsComponent,
    BucketlistComponent
  ],
  imports: [
    RouterModule.forRoot(appRoutes),
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [BucketlistService],
  bootstrap: [AppComponent]
})
export class AppModule { }

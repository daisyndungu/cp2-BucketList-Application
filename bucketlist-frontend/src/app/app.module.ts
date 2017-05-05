import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { BucketlistsComponent } from './pages/bucketlists/bucketlists.component';
import { BucketlistComponent } from './pages/bucketlist/bucketlist.component';
import { BucketlistSearchComponent } from './pages/bucketlist-search/bucketlist-search.component';
import { ItemsComponent } from './pages/items/items.component';

import { BucketlistService } from './bucketlist.service';
import { ItemComponent } from './pages/item/item.component';



const appRoutes: Routes = [
  { path: 'bucketlists', component: BucketlistsComponent },
  { path: 'bucketlists/:id', component: BucketlistComponent },
  { path: 'bucketlists/:id/items', component: ItemsComponent },
  { path: 'bucketlists/:id/items/:item_id', component: ItemComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    BucketlistsComponent,
    BucketlistComponent,
    BucketlistSearchComponent,
    ItemsComponent,
    ItemComponent
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

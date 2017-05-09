import { NgModule } from '@angular/core'
import { HttpModule } from '@angular/http'
import { FormsModule } from '@angular/forms'
import { RouterModule, Routes } from '@angular/router'
import { BrowserModule } from '@angular/platform-browser'

import { AppComponent } from './app.component'
import { BucketlistService } from './bucketlist.service'
import { ItemComponent } from './pages/item/item.component'
import { ItemsComponent } from './pages/items/items.component'
import { UserLoginComponent } from './pages/user-login/user-login.component'
import { BucketlistComponent } from './pages/bucketlist/bucketlist.component'
import { BucketlistsComponent } from './pages/bucketlists/bucketlists.component'
import { UserRegistrationComponent } from './pages/user-registration/user-registration.component'

const appRoutes: Routes = [
  { path: '', redirectTo:'/bucketlists', pathMatch: 'full' },
  { path: 'bucketlists', component: BucketlistsComponent },
  { path: 'bucketlists/:id', component: BucketlistComponent },
  { path: 'bucketlists/:id/items', component: ItemsComponent },
  { path: 'bucketlists/:id/items/:item_id', component: ItemComponent },
  { path: 'auth/register', component: UserRegistrationComponent },
  { path: 'auth/login', component: UserLoginComponent }
  
];

@NgModule({
  declarations: [
    AppComponent,
    BucketlistsComponent,
    BucketlistComponent,
    ItemsComponent,
    ItemComponent,
    UserRegistrationComponent,
    UserLoginComponent
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

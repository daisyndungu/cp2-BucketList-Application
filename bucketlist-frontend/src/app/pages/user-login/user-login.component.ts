import { Component, OnInit } from '@angular/core';

import { BucketlistService } from '../../bucketlist.service'

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent implements OnInit {

  constructor(private bucketlistService: BucketlistService) { }
userLogin(username: string, password: string): any {
    username = username.trim();
    password = password.trim();
    if (!username) { return; }
    this.bucketlistService.userLogin(username, password).subscribe(
      
        
        ); 
  }
  ngOnInit() {
  }

}

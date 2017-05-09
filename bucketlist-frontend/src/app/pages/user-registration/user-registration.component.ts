import { Component, OnInit } from '@angular/core';

import { BucketlistService } from '../../bucketlist.service'
@Component({
  selector: 'app-user-registration',
  templateUrl: './user-registration.component.html',
  styleUrls: ['./user-registration.component.css']
})
export class UserRegistrationComponent implements OnInit {
  constructor(private bucketlistService: BucketlistService) {
    
   }

  addUser(username: string, email: string, password: string): any {
    username = username.trim();
    email = email.trim();
    password = password.trim();
    if (!username) { return; }
    this.bucketlistService.addUser(username, email, password).subscribe(
      // Returns the updated list of all bucketlists
      
        
        ); 
  }
  ngOnInit() {
    
  }

}

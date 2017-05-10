import { Component, OnInit } from '@angular/core'
import { Router }            from '@angular/router';

import { BucketlistService } from '../../bucketlist.service'

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent implements OnInit {
  loading = false;
  error = '';
  constructor(private bucketlistService: BucketlistService, private router: Router) { }
userLogin(username: string, password: string): any {
    username = username.trim();
    password = password.trim();
    if (!username) { return; }
    this.bucketlistService.userLogin(username, password).subscribe(
      result => {
                if (result === true) {
                    // login successful
                    this.router.navigate(['bucketlists']);
                } else {
                    // login failed
                    this.error = 'Username or password is incorrect';
                    this.loading = false;
                }
      }
        
        ); 
  }
  ngOnInit() {
  }

}

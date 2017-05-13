import { Component, OnInit } from '@angular/core'
import { Router }            from '@angular/router';

import { BucketlistService } from '../../bucketlist.service'

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['../../../assets/bootstrap/css/bootstrap-theme.min.css', 
  "../../../assets/bootstrap/css/bootstrap.css"]
})
export class UserLoginComponent implements OnInit {
  loading = false;
  error = '';
  constructor(private bucketlistService: BucketlistService,
  private router: Router) { }
userLogin(username: string, password: string): any {
    this.loading = true;
    username = username.trim();
    password = password.trim();
    if (!username) { return; }
    if (!password) { return; }
    this.bucketlistService.userLogin(username, password).subscribe(
      result => {
          setTimeout(() => { this.router.navigate(['bucketlists']); }, 3000);
        
         },
         error => {
              this.error = ("Invalid Username or password");
              this.loading = false;
         }
         
        
        ); 
  }

  register(): void {
    this.router.navigate(['auth/register']);
  }

  ngOnInit() {
  }

}

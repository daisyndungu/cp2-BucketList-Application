import { Component, OnInit } from '@angular/core'
import { Router }            from '@angular/router'
import { BucketlistService } from '../../bucketlist.service'
@Component({
  selector: 'app-user-registration',
  templateUrl: './user-registration.component.html',
  styleUrls: ['../../../assets/bootstrap/css/bootstrap-theme.min.css', 
  "../../../assets/bootstrap/css/bootstrap.css"
  ]
})
export class UserRegistrationComponent implements OnInit {
  constructor(private bucketlistService: BucketlistService, private router: Router) {
    
   }

  addUser(username: string, email: string, password: string): any {
    username = username.trim();
    email = email.trim();
    password = password.trim();
    if (!username) { return; }
    this.bucketlistService.addUser(username, email, password).subscribe(
      // Returns the updated list of all bucketlists

        );
        // Redirects to Log In page
        this.router.navigate(['auth/login']);
  }

  logIn(): void {
    this.router.navigate(['auth/login']);
  }

  ngOnInit() {
    
  }

}

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
  loading = false;
  error = '';
  message = '';
  constructor(private bucketlistService: BucketlistService, private router: Router) {
    
   }

  addUser(username: string, email: string, password: string): any {
    username = username.trim();
    email = email.trim();
    password = password.trim();
    if (!username) { return; }
    this.bucketlistService.addUser(username, email, password).subscribe(
      // Returns the updated list of all bucketlists
        result => {
          // Redirects to Log In page
          this.message = ("Registered successfully...");
          setTimeout(() => { this.router.navigate(['auth/login']); }, 300);
        
         },
         error => {
              this.error = ("Registration Failed. Please try again");
              this.loading = false;
         }
        );
        
  }

  logIn(): void {
    this.router.navigate(['auth/login']);
  }

  ngOnInit() {
    
  }

}

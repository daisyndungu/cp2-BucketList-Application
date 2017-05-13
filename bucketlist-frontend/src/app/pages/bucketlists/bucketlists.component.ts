import { Component, OnInit } from '@angular/core'
import { Router }            from '@angular/router'

import { BucketlistService } from '../../bucketlist.service'
import { BucketlistComponent } from '../bucketlist/bucketlist.component'

@Component({
  selector: 'bucketlists',
  templateUrl: './bucketlists.component.html',
  styleUrls: ['./bucketlists.component.css']
})
export class BucketlistsComponent implements OnInit {
  bucketlists: any[] = [];
  showButton=false;
  pages: any[];
  errorMessage = '';
  successMessage = '';
  constructor(private bucketlistService: BucketlistService,
    private router: Router) { }

  ngOnInit() {
    this.getBucketlists();
    
  }

add(name: string): void {
    name = name.trim();
    if (!name) { return; }
    this.bucketlistService.add(name).subscribe(
      // Returns the updated list of all bucketlists
        result => {
                
                    // Deleted successful
                    this.successMessage = ("Bucketlist added succesfully");
                    setTimeout( () => this.getBucketlists(), 3);
                    
                      
      },
      error => {
                
              // Deleted successful
              this.errorMessage = ("Bucketlist already exists");
              setTimeout( () => this.getBucketlists(), 30);
                    
                       
      }
      );
  }

//  Get All bucketlists
  getBucketlists(): any {
    this.bucketlistService.getBucketlists()
      .subscribe(
        
        bucketlists => this.bucketlists = bucketlists.bucketlist

      );
  }
  
  items(id): void {
    this.router.navigate(['bucketlists/' + id + '/items']);
  }

  delete(bucketlist): any {
    // Delete a bucketlist by its ID
    this.bucketlistService.delete(bucketlist.bucketlist_id).subscribe(
      // Returns the updated list of all bucketlists
      result => {
                if (result) {
                    // Deleted successful
                    this.errorMessage = ("Bucketlist deleted");
                    setTimeout( () => this.getBucketlists(), 30);
                    
                }
                
      });
        

    }

  edit(id): void {
    
    this.router.navigate(['bucketlists/' + id]);
  }

  goBack(): void {
    this.getBucketlists();
    this.showButton=false
  }

  search(name): any {
    name = name.trim();
    if (!name) { return; }
      this.bucketlistService.search(name).subscribe(

        bucketlists => this.bucketlists = bucketlists
        
        
        );
        this.showButton=true
    }
  
  logout(): void {
    this.bucketlistService.logout()
    this.router.navigate(['auth/login']);
  }
  
     
}



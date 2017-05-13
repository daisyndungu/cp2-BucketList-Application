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
  message = '';
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
        () => this.getBucketlists());
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
                    // login successful
                    this.message = ("Bucketlist deleted succesfully");
                    () => this.getBucketlists();
                } else {
                    // login failed
                     this.message = ("Invalid Username or password");
                    
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
  
     
}



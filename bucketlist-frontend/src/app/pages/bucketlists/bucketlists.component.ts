import { Component, OnInit } from '@angular/core'
import { Router }            from '@angular/router'
import * as _ from 'underscore';

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
  range: any[]=[];
  per_page: number;
  next_page: string;
  prev_page: string;
  total_pages: number;
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
        
        bucketlists => {this.bucketlists = bucketlists,
          this.per_page = bucketlists.meta.per_page,
          this.total_pages = bucketlists.meta.total_pages,
          this.range = _.range(1, this.total_pages),
          this.next_page = bucketlists.meta.next_page,
          this.prev_page = bucketlists.meta.prev_page

        }

      );
  }

  toPage(page_number, per_page): any {
    this.bucketlistService.toPage(page_number, per_page)
      .subscribe(
        
        bucketlists => {this.bucketlists = bucketlists,
          this.per_page = bucketlists.meta.per_page,
          this.total_pages = bucketlists.meta.total_pages,
          this.range = _.range(1, this.total_pages),
          this.next_page = bucketlists.meta.next_page,
          this.prev_page = bucketlists.meta.prev_page

        }

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

  nextPreviousPage(page_url): any {
    this.bucketlistService.nextPreviousPage(page_url)
      .subscribe(
        
        bucketlists => {this.bucketlists = bucketlists,
          this.per_page = bucketlists.meta.per_page,
          this.total_pages = bucketlists.meta.total_pages,
          this.range = _.range(1, this.total_pages),
          this.next_page = bucketlists.meta.next_page,
          this.prev_page = bucketlists.meta.previous_page

        }

      );
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



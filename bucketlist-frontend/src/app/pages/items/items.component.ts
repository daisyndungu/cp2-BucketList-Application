import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import { Router }            from '@angular/router';
import { BucketlistService } from '../../bucketlist.service'

@Component({
  selector: 'items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.css']
})
export class ItemsComponent implements OnInit {
  items: any[] = [];
  bucketlist_id: number;
  errorMessage = '';
  successMessage = '';
  constructor(route: ActivatedRoute, private bucketlistService: BucketlistService,
  private router: Router) { 
    this.bucketlist_id = route.snapshot.params['id']
  }
  getItems(bucketlist_id): void {
    this.bucketlistService.getItems(bucketlist_id)
      .subscribe(
        items => this.items = items
      )
  }

  add(name: string, description: string): any {
    name = name.trim();
    description = description.trim();
    if (!name) { return; }
    this.bucketlistService.addItem(name, description, this.bucketlist_id).subscribe(
    
        result => {
                
                    // Create item successful
                    this.successMessage = ("Item added succesfully");
                    setTimeout( () => this.getItems(this.bucketlist_id), 3);
                    
                      
      },
      error => {
                
              // Deleted successful
              this.errorMessage = ("Item already exists");
              setTimeout( () => this.getItems(this.bucketlist_id), 30);
                    
                       
      }
        
        ); 
  }

  delete(item_id, bucketlist_id): any {
    // Delete a bucketlist by its ID
    this.bucketlistService.deleteItem(item_id, this.bucketlist_id).subscribe(
      // Returns the updated list of all bucketlists
        result => {
                if (result) {
                    // Deleted successful
                    this.errorMessage = ("Item deleted");
                    setTimeout( () => this.getItems(this.bucketlist_id), 30);
                    
                }
                
      }
        );
        

    }

  edit(id): void {
    
    this.router.navigate(['bucketlists/'+ this.bucketlist_id + '/items/' + id]);
  }

  goBack(): void {
    this.router.navigate(['bucketlists']);
  }

  logout(): void {
    this.bucketlistService.logout()
    this.router.navigate(['auth/login']);
  }

  ngOnInit() {
    this.getItems(this.bucketlist_id);
    console.log(this.bucketlist_id)
  }

}

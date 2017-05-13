import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Router }            from '@angular/router';

import { BucketlistService } from '../../bucketlist.service'

@Component({
  selector: 'item',
  templateUrl: './item.component.html'
})
export class ItemComponent implements OnInit {

  id: number;
  item_id: number;
  item: any;
  errorMessage = '';
  successMessage = '';
  constructor(route: ActivatedRoute, private bucketlistService: BucketlistService,
    private router: Router) {
      this.id = route.snapshot.params['id'],
      this.item_id = route.snapshot.params['item_id']
     }

  ngOnInit() {
    this.getItem(this.id, this.item_id);
    console.log(this.id)
    console.log(this.item_id)
  }

  getItem(bucketlist_id, item_id): any {
    this.bucketlistService.getItem(bucketlist_id, item_id)
      .subscribe(
        item => this.item = item
      )
  }


  goBack(): void {
    this.router.navigate(['bucketlists/' + this.id + '/items']);
  }

  save(name: any, description: any, status: any, bucketlist_id: number,  item_id: number): void {
    this.bucketlistService.updateItem(name, description, status, this.id, this.item_id).subscribe(
      
      result => {
                
                    // Deleted successful
                    this.successMessage = ("Item eddited successfully.");
                    setTimeout( () =>  this.getItem(this.id, this.item_id), 3);
                    
                      
      },
      error => {
                
              // Deleted successful
              this.errorMessage = ("Item already exists");
              setTimeout( () =>  this.getItem(this.id, this.item_id), 3);
                       
      }
      );
    
  }

}

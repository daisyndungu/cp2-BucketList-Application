import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';

import { BucketlistService } from '../../bucketlist.service'

@Component({
  selector: 'items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.css']
})
export class ItemsComponent implements OnInit {
  items: any[] = [];
  bucketlist_id: number;
  constructor(route: ActivatedRoute, private bucketlistService: BucketlistService) { 
    this.bucketlist_id = route.snapshot.params['id']
  }
  getItems(bucketlist_id): void {
    this.bucketlistService.getItems(bucketlist_id)
      .subscribe(
        items => this.items = items
      )
  }

  add(name: string, description: string, status: string): any {
    name = name.trim();
    description = description.trim();
    status = status.trim();
    if (!name) { return; }
    this.bucketlistService.addItem(name, description, status, this.bucketlist_id).subscribe(
      // Returns the updated list of all bucketlists
      
        () => this.getItems(this.bucketlist_id)
        );

     
  }

  ngOnInit() {
    this.getItems(this.bucketlist_id);
    console.log(this.bucketlist_id)
  }

}

import { Component, OnInit } from '@angular/core';
import { BucketlistService } from '../../bucketlist.service'

@Component({
  selector: 'app-bucketlists',
  templateUrl: './bucketlists.component.html',
  styleUrls: ['./bucketlists.component.css']
})
export class BucketlistsComponent implements OnInit {
  bucketlists: any[] = [];
  constructor(private bucketlistService: BucketlistService) { }

  ngOnInit() {
    this.getBucketlists();
    console.log(this.bucketlists);
    
  }

add(name: string): void {
    name = name.trim();
    if (!name) { return; }
    this.bucketlistService.add(name).subscribe(
      // Returns the updated list of all bucketlists
        () => this.getBucketlists());

     
  }

//  Get All bucketlists
  getBucketlists(): void {
    this.bucketlistService.getBucketlists()
      .subscribe(
        bucketlists => this.bucketlists = bucketlists
      )
  }
  
  delete(bucketlist): void {
    // Delete a bucketlist by its ID
    this.bucketlistService.delete(bucketlist.bucketlist_id).subscribe(
      // Returns the updated list of all bucketlists
        () => this.getBucketlists());

    }

  edit(bucketlist): void {
    // Edit a bucketlist by its ID
    this.bucketlistService.update(bucketlist.bucketlist_id).subscribe(
      // Returns the updated list of all bucketlists
        () => this.getBucketlists());

    }
    
}



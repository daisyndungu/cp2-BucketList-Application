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

  getBucketlists(): void {
    this.bucketlistService.getBucketlists()
      .subscribe(
        bucketlists => this.bucketlists = bucketlists
      )
  }

  // delete(bucketlist: BucketList): void {
  //   this.bucketlistService
  //   .delete(bucketlist.bucketlist_id)
  //     .then(() => {
  //       this.bucketlists = this.bucketlists.filter(h => h !== bucketlist);
  //       if (this.selectedBucketlist === bucketlist) { this.selectedBucketlist = null; }
  //     });
// }
}


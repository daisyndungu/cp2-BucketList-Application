import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';

import { BucketlistService } from '../../bucketlist.service'


@Component({
  selector: 'app-bucketlist',
  templateUrl: './bucketlist.component.html',
  styleUrls: ['./bucketlist.component.css']
})
export class BucketlistComponent implements OnInit {
  bucketlist: string;
  constructor(route: ActivatedRoute, private bucketlistService: BucketlistService) { 
    this.bucketlist = route.snapshot.params['id']
  }

  ngOnInit() {
    this.getBucketlist(this.bucketlist);
  }

getBucketlist(bucketlist_id): any {
    this.bucketlistService.getBucketlist(bucketlist_id)
      .subscribe(
        bucketlist => this.bucketlist = bucketlist
      )
  }
}

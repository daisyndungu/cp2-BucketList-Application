import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Router }            from '@angular/router';

import { BucketlistService } from '../../bucketlist.service'


@Component({
  selector: 'app-bucketlist',
  templateUrl: './bucketlist.component.html',
  styleUrls: ['./bucketlist.component.css']
})
export class BucketlistComponent implements OnInit {
  bucketlist: number;
  constructor(route: ActivatedRoute, private bucketlistService: BucketlistService,
    private router: Router) { 
    this.bucketlist = route.snapshot.params['id']
  }

  ngOnInit() {
    this.getBucketlist(this.bucketlist);
    console.log(this.bucketlist)

  }

getBucketlist(bucketlist_id): any {
    this.bucketlistService.getBucketlist(bucketlist_id)
      .subscribe(
        bucketlist => this.bucketlist = bucketlist
      )
  }

goBack(): void {
  this.router.navigate(['bucketlists']);
}

save(name: string, bucketlist_id: number): void {
  this.bucketlistService.update(name, bucketlist_id).subscribe(
    () =>  this.getBucketlist(bucketlist_id));
  
}


}

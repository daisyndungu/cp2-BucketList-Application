import { Component, OnInit } from '@angular/core';
import { Router }            from '@angular/router';

import { Observable }        from 'rxjs/Observable';
import { Subject }           from 'rxjs/Subject';
import 'rxjs/add/observable/of';

// Observable operators
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/debounceTime';
import 'rxjs/add/operator/distinctUntilChanged';
import 'rxjs/add/operator/switchMap';

import { BucketlistService } from '../../bucketlist.service'
// import { Bucketlist } from '../../bucketlist'

@Component({
  selector: 'bucketlist-search',
  templateUrl: './bucketlist-search.component.html',
  styleUrls: ['./bucketlist-search.component.css']
})
export class BucketlistSearchComponent implements OnInit {
  // heroes: bucketlist[];
   bucketlists: any[] = [];
  private searchTerms = new Subject<string>();

  constructor(private bucketlistService: BucketlistService,
              private router: Router
  ) { }

//   search(bucketlist): void {
//     // Updates a bucketlist by its ID
//     this.searchTerms.next(bucketlist);

//     }

//   ngOnInit(): void {
//     this.heroes = this.searchTerms
//       .debounceTime(300)        // wait 300ms after each keystroke before considering the term
//       .distinctUntilChanged()   // ignore if next search term is same as previous
//       .switchMap(bucketlist => bucketlist   // switch to new observable each time the term changes
//         // return the http search observable
//         ? this.bucketlistService.search(bucketlist)
//         // or the observable of empty heroes if there was no search term
//         : Observable.of<Bucketlist[]>([]))
//       .catch(error => {
//         // TODO: add real error handling
//         console.log(error);
//         return Observable.of<Bucketlist[]>([]);
//       });
//   }

//   gotoDetail(bucketlist: Bucketlist): void {
//     let link = ['/detail', bucketlist.name];
//     this.router.navigate(link);
  
// }

  search(bucketlist): void {
    // Delete a bucketlist by its ID
    this.bucketlistService.search(bucketlist).subscribe(
      bucketlists => this.bucketlists = bucketlists
    )
      // Returns the updated list of all bucketlists
        
    }

    ngOnInit() {
    this.search(this.bucketlists);
    console.log(this.bucketlists);
    
  }

}

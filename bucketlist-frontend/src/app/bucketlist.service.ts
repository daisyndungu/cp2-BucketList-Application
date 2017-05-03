import { Injectable }    from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Observable } from 'rxjs/Observable'
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class BucketlistService {
  private headers = new Headers({'Content-Type': 'application/json'});
  private baseUrl = 'http://127.0.0.1:5000';  // URL to web api
  
  constructor(private http: Http) { }
  getBucketlists(): Observable<any> {
    return this.http
        .get(`${this.baseUrl}/bucketlists/`)
        .map(response => response.json())
        .catch(this.handleError);
  }

  getBucketlist(bucketlist_id: number): Observable<any> {
    
    return this.http
        .get(`${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}`)
        .map(response => response.json())
        .catch(this.handleError);
  }

  delete(id: number): Observable<void> {
    const url = `${this.baseUrl}` + `/bucketlists/` + `${id}`;
    return this.http.delete(url)
      .catch(this.handleError);
  }

  private extractData(res: Response) {
    

  }
  
  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}

 
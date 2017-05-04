import { Injectable }    from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Observable } from 'rxjs/Observable'
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
// import { Bucketlist } from './bucketlist';

@Injectable()
export class BucketlistService {
  private headers = new Headers({"Content-Type": "application/json"});
  private baseUrl = 'http://127.0.0.1:5000';  // URL to web api
  
  
  constructor(private http: Http) { }
  getBucketlists(): Observable<any> {
    return this.http
        .get(`${this.baseUrl}/bucketlists`)
        .map(response => response.json())
        .catch(this.handleError);
  }

  getBucketlist(bucketlist_id: number): Observable<any> {
    
    return this.http
        .get(`${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}`)
        .map(response => response.json())
        .catch(this.handleError);
  }

  getItems(bucketlist_id: number): Observable<any> {
    
    return this.http
        .get(`${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}`  +  `/items/`)
        .map(response => response.json())
        .catch(this.handleError);
  }

  delete(id: number): Observable<void> {
    const url = `${this.baseUrl}` + `/bucketlists/` + `${id}`;
    return this.http.delete(url)
      .catch(this.handleError);
  }

  update(name: any, bucketlist_id: number): Observable<any> {
    const url = `${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}`;
    return this.http.put(url, JSON.stringify({'name': name}), {headers: this.headers})
      .catch(this.handleError);
  }

  search(term: string): Observable<any> {
    const url = `${this.baseUrl}` + `/bucketlists/` + `?q=${term}`;
    return this.http
               .get(url)
               .map(response => response.json());
  }
  add(name: string): Observable<any> {
    const url = `${this.baseUrl}` + `/bucketlists/`;
    return this.http
               .post(url, JSON.stringify({'name': name}), {headers: this.headers})
               .map(response => response.json());
  }

  addItem(name: string, description: string, status: string, bucketlist_id: number): Observable<any[]> {
    const url = `${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}` + `/items/`;
    return this.http
               .post(url, JSON.stringify({'name': name, 'description': description, 'status': status}), {headers: this.headers})
               .map(response => response.json());
  }

  deleteItem(item_id: number, bucketlist_id: number): Observable<any[]> {
    const url = `${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}` + `/items/` + `${item_id}`;
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

 
import { Injectable }    from '@angular/core';
import { Headers, Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw'

@Injectable()
export class BucketlistService {
  private headers = new Headers(
    {
      "Content-Type": "application/json"
    });
  // Create headers for all endpoints that require authorization
  private authHeader = new Headers(
    {
      "Access-Control-Allow-Origin": '*',
       "Content-Type": "application/json",
       "Authorization": localStorage.getItem('currentUser')
    }
  )

  private baseUrl = 'http://127.0.0.1:5000';  // URL to web api
  // Get token if already exists
  token = localStorage.getItem('currentUser');
  
  constructor(private http: Http) { 
  }
  // Add new user
  addUser(username: string, email: string, password: string): Observable<any> {
    const url = `${this.baseUrl}` + `/auth/register`;
    return this.http
               .post(url, JSON.stringify({'username': username, 'email': email, 'password': password}), {headers: this.headers})
               .map(response => response.json());
  }
  
  userLogin(username: string, password: string): Observable<any> {
    /**
     * Login a registered user and saves the generated token in the local memory
     */
    const url = `${this.baseUrl}` + `/auth/login`;
    return this.http
               .post(url, JSON.stringify({'username': username, 'password': password}), {headers: this.headers})
               .map((response: Response) => {
               let token = response.json().Token;
               if (token) {
                 this.token = token;

                 // store jwt token in local storage to keep user logged in between page refreshes
                 localStorage.setItem('currentUser', this.token);
               }
                
               })

  }

  logout() {
        // remove token from local storage to log user out
        localStorage.removeItem('currentUser');
    }

  getBucketlists(): Observable<any> {
    /**
     * Fetch all bucketlists that belongs to the logged in user
     */
    return this.http
        .get(`${this.baseUrl}/bucketlists/`, {headers: this.authHeader})
        .map(response => response.json())
        .catch(this.handleError);
  }

  getBucketlist(bucketlist_id: number): Observable<any> {
    /**
     * Fetch one bucketlist that belongs to the logged in user
     */
    return this.http
        .get(`${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}`, {headers: this.authHeader})
        .map(response => response.json())
        .catch(this.handleError);
  }

  getItems(bucketlist_id: number): Observable<any> {
     /**
     * Fetch all items related to the specified bucketlist id
     */
    return this.http
        .get(`${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}`  +  `/items/`, {headers: this.authHeader})
        .map(response => response.json())
        .catch(this.handleError);
  }

  getItem(bucketlist_id: number, item_id: number): Observable<any> {
    /**
     * Fetch one item related to the specified bucketlist id
     */
    return this.http
        .get(`${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}`  +  `/items/` + `${item_id}`, {headers: this.authHeader})
        .map(response => response.json())
        .catch(this.handleError);
  }

  delete(id: number): Observable<void> {
    /**
     * Delete a specified bucketlist
     */
    const url = `${this.baseUrl}` + `/bucketlists/` + `${id}`;
    return this.http.delete(url, {headers: this.authHeader})
      .catch(this.handleError);
  }

  update(name: any, bucketlist_id: number): Observable<any> {
    /**
     * Edit a specified bucketlist
     */
    const url = `${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}`;
    return this.http.put(url, JSON.stringify({'name': name}), {headers: this.authHeader})
      .catch(this.handleError);
  }

  search(term: string): Observable<any> {
    /**
     * Search for bucketlists 
     */
    const url = `${this.baseUrl}` + `/bucketlists/` + `?q=${term}`;
    return this.http
               .get(url, {headers: this.authHeader})
               .map(response => response.json());
  }
  
  toPage(page_number: number, per_page: number): Observable<any> {
    /**
     * Redirects to the page number selected when viewing all bucketlists
     */
    const url = `${this.baseUrl}` + `/bucketlists/` + `?page=${page_number}&per_page=${per_page}`;
    return this.http
               .get(url, {headers: this.authHeader})
               .map(response => response.json());
  }

  nextPreviousPage(page_url: string): Observable<any> {
    /**
     * Redirects to the next or previous page when viewing all bucketlists
     */
    const url = `${this.baseUrl}` + page_url;
    return this.http
               .get(url, {headers: this.authHeader})
               .map(response => response.json());
  }

  add(name: string): Observable<any> {
    /**
     * Add a bucketlist
     */
    const url = `${this.baseUrl}` + `/bucketlists/`;
    return this.http
               .post(url, JSON.stringify({'name': name}), {headers: this.authHeader})
               .map(response => response.json());
  }

  addItem(name: string, description: string, bucketlist_id: number): Observable<any[]> {
    /**
     * Add a bucketlist item
     */
    const url = `${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}` + `/items/`;
    return this.http
               .post(url, JSON.stringify({'name': name, 'description': description}), {headers: this.authHeader})
               .map(response => response.json());
  }

  deleteItem(item_id: number, bucketlist_id: number): Observable<any[]> {
    /**
     * Add a bucketlist item
     */
    const url = `${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}` + `/items/` + `${item_id}`;
    return this.http.delete(url, {headers: this.authHeader})
      .catch(this.handleError);
  }

  updateItem(name: any, description: any, status: any, bucketlist_id: number, item_id: number): Observable<any> {
    /**
     * Edit a bucketlist item
     */
    const url = `${this.baseUrl}` + `/bucketlists/` + `${bucketlist_id}` + `/items/` + `${item_id}`;
    return this.http.put(url, JSON.stringify({'name': name, 'description': description, 'status': status}),
    {headers: this.authHeader})
      .catch(this.handleError);
  }

  private extractData(res: Response) {
    

  }
 
  private handleError(error: Response) {
        return Observable.throw(error.json().error || 'Server error'); 
         }
}

 
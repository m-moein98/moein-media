import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { endpoints } from '../endpoints/endpoints';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(
    private httpClient: HttpClient,
  ) { }
  login(username: string, password: string) {
    const body = new HttpParams()
      .set('username', username)
      .set('password', password);
    return this.httpClient.post(endpoints.getToken,
      body.toString(),
      {
      headers: new HttpHeaders({
        'Content-Type': 'application/x-www-form-urlencoded'
      })
    });
  }
  getUser() {
    return this.httpClient.get(endpoints.getUser);
  }
}

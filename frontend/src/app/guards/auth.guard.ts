import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { DataService } from '../services/data.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(
    private dataService: DataService,
  ) { }

  getUser(token: string) {
    this.dataService.getUser().subscribe(
      (user: any) => {
        console.log(
          user
        );
      }
    );
    return true;
  }

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    const token = localStorage.getItem('token');
    if (!token) {
      return false;
    }
    if (!this.getUser(token)) {
      return false;
    }
    return true;
  }

}

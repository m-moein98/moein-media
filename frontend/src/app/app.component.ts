import { Component } from '@angular/core';
import { DataService } from './services/data.service';
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  token = localStorage.getItem('token');
  fullName: string;
  email: string;
  public appPages = [
    { title: 'Inbox', url: '/folder/Inbox', icon: 'mail' },
    { title: 'Outbox', url: '/folder/Outbox', icon: 'paper-plane' },
    { title: 'Favorites', url: '/folder/Favorites', icon: 'heart' },
    { title: 'Archived', url: '/folder/Archived', icon: 'archive' },
    { title: 'Trash', url: '/folder/Trash', icon: 'trash' },
    { title: 'Spam', url: '/folder/Spam', icon: 'warning' },
  ];
  constructor(dataservice: DataService) {
    dataservice.getUser().subscribe(data => {
      this.fullName = data["firstName"] + ' ' + data["lastName"];
      this.email = data["email"];
    }
    );
  }
}

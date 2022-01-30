import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { DataService } from 'src/app/services/data.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {

  loginForm = new FormGroup({
    username: new FormControl(''),
    password: new FormControl('')
  });

  constructor(
    private dataService: DataService,
  ) { }

  ngOnInit() { }
  onSubmit() {
    this.dataService.login(this.loginForm.value.username, this.loginForm.value.password).subscribe(
      data => {
        localStorage.setItem('token', data['access_token']);
      }
    );
  }
}


import { Component, OnInit } from '@angular/core';
import { PhotoService } from '../services/photo.service';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})
export class Tab1Page implements OnInit {

  constructor(public photoService: PhotoService) {}

  ngOnInit() {
    this.photoService.capturePhoto();
  }

  photoButtonClick() {
    this.photoService.capturePhoto();
  }

}

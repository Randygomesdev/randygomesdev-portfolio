import { Component } from '@angular/core';
import { LucideMail } from '@lucide/angular';

@Component({
  selector: 'app-footer',
  imports: [LucideMail],
  templateUrl: './footer.html'
})
export class FooterComponent {

  currentYear = new Date().getFullYear();
  angularVersion = '21'
}

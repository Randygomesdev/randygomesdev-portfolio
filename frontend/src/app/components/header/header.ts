import { Component, signal } from '@angular/core';
import { LucideCodeXml } from '@lucide/angular';

@Component({
  selector: 'app-header',
  imports: [LucideCodeXml],
  templateUrl: './header.html'
})
export class HeaderComponent {
  isMenuOpen = signal(false);

  toggleMenu() {
    this.isMenuOpen.update(v => !v);
  }
}

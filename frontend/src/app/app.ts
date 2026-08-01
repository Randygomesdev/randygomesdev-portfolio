import { Component, signal } from '@angular/core';
import { HeaderComponent } from './components/header/header';
import { HeroComponent } from './components/hero/hero';
import { ProjectsComponent } from './components/projects/projects';
import { SkillsComponent } from './components/skills/skills';
import { FooterComponent } from './components/footer/footer';
import { AboutMe } from "./components/about-me/about-me";

@Component({
  selector: 'app-root',
  imports: [
    HeaderComponent,
    HeroComponent,
    ProjectsComponent,
    SkillsComponent,
    FooterComponent,
    AboutMe
],
  templateUrl: './app.html'
})
export class App {
  protected readonly title = signal('Portfolio');
}

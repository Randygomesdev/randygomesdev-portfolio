import { Component, inject } from '@angular/core';
import { PortfolioService } from '../../services/portfolio';

@Component({
  selector: 'app-skills',
  imports: [],
  templateUrl: './skills.html'
})
export class SkillsComponent {

  protected portfolioService = inject(PortfolioService);

}

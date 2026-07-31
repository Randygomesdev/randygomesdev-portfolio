import { Component, inject } from '@angular/core';
import { PortfolioService } from '../../services/portfolio';

@Component({
  selector: 'app-projects',
  imports: [],
  templateUrl: './projects.html'
})
export class ProjectsComponent {

  protected portfolioService = inject(PortfolioService);

}

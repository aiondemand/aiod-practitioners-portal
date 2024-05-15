import { Component } from '@angular/core';
import { ExperimentListBaseComponent } from './experiment-list-base.component';
import { Experiment } from 'src/app/models/experiment';
import { Observable, of } from 'rxjs';

@Component({
  selector: 'app-all-experiment-list',
  templateUrl: './experiment-lists.component.html',
  styleUrls: ['./experiment-lists.component.scss']
})
export class AllExperimentListComponent extends ExperimentListBaseComponent {
  protected override getExperimentsCount(): Observable<number> {
    return this.backend.getExperimentsCount(
      this.searchQuery, 
      { 
        only_usable: true,
        only_public: true
      }
    );
  }

  protected override getExperiments(): Observable<Experiment[]>  {
    return this.backend.getExperiments(
      this.searchQuery,
      {
        offset: this.pagination.pageIndex * this.pagination.pageSize,
        limit: this.pagination.pageSize
      },
      {
        only_usable: true,
        only_public: true
      }
    );
  }
}

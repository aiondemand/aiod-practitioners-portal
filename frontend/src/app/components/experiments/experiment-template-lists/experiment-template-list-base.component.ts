import { Injectable } from '@angular/core';
import { FormControl } from '@angular/forms';
import { PageEvent } from '@angular/material/paginator';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { ExperimentTemplate } from 'src/app/models/experiment-template';
import { BackendApiService } from 'src/app/services/backend-api.service';
import { environment } from 'src/environments/environment';

@Injectable()
export  abstract class ExperimentTemplateListBaseComponent {
  protected experiment_templates$: Observable<ExperimentTemplate[]>;
  protected pagination = {
    pageSize: environment.DEFAULT_PAGE_SIZE,
    pageIndex: 0,
    length: 0
  }
  protected filterOpened: boolean = false;
  protected chosenDockerImages: FormControl = new FormControl("");
  protected chosenModelPlatforms: FormControl = new FormControl("");
  protected chosenDatasetPlatforms: FormControl = new FormControl("");

  protected dockerImageList: string[] = [
    "Python:3.8",
    "Python:3.9",
    "Python:3.10",
  ];
  protected platforms: string[] = [
    "HuggingFace",
    "OpenML",
    "Zenodo"
  ]

  constructor(
    protected backend: BackendApiService,
    protected route: ActivatedRoute,
    protected router: Router
  ) { }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.pagination.pageSize = params['pageSize']
        ? parseInt(params['pageSize']) : 10;
      this.pagination.pageIndex = params['pageIndex']
        ? parseInt(params['pageIndex']) : 0;

        this.experiment_templates$  = this.updateExperimentTemplates();
    });

    this.getExperimentTemplatesCount().subscribe(count => {
      this.pagination.length = count;
    });
  }

  handlePageEvent(e: PageEvent) {
    this.pagination.length = e.length;
    this.pagination.pageSize = e.pageSize;
    this.pagination.pageIndex = e.pageIndex;

    // update the route
    this.router.navigate([], {
      relativeTo: this.route,
      queryParams: {
        pageSize: this.pagination.pageSize,
        pageIndex: this.pagination.pageIndex
      },
      queryParamsHandling: 'merge'
    });

    this.experiment_templates$  = this.updateExperimentTemplates();
  }

  protected abstract updateExperimentTemplates(): Observable<ExperimentTemplate[]>;

  protected abstract getExperimentTemplatesCount(): Observable<number>
}
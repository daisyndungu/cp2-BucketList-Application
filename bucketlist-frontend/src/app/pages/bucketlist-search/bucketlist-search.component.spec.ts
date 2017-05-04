import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BucketlistSearchComponent } from './bucketlist-search.component';

describe('BucketlistSearchComponent', () => {
  let component: BucketlistSearchComponent;
  let fixture: ComponentFixture<BucketlistSearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BucketlistSearchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BucketlistSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

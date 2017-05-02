import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BucketlistsComponent } from './bucketlists.component';

describe('BucketlistsComponent', () => {
  let component: BucketlistsComponent;
  let fixture: ComponentFixture<BucketlistsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BucketlistsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BucketlistsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

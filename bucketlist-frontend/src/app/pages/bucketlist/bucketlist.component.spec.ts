import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BucketlistComponent } from './bucketlist.component';

describe('BucketlistComponent', () => {
  let component: BucketlistComponent;
  let fixture: ComponentFixture<BucketlistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BucketlistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BucketlistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { TestBed, inject } from '@angular/core/testing';

import { BucketlistService } from './bucketlist.service';

describe('BucketlistService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [BucketlistService]
    });
  });

  it('should ...', inject([BucketlistService], (service: BucketlistService) => {
    expect(service).toBeTruthy();
  }));
});

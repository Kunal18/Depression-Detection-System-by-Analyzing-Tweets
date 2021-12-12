import { TestBed, inject } from '@angular/core/testing';

import { SendIdService } from './send-id.service';

describe('SendIdService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SendIdService]
    });
  });

  it('should be created', inject([SendIdService], (service: SendIdService) => {
    expect(service).toBeTruthy();
  }));
});

import { BucketlistFrontendPage } from './app.po';

describe('bucketlist-frontend App', () => {
  let page: BucketlistFrontendPage;

  beforeEach(() => {
    page = new BucketlistFrontendPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});

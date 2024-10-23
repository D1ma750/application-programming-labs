import os
from icrawler.builtin import BingImageCrawler


def download_images(keyword: str, number_of_images: int, imgdir: str) -> None:
    if not (os.path.isdir(imgdir)):
        os.mkdir(imgdir)
    for filename in os.listdir(imgdir):
        os.remove(os.path.join(imgdir, filename))
    bing_crawler = BingImageCrawler(storage={'root_dir': imgdir})
    bing_crawler.crawl(keyword=keyword, max_num=number_of_images)


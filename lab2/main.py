import argparse
import csv
import os
from icrawler.builtin import BingImageCrawler

def download_images(keyword: str, number_of_images: int, imgdir: str):
    """
    Download images in special directory
    :param keyword: word for searching
    :param number_of_images:number of images for download
    :param imgdir: directory with images
    :return:
    """
    if not (os.path.isdir(imgdir)):
        os.mkdir(imgdir)
    for filename in os.listdir(imgdir):
        os.remove(os.path.join(imgdir, filename))
    bing_crawler = BingImageCrawler(storage={'root_dir': imgdir})
    bing_crawler.crawl(keyword=keyword, max_num=number_of_images)

def parsing_arguments():
    """
    Reads arguments from terminal
    :return: Arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="Keyword of search request")
    parser.add_argument("number_of_images", type=int, help="Number of images that you want to download")
    parser.add_argument("imgdir", type=str, help="Path to the folder, where you want to save images")
    parser.add_argument("file_with_annotation", type=str, help="Path to the annotation file")
    arguments = parser.parse_args()
    return arguments

class ImageIterator:
    def __init__(self, csv_path: str) -> None:
        self.csv_path = csv_path
        self.path_list = self.__load_csv()
        self.limit = len(self.path_list)  # ограничение
        self.counter = 0  # счётчик

    def __iter__(self) -> 'ImageIterator':
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            next_element = self.path_list[self.counter]
            self.counter += 1
            return next_element
        else:
            raise StopIteration

    def __load_csv(self) -> list:
        with open(self.csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # пропускаем заголовок
            path_list = list(row[1] for row in reader)
            return path_list

def create_annotation(imgdir: str, csv_path: str):
    """
    Creates annotation with absolute and relative paths to images
    :param imgdir: Directory with images
    :param csv_path: .csv file for annotation
    """
    with open(csv_path, mode='w', encoding='utf-8') as file_with_annotation:
        writer = csv.writer(file_with_annotation)
        headers = ['Relative path', 'Absolute path']
        writer.writerow(headers)

        for file in os.listdir(imgdir):
            relative_path = os.path.relpath(file, imgdir)
            absolute_path = os.path.abspath(file)
            writer.writerow([relative_path, absolute_path])

def main():
    arguments = parsing_arguments()
    try:
        download_images(arguments.keyword, arguments.number_of_images, arguments.imgdir)
        create_annotation(arguments.imgdir,arguments.annotation_file)
        my_iterator = ImageIterator(arguments.annotation_file)
        for image in my_iterator:
            print(image)
    except Exception as e:
        print(f"Error: {e} ")
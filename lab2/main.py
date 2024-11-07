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
    def __init__(self, file_with_annotation:str):
        self.images = []
        with open(file_with_annotation, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.images.append(row['Absolute path'])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.images):
            image_path = self.images[self.index]
            self.index += 1
            return image_path
        else:
            raise StopIteration

def create_annotation(imgdir: str, file_with_annotation: str):
    """
    Creates annotation with absolute and relative paths to images
    :param imgdir: Directory with images
    :param file_with_annotation: .csv file for annotation
    """
    with open(file_with_annotation, mode='w', encoding='utf-8') as file_with_annotation:
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
        create_annotation(arguments.imgdir,arguments.file_with_annotation)
        my_iterator = ImageIterator(arguments.file_with_annotation)
        for image in my_iterator :
            print(image)
    except Exception as e:
        print(f"Error: {e} ")

if __name__=="__main__":
    main()
import csv
import os

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
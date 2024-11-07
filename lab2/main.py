import argparse
from iterator import ImageIterator
from downloader import download_images
from annotation import create_annotation

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
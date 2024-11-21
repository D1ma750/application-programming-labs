import cv2
import argparse

from work_with_image import colors_of_histogram, creating_histogram, changing_image_size, show_image


def parsing_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type=str, help="Path to image")
    parser.add_argument("new_image_path", type=str, help="Path to load new image")
    parser.add_argument("height", type=int, help="Height of new image")
    parser.add_argument("width", type=int, help="Width of new image")
    arguments = parser.parse_args()
    return arguments
def main():
    arguments = parsing_arguments()
    try:
        image = cv2.imread(arguments.image_path)
        print(image.shape)
        blue, green, red= colors_of_histogram(image)
        creating_histogram(blue, green, red)
        new_image=changing_image_size(image, arguments.width, arguments.height)
        print(new_image.shape)
        show_image(image, new_image)
        cv2.imwrite(arguments.new_image_path, new_image)

    except Exception as e:
        print(f"Error: {e} ")


if __name__=='__main__':
    main()
import cv2
import matplotlib.pyplot as plt
import numpy as np


def colors_of_histogram(image:np.ndarray)->tuple:
    blue = cv2.calcHist([image], [0], None, [256], [0, 255])
    green = cv2.calcHist([image], [1], None, [256], [0, 255])
    red = cv2.calcHist([image], [2], None, [256], [0, 255])
    return blue,green,red


def creating_histogram(blue:np.ndarray, green:np.ndarray, red:np.ndarray)->None:
    plt.figure(figsize=(10, 5))
    plt.plot( blue, label='Синяя линия', color='blue')
    plt.plot( green, label='Зеленая линия', color='green')
    plt.plot( red, label='Красная линия', color='red')
    plt.xlim([0, 255])
    plt.title('Гистограмма цвета изображения')
    plt.xlabel('Интенсивность цвета')
    plt.ylabel('Частота')
    plt.grid()
    plt.legend()
    plt.show()


def changing_image_size(image:np.ndarray, width:int, height:int)->np.ndarray:
    new_image=cv2.resize(image, (height, width))
    return new_image


def show_image(image:np.ndarray, new_image:np.ndarray)->None:
    cv2.imshow('image', image)
    cv2.imshow('image_with_new_size', new_image)
    cv2.waitKey(0)
import cv2
import pandas as pd
import matplotlib.pyplot as plt


def create_df(path_csv: str) -> pd.DataFrame:
    """
    создание DataFrame
    :param path_csv: путь к annotation file
    :return: DataFrame
    """
    df = pd.read_csv(path_csv)
    return df


def add_hwd_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет столбцы 'Height', 'Width' и 'Depth' в DataFrame,
    используя информацию о размере изображений.

    :param df: Исходный DataFrame, содержащий путь к изображению в колонке 'Relpath'.
    :return: Обновленный DataFrame с новыми столбцами.
    """
    heights, widths, depths = [], [], []
    for abspath in df["Absolute_path"]:
        img = cv2.imread(abspath)
        height, width, depth = img.shape
        heights.append(height)
        widths.append(width)
        depths.append(depth)
    df["Height"] = heights
    df["Width"] = widths
    df["Depth"] = depths
    return df


def filter_columns(df: pd.DataFrame, max_height: int, max_width: int) -> pd.DataFrame:
    """
    Функция фильтрации изображений
    :param df:
    :param max_width: фильтр по ширине
    :param max_height: фильтр по высоте
    :return: Отсортированный DataFrame
    """
    return df[(df['Height'] <= max_height) & (df['Width'] <= max_width)]


def create_column_area(df: pd.DataFrame) -> None:
    """
    Функция добавления столбца area
    :param df: DataFrame
    :return: None
    """
    df['Area'] = df['Height'] * df['Width']


def create_histogram(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    plt.hist(df['Area'], bins=30, edgecolor='black')
    plt.title('Распределение площадей изображений')
    plt.xlabel('Площадь изображения')
    plt.ylabel('Количество изображений')
    plt.grid(True)
    plt.show()


def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by='Area', ascending=False)

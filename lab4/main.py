import argparse

from dataframe import create_df, add_hwd_columns, create_histogram, create_column_area, filter_columns, sort_by_area


def parsing_arguments():
    """
    Reads arguments from terminal
    :return: Arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path_csv", type = str, help="Path to csv file")
    arguments = parser.parse_args()
    return arguments


def main():
    arguments = parsing_arguments()
    try:
        df = create_df(arguments.path_csv)
        print(df.head())
        print('dataframe')
        add_hwd_columns(df)
        print(df.head())
        print('new_columns')
        stats = df[['Height', 'Width', 'Depth']].describe()
        print(stats)
        filtered_df = filter_columns(df, 1000, 1000)
        print(filtered_df.head())
        print('sort data')
        create_column_area(df)
        print(df.head())
        print('area')
        df_sort_by_value = sort_by_area(df)
        print(df_sort_by_value.head())
        print('sort area')
        create_histogram(df)
    except Exception as e:
        print(f"Error: {e} ")


if __name__ == "__main__":
    main()
















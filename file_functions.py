import pandas as pd

def num_formatter(column_name, file):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    # Sets max rows (make a toggle)
    for i in range(0, len(file)):
        # For Every Line in the csv converts string to float then rounds to 2 decimel points
        file.loc[i, column_name] = round(float(file.loc[i, column_name]), 2)

    return file


def file_formatter_from_file(file_name='data.csv', write=False):
    file = pd.read_csv(file_name)
    # loads the file
    for column in file.columns:
        # For every column in the file
        try:
            num_formatter(column_name=column, file=file)
            # call file_formatter
        except ValueError:
            # to stop it from attempting to convert the date
            continue
    if write:
        # if write is passed will write this to data.csv
        file.to_csv('data.csv')
        return file
    else:
        return file


def file_formatter_from_mem(data_pd):
    for column in data_pd.columns:
        print(column)
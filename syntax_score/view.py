import os

import pandas
from PyQt5.QtWidgets import QApplication, QFileDialog


def create_form_1(data_1, file_path):
    df_form1 = pandas.DataFrame.from_dict(data_1)
    df_form1.to_csv(os.path.join(file_path, 'form1.csv'), index=False)


def create_form_2(data_2, file_path):
    df_form2 = pandas.DataFrame.from_dict(data_2)
    df_form2.to_csv(os.path.join(file_path, 'form2.csv'), index=False)


def choose_file():
    app = QApplication([])
    file = QFileDialog.getOpenFileNames(directory='C:/')[0][0]
    return file


if __name__ == '__main__':
    pass

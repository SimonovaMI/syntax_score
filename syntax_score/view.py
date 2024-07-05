import pandas
from PyQt5 import QtCore, QtWidgets


def create_form_1(data_1):
    df_form1 = pandas.DataFrame.from_dict(data_1)
    df_form1.to_csv(r'form1.csv', index=False)


def create_form_2(data_2):
    df_form2 = pandas.DataFrame.from_dict(data_2)
    df_form2.to_csv(r'form2.csv', index=False)


def choose_file():
    app = QtWidgets.QApplication([])
    file = QtWidgets.QFileDialog.getOpenFileNames()[0]
    return file


if __name__ == '__main__':
    pass

import pandas


def get_all_data(file_path):
    data_frame = pandas.read_csv(file_path)
    columns = data_frame.columns.values.tolist()
    filtered_columns = [i for i in columns if 'Укажите номер сегмента в котором начинается окклюзия' in i or
                        'Укажите первый сегмент дистальнее окклюзии визуализируемый антеградным' in i]
    for i in filtered_columns:
        data_frame[i] = data_frame[i].astype('string')
    data_frame['Номер эпизода'] = data_frame['Номер эпизода'].str.upper()
    return data_frame


if __name__ == '__main__':
    pass

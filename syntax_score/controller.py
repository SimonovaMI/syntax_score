import statistics
import model
import view

__coeff__ = 2
__coeff_ocl__ = 5

__zone_left__ = {'1 - проксимальный сегмент ПКА': 0, '2 - средний сегмент ПКА': 0, '3 - дистальный сегмент ПКА': 0,
                 '5 - ствол ЛКА': 6, '6 - проксимальный сегмент ПМЖВ': 3.5, '7 - средний сегмент ПМЖВ': 2.5,
                 '8 - дистальный сегмент ПМЖВ': 1, '9 - первая диагональная артерия': 1,
                 '9a - дополнительная первая диагональная артерия': 1, '10 - вторая диагональная ветвь': 0.5,
                 '10a - дополнительная вторая диагональная артерия': 0.5,
                 '11 - проксимальный сегмент огибающей артерии': 2.5, '12 - промежуточная артерия': 1,
                 '12a - первая ветвь тупого края': 1, '12b - вторая ветвь тупого края': 1,
                 '13 - дистальный сегмент огибающей артерии': 1.5, '14 - задне-боковая ветвь от ОА': 1,
                 '14a - задне-боковая ветвь от ОА': 1, '14b - задне-боковая ветвь от ОА': 1, '15 - ЗМЖВ от ОА': 1}
__zone_right__ = {'1 - проксимальный сегмент ПКА': 1, '2 - средний сегмент ПКА': 1, '3 - дистальный сегмент ПКА': 1,
                  '4- ЗМЖВ от ПКА': 1, '5 - ствол ЛКА': 5, '6 - проксимальный сегмент ПМЖВ': 3.5,
                  '7 - средний сегмент ПМЖВ': 2.5, '8 - дистальный сегмент ПМЖВ': 1,
                  '9 - первая диагональная артерия': 1, '9a - дополнительная первая диагональная артерия': 1,
                  '10 - вторая диагональная ветвь': 0.5,
                  '10a - дополнительная вторая диагональная артерия': 0.5,
                  '11 - проксимальный сегмент огибающей артерии': 1.5, '12 - промежуточная артерия': 1,
                  '12a - первая ветвь тупого края': 1, '12b - вторая ветвь тупого края': 1,
                  '13 - дистальный сегмент огибающей артерии': 0.5, '14 - задне-боковая ветвь от ОА': 0.5,
                  '14a - задне-боковая ветвь от ОА': 0.5, '14b - задне-боковая ветвь от ОА': 0.5,
                  '16 - задне-боковая ветвь от ПКА': 0.5, '16a - задне-боковая ветвь от ПКА': 0.5,
                  '16b- задне-боковая ветвь от ПКА': 0.5, '16c- задне-боковая ветвь от ПКА': 0.5}
__segments__ = {'1 - проксимальный сегмент ПКА': 0, '2 - средний сегмент ПКА': 0, '3 - дистальный сегмент ПКА': 0,
                '4- ЗМЖВ от ПКА': 0, '5 - ствол ЛКА': 0, '6 - проксимальный сегмент ПМЖВ': 0,
                '7 - средний сегмент ПМЖВ': 0, '8 - дистальный сегмент ПМЖВ': 0,
                '9 - первая диагональная артерия': 0, '9a - дополнительная первая диагональная артерия': 0,
                '10 - вторая диагональная ветвь': 0,
                '10a - дополнительная вторая диагональная артерия': 0,
                '11 - проксимальный сегмент огибающей артерии': 0, '12 - промежуточная артерия': 0,
                '12a - первая ветвь тупого края': 0, '12b - вторая ветвь тупого края': 0,
                '13 - дистальный сегмент огибающей артерии': 0, '14 - задне-боковая ветвь от ОА': 0,
                '14a - задне-боковая ветвь от ОА': 0, '14b - задне-боковая ветвь от ОА': 0, '15 - ЗМЖВ от ОА': 0,
                '16 - задне-боковая ветвь от ПКА': 0, '16a - задне-боковая ветвь от ПКА': 0,
                '16b- задне-боковая ветвь от ПКА': 0, '16c- задне-боковая ветвь от ПКА': 0}
__ocl_float__ = {'1.0': '1 - проксимальный сегмент ПКА', '2.0': '2 - средний сегмент ПКА',
                 '3.0': '3 - дистальный сегмент ПКА',
                 '4.0': '4- ЗМЖВ от ПКА', '5.0': '5 - ствол ЛКА', '6.0': '6 - проксимальный сегмент ПМЖВ',
                 '7.0': '7 - средний сегмент ПМЖВ', '8.0': '8 - дистальный сегмент ПМЖВ',
                 '9.0': '9 - первая диагональная артерия', '10.0': '10 - вторая диагональная ветвь',
                 '11.0': '11 - проксимальный сегмент огибающей артерии', '12.0': '12 - промежуточная артерия',
                 '13.0': '13 - дистальный сегмент огибающей артерии', '14.0': '14 - задне-боковая ветвь от ОА',
                 '15.0': '15 - ЗМЖВ от ОА', '16.0': '16 - задне-боковая ветвь от ПКА'}
__ocl_str__ = {'1': '1 - проксимальный сегмент ПКА', '2': '2 - средний сегмент ПКА',
               '3': '3 - дистальный сегмент ПКА',
               '4': '4- ЗМЖВ от ПКА', '5': '5 - ствол ЛКА', '6': '6 - проксимальный сегмент ПМЖВ',
               '7': '7 - средний сегмент ПМЖВ', '8': '8 - дистальный сегмент ПМЖВ',
               '9': '9 - первая диагональная артерия', '9a': '9a - дополнительная первая диагональная артерия',
               '10': '10 - вторая диагональная ветвь',
               '10a': '10a - дополнительная вторая диагональная артерия',
               '11': '11 - проксимальный сегмент огибающей артерии', '12': '12 - промежуточная артерия',
               '12a': '12a - первая ветвь тупого края', '12b': '12b - вторая ветвь тупого края',
               '13': '13 - дистальный сегмент огибающей артерии', '14': '14 - задне-боковая ветвь от ОА',
               '14a': '14a - задне-боковая ветвь от ОА', '14b': '14b - задне-боковая ветвь от ОА',
               '15': '15 - ЗМЖВ от ОА',
               '16': '16 - задне-боковая ветвь от ПКА', '16a': '16a - задне-боковая ветвь от ПКА',
               '16b': '16b- задне-боковая ветвь от ПКА', '16c': '16c- задне-боковая ветвь от ПКА'}
__diff_zone__ = 1
__trifurcation_coeff__ = {'1 сегмент поражен': 3, '2 сегмента поражено': 4, '3 сегмента поражено': 5,
                          '4 сегмента поражено': 6}
__bifurcation_coeff__ = {'1,0,0': 1, '0,1,0': 1, '1,1,0': 1, '1,1,1': 2, '0,0,1': 2, '1,0,1': 2, '0,1,1': 2}

data_1 = []
data_2 = []


class ClinicalCase:
    def __init__(self, case_number, cor_angiography_list):
        self.case_number = case_number
        self.cor_angiography_list = cor_angiography_list

    def get_average_syntax_score(self):
        summ_syntax_score_list = [i.get_summ_syntax_score() for i in self.cor_angiography_list]
        if len(summ_syntax_score_list) != 0:
            return round(statistics.mean(summ_syntax_score_list), 3)
        else:
            return '?'


class CoronaryAngiography:
    def __init__(self, id_research, type_blood_supply, affected_segments):
        self.affected_segments = affected_segments
        self.id_research = id_research
        self.type_blood_supply = type_blood_supply

    def get_summ_syntax_score(self):
        summ = 0
        for i in self.affected_segments.values():
            summ += i.count_syntax_score()
        return summ


class AffectedSegment:
    def __init__(self, segments, occlusion_more_three_month=0, blind_stump=0, pontine_collaterals=0,
                 lateral_branches=0, trifurcation=0, bifurcation=0, pronounced_angulation=0, wellhead_lesion=0,
                 pronounced_tortuosity=0, lession_length=0, calcification=0, thrombosis=0, diffuse_lesions=0):
        self.segments = segments
        self.occlusion_more_three_month = occlusion_more_three_month
        self.blind_stump = blind_stump
        self.pontine_collaterals = pontine_collaterals
        self.lateral_branches = lateral_branches
        self.trifurcation = trifurcation
        self.bifurcation = bifurcation
        self.pronounced_angulation = pronounced_angulation
        self.wellhead_lesion = wellhead_lesion
        self.pronounced_tortuosity = pronounced_tortuosity
        self.lession_length = lession_length
        self.calcification = calcification
        self.thrombosis = thrombosis
        self.diffuse_lesions = diffuse_lesions

    def count_syntax_score(self):
        segment_score = sum(self.segments.values())
        return (segment_score + self.occlusion_more_three_month + self.blind_stump + self.pontine_collaterals +
                self.lateral_branches + self.trifurcation + self.bifurcation + self.pronounced_angulation +
                self.wellhead_lesion + self.pronounced_tortuosity + self.lession_length +
                self.calcification + self.thrombosis + self.diffuse_lesions)


def get_data():
    data_frame = model.get_all_data()
    cases = list(data_frame['Номер эпизода'].unique())
    for case in cases:
        case_data = data_frame[data_frame['Номер эпизода'] == case].to_dict('records')
        created_case = create_case(case_data)
        create_data_1(created_case)
        create_data_2(created_case)
    create_forms()


def create_segment(dec, type_blood_supply):
    without_none = {key: value for key, value in dec.items() if not isinstance(value, float) and value != 'нет' and
                    value is not None}
    segments_with_count = count_segments(without_none, type_blood_supply)
    affected_segment = AffectedSegment(segments_with_count)
    affected_segment.occlusion_more_three_month = count_occlusion_more_three_month(without_none)
    affected_segment.blind_stump = count_blind_stump(without_none)
    affected_segment.pontine_collaterals = count_pontine_collaterals(without_none)
    affected_segment.lateral_branches = count_lateral_branches(without_none)
    affected_segment.trifurcation = count_trifurcation(without_none)
    affected_segment.bifurcation = count_bifurcation(without_none)
    affected_segment.pronounced_angulation = count_pronounced_angulation(without_none)
    affected_segment.wellhead_lesion = count_wellhead_lesion(without_none)
    affected_segment.pronounced_tortuosity = count_pronounced_tortuosity(without_none)
    affected_segment.calcification = count_calcification(without_none)
    affected_segment.thrombosis = count_thrombosis(without_none)
    affected_segment.diffuse_lesions = count_diffuse_lesions(without_none)

    return affected_segment


def count_diffuse_lesions(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Выберите сегмент(ы) с диффузным поражением' in key:
            result += 1
    return result


def count_thrombosis(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Наличие пристеночного тромбоза?' in key:
            result += 1
    return result


def count_calcification(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Выраженный кальциноз?' in key:
            result += 2
    return result


def count_lession_length(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Длина поражения >20 мм?' in key:
            result += 1
    return result


def count_pronounced_tortuosity(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Выраженная извитость?' in key:
            result += 2
    return result


def count_wellhead_lesion(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Аорто-устьевое поражение?' in key:
            result += 1
    return result


def count_pronounced_angulation(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Острый угол бифуркации?' in key:
            result += 1
    return result


def count_bifurcation(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Тип бифуркационного поражения по Медина' in key:
            result += __bifurcation_coeff__[value]
    return result


def count_trifurcation(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Сколько сегментов поражены?' in key:
            result += __trifurcation_coeff__[value]
    return result


def count_lateral_branches(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Если ли боковые ветви в начале окклюзии?' in key:
            result += 1
    return result


def count_pontine_collaterals(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Имеются ли "мостовые" коллатерали?' in key:
            result += 1
    return result


def count_blind_stump(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Проксимальная культя окклюзии слепая?' in key:
            result += 1
    return result


def count_occlusion_more_three_month(without_none):
    result = 0
    for key, value in without_none.items():
        if 'Окклюзия наблюдается больше 3 месяцев?' in key:
            result += 1
    return result


def count_segments(without_none, type_blood_supply):
    segments = __segments__.copy()
    zone = {'Левый': __zone_left__, 'Правый': __zone_right__}
    for key, value in without_none.items():
        for i in segments.keys():
            if i in key:
                segments[i] = zone[type_blood_supply][i] * __coeff__
        if 'Укажите номер сегмента в котором начинается окклюзия' in key:
            float_key = __ocl_float__.get(value)
            str_key = __ocl_str__.get(value)
            if float_key:
                segments[float_key] = zone[type_blood_supply][float_key] * __coeff_ocl__
            else:
                if str_key:
                    segments[str_key] = zone[type_blood_supply][str_key] * __coeff_ocl__

    return segments


def create_case(case_data):
    coronary_angiographies = []
    for dec in case_data:
        affected_segments = {}

        if dec['Коронарные артерии без ангиографически значимых поражений?'] == 'да':
            for i in range(0, 9):
                affected_segments[i] = AffectedSegment({})
            coronary_angiographies.append(CoronaryAngiography(dec['ID'], dec['Тип кровоснабжения'], affected_segments))
        else:
            if dec['Все поражения указаны?'] == 'Да':
                for i in range(0, 9):
                    number_segment = '[' + str(i + 1) + ']'
                    dec_segment = {key: value for key, value in dec.items() if number_segment in key}
                    affected_segments[i] = create_segment(dec_segment, dec['Тип кровоснабжения'])

            coronary_angiographies.append(CoronaryAngiography(dec['ID'], dec['Тип кровоснабжения'], affected_segments))

    return ClinicalCase(case_data[0]['Номер эпизода'], coronary_angiographies)


def create_data_1(created_case):
    for i in created_case.cor_angiography_list:
        try:
            data_1.append({'Номер эпизода': created_case.case_number, 'ID': i.id_research,
                           'Тип кровоснабжения': i.type_blood_supply,
                           '[1]': i.affected_segments[0].count_syntax_score(),
                           '[2]': i.affected_segments[1].count_syntax_score(),
                           '[3]': i.affected_segments[2].count_syntax_score(),
                           '[4]': i.affected_segments[3].count_syntax_score(),
                           '[5]': i.affected_segments[4].count_syntax_score(),
                           '[6]': i.affected_segments[5].count_syntax_score(),
                           '[7]': i.affected_segments[6].count_syntax_score(),
                           '[8]': i.affected_segments[7].count_syntax_score(),
                           '[9]': i.affected_segments[8].count_syntax_score(),
                           'Сумма по всем поражениям': i.get_summ_syntax_score()})
        except KeyError:
            data_1.append({'Номер эпизода': created_case.case_number, 'ID': i.id_research,
                           'Тип кровоснабжения': i.type_blood_supply,
                           '[1]': -1, '[2]': -1, '[3]': -1, '[4]': -1, '[5]': -1, '[6]': -1, '[7]': -1,
                           '[8]': -1,
                           '[9]': -1,
                           'Сумма по всем поражениям': -1})


def create_data_2(created_case):
    data_2.append({'Номер эпизода': created_case.case_number,
                   'Среднее зачение': created_case.get_average_syntax_score()})


def create_forms():
    view.create_form_1(data_1)
    view.create_form_2(data_2)


if __name__ == '__main__':
    get_data()

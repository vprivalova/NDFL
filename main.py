"""
Khludina Ksenia
Nizovtseva Anastasia
Privalova Viktoria
Fedotova Tatiana
"""

yes = ['да', 'Да', 'ДА', 'yes', 'Yes', 'YES']
no = ['нет', 'НЕТ', 'Нет', 'No', 'NO', 'no']

income = input('Введите налоговую базу: ')
q1_residents = input('Вы являетесь налоговым резидентом РФ?')

if q1_residents in yes:
    # тут весь код Насти и Ксюши
    q2_incomeinRF = input('Вы получаете доход на территории РФ?')

    if q2_incomeinRF in yes:
        pass

    else:
        pass

else:
    pass
    # тут весь код Вики
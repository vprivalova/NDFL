"""
Khludina Ksenia
Nizovtseva Anastasia
Privalova Viktoria
Fedotova Tatiana
"""

import ru_local as ru


yes = ['да', 'Да', 'ДА', 'yes', 'Yes', 'YES']
no = ['нет', 'НЕТ', 'Нет', 'No', 'NO', 'no']

overall_tax = 0
q1_residents = input('Вы являетесь налоговым резидентом РФ? ')

if q1_residents in yes:
    # тут весь код Насти и Ксюши
    q2_incomeRF = input('Вы получаете доход на территории РФ? ')

    if q2_incomeRF in yes:
        pass

    else:
        pass

else:
    # тут весь код Вики
    q2_incomeRF = input('Вы получаете доход на территории РФ? ')

    if q2_incomeRF in yes:
        q17_dividends = input('Вы получаете доход в виде дивидендов от долевого участия в деятельности российских '
                              'организаций и выплат, не связанных с выкупом цифровых финансовых активов? ')

        if q17_dividends in yes:
            income_dividends = int(input('Введите сумму данного вида дохода: '))
            tax_dividends = income_dividends * 0.15
            overall_tax = overall_tax + tax_dividends
        else:
            pass

        q18_labour = input(ru.LABOUR)
        if q18_labour in yes:
            income_labour = int(input('Введите сумму данного вида дохода: '))

            if income_labour <= 5000000:
                tax_labour = income_labour * 0.13
                overall_tax = overall_tax + tax_labour
            else:
                tax_labour = income_labour * 0.15
                overall_tax = overall_tax + tax_labour + 650000
        else:
            pass

        q19_deposit = input('Вы получали доход в виде процентов по вкладам (остаткам на счетах) /'
                            'в банках, находящихся на территории Российской Федерации? ')
        if q19_deposit in yes:
            income_deposit = int(input('Введите сумму данного вида дохода: '))

            if income_deposit <= 5000000:
                tax_deposit = income_deposit * 0.13
                overall_tax = overall_tax + tax_deposit
            else:
                tax_deposit = income_deposit * 0.15
                overall_tax = overall_tax + tax_deposit + 650000
        else:
            pass

        q20_otherinc = input('У вас есть иные доходы на территории РФ? ')
        if q20_otherinc in yes:
            income_otherinc = int(input('Введите сумму данного вида дохода: '))
            tax_otherinc = income_otherinc * 0.30
            overall_tax = overall_tax + tax_otherinc
        else:
            pass

    else:
        overall_tax = 0

print('Общая сумма налога, которую вам необходимо заплатить: ', overall_tax)
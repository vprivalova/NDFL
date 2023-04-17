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
q1_residents = input('Вы являетесь налоговым резидентом РФ? \n')

if q1_residents in yes:

    q2_incomeRF = input('Вы получаете доход на территории РФ? \n')
    if q2_incomeRF in yes:

        q3_disability = input('Ваш доход является пособием по временной нетрудоспособности? \n')
        if q3_disability in yes:
            tax = 0.13
            income_disability = int(input('Введите сумму данного вида дохода (в рублях): \n'))
            tax_disability = income_disability * tax
            overall_tax += tax_disability
        else:
            pass

        q4_award = input('Ваш доход получен путём вознаграждения, выплачиваемого наследникам (правопреемникам) авторов произведений науки, литературы, искусства, а также вознаграждения, выплачиваемого наследникам патентообладателей изобретений, полезных моделей, промышленных образцов? \n')
        if q4_award in yes:
            tax = 0.13
            income_award = int(input('Введите сумму данного вида дохода (в рублях): \n'))
            tax_award = income_award * tax
            overall_tax += tax_award
        else:
            pass

        q5_donation = input('Ваш доход получен путём дарения недвижимого имущества, транспортных средств, акций, цифровых финансовых активов, цифровых прав, включающих одновременно цифровые финансовые активы и утилитарные цифровые права, долей, паев? \n')
        if q5_donation in yes:
            tax = 0.13
            income_donation = int(input('Введите сумму данного вида дохода (в рублях): \n'))
            tax_donation = income_donation * tax
            overall_tax += tax_donation
        else:
            pass

        q6_cases1 = input(ru.CASES1)
        if q6_cases1 in yes:
            tax = 0.09
            income_cases1 = int(input('Введите сумму данного вида дохода (в рублях): \n'))
            tax_cases = income_cases1 * tax
            overall_tax += tax_cases
        else:
            pass

        q7_cases2 = input(ru.CASES2)
        if q7_cases2 in yes:
            tax = 0.35
            income_cases2 = int(input('Введите сумму данного вида дохода (в рублях): \n'))
            tax_cases2 = income_cases2 * tax
            overall_tax += tax_cases2
        else:
            pass

        q8_winner = input('Ваш доход был получен с выигрыша до 15 тыс. рублей, выплачиваемого операторами лотерей, распространителями, организаторами азартных игр, проводимых в букмекерской конторе и тотализаторе? \n')
        if q8_winner in yes:
            tax = 0.13
            income_winner = int(input('Введите сумму данного вида дохода (в рублях): \n'))
            tax_winner = income_winner * tax
            overall_tax += tax_winner
        else:
            pass

        q9_cases3 = input(ru.CASES3)
        if q9_cases3 in yes:
            income_cases3 = int(input('Введите сумму данного вида дохода (в рублях): \n'))
            if income_cases3 <= 5000000:
                tax = 0.13
                tax_cases3 = income_cases3 * tax
                overall_tax += tax_cases3
            else:
                tax = 0.15
                tax_cases3 = income_cases3 * tax
                overall_tax = overall_tax + tax_cases3 + 650000
        else:
            pass


else:
    q2_incomeRF = input('Вы получаете доход на территории РФ? \n')

    if q2_incomeRF in yes:
        q10_dividends = input('Вы получаете доход в виде дивидендов от долевого участия в деятельности российских организаций и выплат, не связанных с выкупом цифровых финансовых активов? \n')

        if q10_dividends in yes:
            tax = 0.15
            income_dividends = int(input('Введите сумму данного вида дохода (в рублях): \n'))
            tax_dividends = income_dividends * tax
            overall_tax += tax_dividends
        else:
            pass

        q11_labour = input(ru.LABOUR)
        if q11_labour in yes:
            income_labour = int(input('Введите сумму данного вида дохода (в рублях): \n'))

            if income_labour <= 5000000:
                tax = 0.13
                tax_labour = income_labour * tax
                overall_tax += tax_labour
            else:
                tax = 0.15
                tax_labour = income_labour * tax
                overall_tax = overall_tax + tax_labour + 650000
        else:
            pass

        q12_deposit = input('Вы получали доход в виде процентов по вкладам (остаткам на счетах) в банках, находящихся на территории Российской Федерации? \n')
        if q12_deposit in yes:
            income_deposit = int(input('Введите сумму данного вида дохода (в рублях): \n'))

            if income_deposit <= 5000000:
                tax = 0.13
                tax_deposit = income_deposit * tax
                overall_tax += tax_deposit
            else:
                tax = 0.15
                tax_deposit = income_deposit * tax
                overall_tax = overall_tax + tax_deposit + 650000
        else:
            pass

        q13_other = input('У вас есть иные доходы на территории РФ? \n')
        if q13_other in yes:
            tax = 0.30
            income_other = int(input('Введите сумму данного вида дохода (в рублях): \n'))
            tax_other = income_other * tax
            overall_tax += tax_other
        else:
            pass

    else:
        overall_tax = 0

print('Общая сумма налога, которую вам необходимо заплатить: ', overall_tax)
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
    boolflag = 0
    q2_incomeRF = input('Вы получаете доход на территории РФ? \n')
    if q2_incomeRF in yes:
        income_cases1 = ' * государственные пособия \n * пенсии по государственному пенсионному обеспечению, страховые пенсии, фиксированная выплата к страховой пенсии, накопительная пенсия, социальные доплаты к пенсиям \n * доход с алиментов, получаемых налогоплательщиками \n * ежемесячная выплата (материнский капитал) в связи с рождением (усыновлением) первого и (или) второго ребенка \n * адресная социальная помощь за счет средств федерального бюджета, бюджетов субъектов Российской Федерации, местных бюджетов и внебюджетных фондов \n * суммы, уплаченные работодателями за оказание медицинских услуг своим работникам, их родственникам, а также бывшим работникам-пенсионерам \n * стипендии студентов, аспирантов, ординаторов и ассистентов-стажеров организаций, осуществляющих образовательную деятельность по основным профессиональным образовательным программам, а также стипендиаты с именными стипендиями, президентскими и правительственными \n * доходы, получаемые от продажи выращенной в личных подсобных хозяйствах, находящихся на территории Российской Федерации, продукции животноводства (как в живом виде, так и продуктов убоя в сыром или переработанном виде), продукции растениеводства (как в натуральном, так и в переработанном виде) при соблюдении определенных условий \n * доходы, получаемые за соответствующий налоговый период от продажи объектов недвижимого имущества, а также долей в указанном имуществе с учетом особенностей, а также от продажи иного имущества в собственности налогоплательщика три года и более \n * доходы в денежной и натуральной формах, получаемые от физических лиц в порядке дарения \n * доходы в денежной и натуральной формах, получаемые от физических лиц в порядке наследования \n * благотворительная помощь детям-сиротам и оставшимися без попечения родителей, а также несовершеннолетним членам семей, доходы которых на одного члена не превышают прожиточного минимума \n * доход, являющийся стоимостью подарков, полученных от организаций или индивидуальных предпринимателей стоимостью не более 4000 руб. \n'
        print('Ваш доход относится к одному из представленных случаев? \n')
        q3_incomeCases = input(income_cases1)
        tax = 0
        if q3_incomeCases in yes:
            q4_stipend = input('Ваш доход является пособием по временной нетрудоспособности? \n')
            if q4_stipend in yes:
                tax = 0.13
            else:
                q5_award = input('Ваш доход получен путём вознаграждения, выплачиваемого наследникам (правопреемникам) авторов произведений науки, литературы, искусства, а также вознаграждения, выплачиваемого наследникам патентообладателей изобретений, полезных моделей, промышленных образцов? \n')
                if q5_award in yes:
                    tax = 0.13
                else:
                    q6_incomeFromFamily = input('Ваш доход был получен от члена семьи и (или) близкого родственника в соответствии с Семейным кодексом РФ? \n')
                    if q6_incomeFromFamily in yes:
                        tax = 0
                    else:
                        q7 = input('Ваш доход получен путём дарения недвижимого имущества, транспортных средств, акций, цифровых финансовых активов, цифровых прав, включающих одновременно цифровые финансовые активы и утилитарные цифровые права, долей, паев? \n')
                        if q7 in yes:
                            tax = 0.13
                        else:
                            tax = 0
    else:
        income_cases2 = ' * получение дивидендов до 2015 года \n * получение процентов по облигациям с ипотечным покрытием, эмитированным до 1 января 2007 г. \n * получение доходов учредителями доверительного управления ипотечным покрытием. Получены на основании приобретения ипотечных сертификатов участия, выданных управляющим ипотечным покрытием до 1 января 2007 г. \n '
        print('Ваш доход относится к одному из представленных случаев? \n')
        q8_incomeCases2 = input(income_cases2)
        tax = 0
        if q8_incomeCases2 in yes:
            tax = 0.09
        else:
            income_cases3 = ' * стоимость любых выигрышей и призов, получаемых в проводимых конкурсах, играх и других мероприятиях в целях рекламы товаров, работ и услуг \n * процентные доходы по вкладам в банках в части превышения установленных размеров \n * сумма экономии на процентах при получении заемных (кредитных) средств в части превышения установленных размеров \n * плата за использование денежных средств членов кредитного потребительского кооператива (пайщиков), а также процентов за использование сельскохозяйственным кредитным потребительским кооперативом средств, привлекаемых в форме займов от членов сельскохозяйственного кредитного потребительского кооператива или ассоциированных членов сельскохозяйственного кредитного потребительского кооператива, в части превышения установленных размеров. \n'
            print('Ваш доход относится к одному из представленных случаев? \n')
            q9_incomeCases3 = input(income_cases3)
            tax = 0
            if q9_incomeCases3 in yes:
                q10_winner = input('Ваш доход был получен с выигрыша до 15 тыс. рублей, выплачиваемого операторами лотерей, распространителями, организаторами азартных игр, проводимых в букмекерской конторе и тотализаторе? \n')
                if q10_winner in yes:
                    tax = 0.13
                else:
                    tax = 0.35
            else:
                q11_income5mln = input('Размер Вашего дохода превышает превышает сумму 5 миллионов рублей? \n')
                if q11_income5mln in yes:
                    print('Ваш доход получен: \n')
                    incomeCases4 = ' * в качестве оплаты по трудовому или гражданско-правовому договору с организацией, не являющейся налоговым агентом. В том числе по договору найма или аренды любого имущества \n * от продажи имущества, находящегося в собственности \n * в качестве вознаграждения по гражданско-правовым договорам \n * премия в рамках трудовых отношений \n * от страховых выплат по договорам страхования и выплат \n'
                    q11_income5mln = input(incomeCases4)
                    if q11_income5mln in yes:
                        tax = 0.15
                        boolflag = 1
                else:
                        tax = 0.13
    ans = input('Вам назвать только процент налога? \n')
    if ans in yes:
        print('Размер дохода для уплаты: в процентах', tax*100)
    else:
        ans = int(input('Введите сумму дохода в рублях: '))
        if boolflag == 0:
            print('Размер дохода для уплаты в рублях: ', tax * ans)
        else:
            print('Размер дохода для уплаты в рублях: ', tax * ans + 650000)




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
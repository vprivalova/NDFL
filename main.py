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
q1_residents = input(ru.Q1_RESIDENTS_TEXT)

if q1_residents in yes:

    q2_incomeRF = input(ru.Q2_INCOMERF_TEXT)
    if q2_incomeRF in yes:

        q3_disability = input(ru.Q3_DISABILITY_TEXT)
        if q3_disability in yes:
            tax = 0.13
            income_disability = float(input(ru.INCOME_DISABILITY_TEXT))
            tax_disability = income_disability * tax
            overall_tax += tax_disability
        else:
            pass

        q4_award = input(ru.Q4_AWARD_TEXT)
        if q4_award in yes:
            tax = 0.13
            income_award = float(input(ru.INCOME_AWARD_TEXT))
            tax_award = income_award * tax
            overall_tax += tax_award
        else:
            pass

        q5_donation = input(ru.Q5_DONATION_TEXT)
        if q5_donation in yes:
            tax = 0.13
            income_donation = float(input(ru.INCOME_DONATION_TEXT))
            tax_donation = income_donation * tax
            overall_tax += tax_donation
        else:
            pass

        q6_cases1 = input(ru.CASES1)
        if q6_cases1 in yes:
            tax = 0.09
            income_cases1 = float(input(ru.INCOME_CASES1_TEXT))
            tax_cases = income_cases1 * tax
            overall_tax += tax_cases
        else:
            pass

        q7_cases2 = input(ru.CASES2)
        if q7_cases2 in yes:
            tax = 0.35
            income_cases2 = float(input(ru.INCOME_CASES2_TEXT))
            tax_cases2 = income_cases2 * tax
            overall_tax += tax_cases2
        else:
            pass

        q8_winner = input(ru.Q8_WINNER_TEXT)
        if q8_winner in yes:
            tax = 0.13
            income_winner = float(input(ru.INCOME_WINNER_TEXT))
            tax_winner = income_winner * tax
            overall_tax += tax_winner
        else:
            pass

        q9_cases3 = input(ru.CASES3)
        if q9_cases3 in yes:
            income_cases3 = float(input(ru.INCOME_CASES3_TEXT))
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
    q2_incomeRF = input(ru.Q2_INCOMERF_TEXT)

    if q2_incomeRF in yes:
        q10_dividends = input(ru.Q10_DIVIDENDS_TEXT)
        if q10_dividends in yes:
            tax = 0.15
            income_dividends = float(input(ru.INCOME_DIVIDENDS_TEXT))
            tax_dividends = income_dividends * tax
            overall_tax += tax_dividends
        else:
            pass

        q11_labour = input(ru.LABOUR)
        if q11_labour in yes:
            income_labour = float(input(ru.INCOME_LABOUR_TEXT))

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

        q12_deposit = input(ru.Q12_DEPOSIT_TEXT)
        if q12_deposit in yes:
            income_deposit = float(input(ru.INCOME_DEPOSIT_TEXT))

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

        q13_other = input(ru.Q13_OTHER_TEXT)
        if q13_other in yes:
            tax = 0.30
            income_other = float(input(ru.INCOME_OTHER_TEXT))
            tax_other = income_other * tax
            overall_tax += tax_other
        else:
            pass

    else:
        overall_tax = 0

print(ru.TOTAL_TEXT, overall_tax)
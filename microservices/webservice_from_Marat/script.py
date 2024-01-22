# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.relativedelta import *

import math
import sys


def get_score(kwargs):
    '''
    Скрипт скоринга обернутый в функцию
    '''

    try:
        a1 = int(kwargs.get('a1'))
    except:
        a1 = None

    # a2 = input('DateOfBirth : ')
    try:
        a2 = datetime.strptime(kwargs.get('a2'), '%Y-%m-%d %H:%M:%S.%f')
    except:
        a2 = None

    # a3 = input('MaritalStatus : ')
    try:
        a3 = int(kwargs.get('a3'))
    except:
        a3 = None

    # a4 = input('Education : ')
    try:
        a4 = int(kwargs.get('a4'))
    except:
        a4 = None

    a5 = kwargs.get('a5')

    a6 = kwargs.get('a6')

    a7 = kwargs.get('a7')

    # a8 = input('OrganizationType : ')
    try:
        a8 = int(kwargs.get('a8'))
    except:
        a8 = None

    # a9 = input('ChildrenCount : ')
    try:
        a9 = int(kwargs.get('a9'))
    except:
        a9 = None

    # a10 = input('Period : ')
    try:
        a10 = int(kwargs.get('a10'))
    except:
        a10 = None

    # a11 = input('MaxLoanAmount : ')
    try:
        a11 = int(kwargs.get('a11'))
    except:
        a11 = None

    # a12 = input('PrevKompLoan : ')
    try:
        a12 = int(kwargs.get('a12'))
    except:
        a12 = None

    # a13 = input('ActiveNonKompLoan : ')
    try:
        a13 = int(kwargs.get('a13'))
    except:
        a13 = None

    # a14 = input('ActiveNonKompLoanSum : ')
    try:
        a14 = int(kwargs.get('a14'))
    except:
        a14 = None

    # a15 = input('PrevNonKompLoan : ')
    try:
        a15 = int(kwargs.get('a15'))
    except:
        a15 = None

    # a16 = input('Number_Add_Loans : ')
    try:
        a16 = int(kwargs.get('a16'))
    except:
        a16 = None

    # a17 = input('Worst_Max_overdue : ')
    try:
        a17 = int(kwargs.get('a17'))
    except:
        a17 = None

    # a18 = input('Worst_Sum_overdue : ')
    try:
        a18 = int(kwargs.get('a18'))
    except:
        a18 = None

    # a19 = input('TotalAdditionalIncome : ')
    try:
        a19 = int(kwargs.get('a19'))
    except:
        a19 = None

    # a20 = input('AverageSalary : ')
    try:
        a20 = float(kwargs.get('a20'))
    except:
        a20 = None

    try:
        a21 = kwargs.get('a21')
    except:
        a21 = False

    # a22 = input('OwnershipResidence : ')
    try:
        a22 = int(kwargs.get('a22'))
    except:
        a22 = None

    # a23 = input('MaxInstallment : ')
    try:
        a23 = float(kwargs.get('a23'))
    except:
        a23 = None

    # a24 = input('ActiveKompInstallment : ')
    try:
        komp_inst = float(kwargs.get('a24'))
    except:
        komp_inst = 0

    # a25 = input('ActiveNonKompInstallment : ')
    try:
        nonkomp_inst = float(kwargs.get('a25'))
    except:
        nonkomp_inst = 0

    a26 = kwargs.get('a26')

    # a27 = input('Amount : ')
    try:
        a27 = int(kwargs.get('a27'))
    except:
        a27 = None

    # a28 = input('CreatedDateTime : ')
    try:
        a28 = datetime.strptime(kwargs.get('a28'), '%Y-%m-%d %H:%M:%S.%f')
    except:
        a28 = None

    factregion = 'не определён'
    # Блок подготовки данных
    if a5:
        a5 = a5.lower()
        a5 = a5.replace('ң', 'н')
        a5 = a5.replace('ү', 'у')
        a5 = a5.replace('ө', 'о')
        if 'бишк' in a5:
            factregion = 'Бишкек'
        elif 'талас' in a5 or 'бакайат' in a5 or 'бакай ат' in a5 or 'бакай-ат' in a5 or 'карабу' in a5 or 'кара бу' in a5 or 'кара-бу' in a5 or 'манас' in a5 or 'маймак' in a5 or 'шекер' in a5:
            factregion = 'Талас'
        elif 'батке' in a5 or 'кадамжай' in a5 or 'лейлек' in a5 or 'кызылки' in a5 or 'кызылкы' in a5 or 'кызыл ки' in a5 or 'кызыл кы' in a5 or 'кызыл-ки' in a5 or 'кызыл-кы' in a5 or 'сулюкт' in a5 or 'сулукт' in a5 or 'сюлюкт' in a5 or 'сюлукт' in a5 or 'исфан' in a5:
            factregion = 'Баткен'
        elif 'жалал' in a5 or 'майлу' in a5 or 'ташкум' in a5 or 'ташком' in a5 or 'таш кум' in a5 or 'таш ком' in a5 or 'таш-кум' in a5 or 'таш-ком' in a5 or 'токтогул' in a5 or 'аксы' in a5 or 'ноокен' in a5 or 'каракул' in a5 or 'кара кул' in a5 or 'кара-кул' in a5 or 'кербен' in a5 or 'алабук' in a5 or 'ала бук' in a5 or 'ала-бук' in a5 or 'базаркоргон' in a5 or 'базар коргон' in a5 or 'базар-коргон' in a5 or 'масы' in a5 or 'массы' in a5 or 'сузак' in a5 or 'тогузтор' in a5 or 'тогуз тор' in a5 or 'тогуз-тор' in a5 or 'чаткал' in a5 or 'канышк' in a5 or 'учтерек' in a5 or 'уч терек' in a5 or 'уч-терек' in a5 or 'кокжангак' in a5 or 'кокянгак' in a5 or 'кок жангак' in a5 or 'кок янгак' in a5 or 'кок-жангак' in a5 or 'кок-янгак' in a5 or 'кетментуб' in a5 or 'кетментоб' in a5 or 'кетментеб' in a5 or 'кетментёб' in a5 or 'кетменьтуб' in a5 or 'кетменьтоб' in a5 or 'кетменьтеб' in a5 or 'кетменьтёб' in a5 or 'кетмен туб' in a5 or 'кетмен тоб' in a5 or 'кетмен теб' in a5 or 'кетмен тёб' in a5 or 'кетмень туб' in a5 or 'кетмень тоб' in a5 or 'кетмень теб' in a5 or 'кетмень тёб' in a5 or 'кетмен-туб' in a5 or 'кетмен-тоб' in a5 or 'кетмен-теб' in a5 or 'кетмен-тёб' in a5 or 'кетмень-туб' in a5 or 'кетмень-тоб' in a5 or 'кетмень-теб' in a5 or 'кетмень-тёб' in a5:
            factregion = 'Джалал-Абад'
        elif 'чуй' in a5 or 'токм' in a5 or 'карабалт' in a5 or 'кара балт' in a5 or 'кара-балт' in a5 or 'кемин' in a5 or 'аламед' in a5 or 'аламуд' in a5 or 'ала мед' in a5 or 'ала муд' in a5 or 'ала-мед' in a5 or 'ала-муд' in a5 or 'жайыл' in a5 or 'ысыкат' in a5 or 'ыссыкат' in a5 or 'исыкат' in a5 or 'иссыкат' in a5 or 'ысык ат' in a5 or 'ыссык ат' in a5 or 'исык ат' in a5 or 'иссык ат' in a5 or 'ысык-ат' in a5 or 'ыссык-ат' in a5 or 'исык-ат' in a5 or 'иссык-ат' in a5 or 'москов' in a5 or 'панфилов' in a5 or 'кант' in a5 or 'сокулук' in a5 or 'шопоков' in a5 or 'беловод' in a5:
            factregion = 'Чуй'
        elif 'иссыкк' in a5 or 'исыкк' in a5 or 'ыссыкк' in a5 or 'ысыкк' in a5 or 'иссык к' in a5 or 'исык к' in a5 or 'ыссык к' in a5 or 'ысык к' in a5 or 'иссык-к' in a5 or 'исык-к' in a5 or 'ыссык-к' in a5 or 'ысык-к' in a5 or 'иссыку' in a5 or 'исыку' in a5 or 'ыссыку' in a5 or 'ысыку' in a5 or 'иссыко' in a5 or 'исыко' in a5 or 'ыссыко' in a5 or 'ысыко' in a5 or 'каракол' in a5 or 'балыкч' in a5 or 'чолпонат' in a5 or 'чолпон ат' in a5 or 'чолпон-ат' in a5 or 'барск' in a5 or 'тюп' in a5 or 'тон' in a5 or 'жетиог' in a5 or 'жетыог' in a5 or 'жети ог' in a5 or 'жеты ог' in a5 or 'жети-ог' in a5 or 'жеты-ог' in a5 or 'боконба' in a5 or 'тюп' in a5 or 'тон' in a5 or 'теплокл' in a5 or 'ак су' in a5 or 'аксу' in a5 or 'ак-су' in a5:
            factregion = 'Иссык-Куль'
        elif 'нарын' in a5 or 'баетов' in a5 or 'жумгал' in a5 or 'актал' in a5 or 'ак тал' in a5 or 'ак-тал' in a5 or 'чаек' in a5 or 'атбаш' in a5 or 'ат баш' in a5 or 'ат-баш' in a5 or 'кочкор' in a5:
            factregion = 'Нарын'
        elif 'ош' in a5 or 'карасу' in a5 or 'кара су' in a5 or 'кара-су' in a5 or 'ноокат' in a5 or 'алай' in a5 or 'араван' in a5 or 'узген' in a5 or 'озгон' in a5 or 'каракулж' in a5 or 'каракулдж' in a5 or 'каракульж' in a5 or 'каракульдж' in a5 or 'кара кулж' in a5 or 'кара кулдж' in a5 or 'кара кульж' in a5 or 'кара кульдж' in a5 or 'кара-кулж' in a5 or 'кара-кулдж' in a5 or 'кара-кульж' in a5 or 'кара-кульдж' in a5 or 'шарк' in a5 or 'гулч' in a5 or 'гульч' in a5:
            factregion = 'Ош'

    residenceregion = 'не определён'
    if a6:
        a6 = a6.lower()
        a6 = a6.replace('ң', 'н')
        a6 = a6.replace('ү', 'у')
        a6 = a6.replace('ө', 'о')
        if 'бишк' in a6:
            residenceregion = 'Бишкек'
        elif 'талас' in a6 or 'бакайат' in a6 or 'бакай ат' in a6 or 'бакай-ат' in a6 or 'карабу' in a6 or 'кара бу' in a6 or 'кара-бу' in a6 or 'манас' in a6 or 'маймак' in a6 or 'шекер' in a6:
            residenceregion = 'Талас'
        elif 'батке' in a6 or 'кадамжай' in a6 or 'лейлек' in a6 or 'кызылки' in a6 or 'кызылкы' in a6 or 'кызыл ки' in a6 or 'кызыл кы' in a6 or 'кызыл-ки' in a6 or 'кызыл-кы' in a6 or 'сулюкт' in a6 or 'сулукт' in a6 or 'сюлюкт' in a6 or 'сюлукт' in a6 or 'исфан' in a6:
            residenceregion = 'Баткен'
        elif 'жалал' in a6 or 'майлу' in a6 or 'ташкум' in a6 or 'ташком' in a6 or 'таш кум' in a6 or 'таш ком' in a6 or 'таш-кум' in a6 or 'таш-ком' in a6 or 'токтогул' in a6 or 'аксы' in a6 or 'ноокен' in a6 or 'каракул' in a6 or 'кара кул' in a6 or 'кара-кул' in a6 or 'кербен' in a6 or 'алабук' in a6 or 'ала бук' in a6 or 'ала-бук' in a6 or 'базаркоргон' in a6 or 'базар коргон' in a6 or 'базар-коргон' in a6 or 'масы' in a6 or 'массы' in a6 or 'сузак' in a6 or 'тогузтор' in a6 or 'тогуз тор' in a6 or 'тогуз-тор' in a6 or 'чаткал' in a6 or 'канышк' in a6 or 'учтерек' in a6 or 'уч терек' in a6 or 'уч-терек' in a6 or 'кокжангак' in a6 or 'кокянгак' in a6 or 'кок жангак' in a6 or 'кок янгак' in a6 or 'кок-жангак' in a6 or 'кок-янгак' in a6 or 'кетментуб' in a6 or 'кетментоб' in a6 or 'кетментеб' in a6 or 'кетментёб' in a6 or 'кетменьтуб' in a6 or 'кетменьтоб' in a6 or 'кетменьтеб' in a6 or 'кетменьтёб' in a6 or 'кетмен туб' in a6 or 'кетмен тоб' in a6 or 'кетмен теб' in a6 or 'кетмен тёб' in a6 or 'кетмень туб' in a6 or 'кетмень тоб' in a6 or 'кетмень теб' in a6 or 'кетмень тёб' in a6 or 'кетмен-туб' in a6 or 'кетмен-тоб' in a6 or 'кетмен-теб' in a6 or 'кетмен-тёб' in a6 or 'кетмень-туб' in a6 or 'кетмень-тоб' in a6 or 'кетмень-теб' in a6 or 'кетмень-тёб' in a6:
            residenceregion = 'Джалал-Абад'
        elif 'чуй' in a6 or 'токм' in a6 or 'карабалт' in a6 or 'кара балт' in a6 or 'кара-балт' in a6 or 'кемин' in a6 or 'аламед' in a6 or 'аламуд' in a6 or 'ала мед' in a6 or 'ала муд' in a6 or 'ала-мед' in a6 or 'ала-муд' in a6 or 'жайыл' in a6 or 'ысыкат' in a6 or 'ыссыкат' in a6 or 'исыкат' in a6 or 'иссыкат' in a6 or 'ысык ат' in a6 or 'ыссык ат' in a6 or 'исык ат' in a6 or 'иссык ат' in a6 or 'ысык-ат' in a6 or 'ыссык-ат' in a6 or 'исык-ат' in a6 or 'иссык-ат' in a6 or 'москов' in a6 or 'панфилов' in a6 or 'кант' in a6 or 'сокулук' in a6 or 'шопоков' in a6 or 'беловод' in a6:
            residenceregion = 'Чуй'
        elif 'иссыкк' in a6 or 'исыкк' in a6 or 'ыссыкк' in a6 or 'ысыкк' in a6 or 'иссык к' in a6 or 'исык к' in a6 or 'ыссык к' in a6 or 'ысык к' in a6 or 'иссык-к' in a6 or 'исык-к' in a6 or 'ыссык-к' in a6 or 'ысык-к' in a6 or 'иссыку' in a6 or 'исыку' in a6 or 'ыссыку' in a6 or 'ысыку' in a6 or 'иссыко' in a6 or 'исыко' in a6 or 'ыссыко' in a6 or 'ысыко' in a6 or 'каракол' in a6 or 'балыкч' in a6 or 'чолпонат' in a6 or 'чолпон ат' in a6 or 'чолпон-ат' in a6 or 'барск' in a6 or 'тюп' in a6 or 'тон' in a6 or 'жетиог' in a6 or 'жетыог' in a6 or 'жети ог' in a6 or 'жеты ог' in a6 or 'жети-ог' in a6 or 'жеты-ог' in a6 or 'боконба' in a6 or 'тюп' in a6 or 'тон' in a6 or 'теплокл' in a6 or 'ак су' in a6 or 'аксу' in a6 or 'ак-су' in a6:
            residenceregion = 'Иссык-Куль'
        elif 'нарын' in a6 or 'баетов' in a6 or 'жумгал' in a6 or 'актал' in a6 or 'ак тал' in a6 or 'ак-тал' in a6 or 'чаек' in a6 or 'атбаш' in a6 or 'ат баш' in a6 or 'ат-баш' in a6 or 'кочкор' in a6:
            residenceregion = 'Нарын'
        elif 'ош' in a6 or 'карасу' in a6 or 'кара су' in a6 or 'кара-су' in a6 or 'ноокат' in a6 or 'алай' in a6 or 'араван' in a6 or 'узген' in a6 or 'озгон' in a6 or 'каракулж' in a6 or 'каракулдж' in a6 or 'каракульж' in a6 or 'каракульдж' in a6 or 'кара кулж' in a6 or 'кара кулдж' in a6 or 'кара кульж' in a6 or 'кара кульдж' in a6 or 'кара-кулж' in a6 or 'кара-кулдж' in a6 or 'кара-кульж' in a6 or 'кара-кульдж' in a6 or 'шарк' in a6 or 'гулч' in a6 or 'гульч' in a6:
            residenceregion = 'Ош'

    if factregion != 'не определён':
        region = factregion
    else:
        region = residenceregion

    # Блок расчёта дохода
    try:
        if a9 != 'none':
            children_income = a9 * 5000
        else:
            children_income = 0
    except:
        children_income = 0

    try:
        if a21 == 'True':
            car_income = 8000
        else:
            car_income = 3000
    except:
        car_income = 3000

    try:
        if a22 == 1 or a22 == 2 or a22 == 3 or a22 == 5 or a22 == 7:
            home_income = 5000
        elif a22 == 4 or a22 == 2 or a22 == 6 or a22 == 8:
            home_income = 10000
        else:
            home_income = 3000
    except:
        home_income = 3000

    try:
        if a23 >= 0:
            maxinst = a23
        else:
            maxinst = 0
    except:
        maxinst = 0

    probincome = children_income + car_income + home_income + maxinst

    try:
        if a20 >= 0:
            av_salary = a20
        else:
            av_salary = 0
    except:
        av_salary = 0

    try:
        if a19 >= 0:
            income = a19
        else:
            income = 0
    except:
        income = 0

    if av_salary > 0:
        final_income = av_salary
    else:
        if income < probincome:
            final_income = income
        else:
            final_income = probincome

    # print(final_income)

    # Блок скоринговой карты

    score = 580

    # Пол
    if a1 != 'none':
        if a1 == 2:
            score = score - 9
        elif a1 == 1:
            score = score + 0

    # print(score)

    # Возраст
    if a28 and a2:
        age = relativedelta(a28, a2).years
        if age < 21:
            score = score - 500
        elif 21 <= age <= 25:
            score = score - 29
        elif 25 < age <= 30:
            score = score - 17
        elif 30 < age <= 35:
            score = score - 11
        elif 35 < age <= 40:
            score = score - 8
        elif 40 < age <= 45:
            score = score - 3
        elif 45 < age <= 50:
            score = score + 6
        elif 50 < age <= 55:
            score = score + 12
        elif 55 < age <= 60:
            score = score + 18
        elif 60 < age <= 68:
            score = score + 24
        else:
            score = score - 500

    # print(score)

    # Семейное положение
    if a3:
        if a3 == 1:
            score = score + 11
        elif a3 == 2:
            score = score - 11
        elif a3 == 3:
            score = score + 3
        elif a3 == 4:
            score = score - 12
        elif a3 == 5:
            score = score - 12

    # print(score)

    # Образование
    if a4:
        if a4 == 1:
            score = score + 11
        elif a4 == 2:
            score = score - 12
        elif a4 == 3:
            score = score - 7
        elif a4 == 4:
            score = score + 11

    # print(score)

    # Регион
    if region == 'Бишкек':
        score = score - 39
    elif region == 'Баткен':
        score = score + 20
    elif region == 'Ош':
        score = score + 1
    elif region == 'Джалал-Абад':
        score = score - 2
    elif region == 'Нарын':
        score = score + 3
    elif region == 'Талас':
        score = score + 24
    elif region == 'Чуй':
        score = score - 3
    elif region == 'Иссык-Куль':
        score = score - 14

    # print(score)

    # Вид деятельности
    try:
        if a7 == 'Торговля':
            score = score - 7
        elif a7 == 'Услуги':
            score = score + 3
        elif a7 == 'Производство':
            score = score - 23
        elif a7 == 'Животноводство':
            score = score + 19
        elif a7 == 'Пчеловодство':
            score = score + 19
        elif a7 == 'Птицеводство':
            score = score + 19
        elif a7 == 'Растениеводство':
            score = score + 26
        else:
            if a8 == 87 or a8 == 88 or a8 == 89:
                score = score + 12
            elif a8 == 90 or a8 == 91 or a8 == 92:
                score = score - 11
    except:
        score = score + 0

    # Количество детей
    if a9:
        if a9 == 0:
            score = score + 0
        elif a9 == 1:
            score = score + 8
        elif a9 == 2:
            score = score + 10
        elif a9 == 3:
            score = score + 8
        elif a9 == 4:
            score = score + 16
        elif a9 >= 5:
            score = score - 3
        else:
            score = score - 3

    # print(score)

    # Доход (проверенный)
    if final_income <= 10000:
        score = score - 35
    elif 10000 < final_income <= 15000:
        score = score - 20
    elif 15000 < final_income <= 20000:
        score = score - 8
    elif 20000 < final_income <= 25000:
        score = score + 1
    elif 25000 < final_income <= 30000:
        score = score + 11
    elif 30000 < final_income <= 35000:
        score = score + 17
    elif final_income > 35000:
        score = score + 24
    else:
        score = score + 24

    # print(score)

    # Срок кредита
    if a10:
        if a10 <= 6:
            score = score + 13
        elif 6 < a10 <= 12:
            score = score + 1
        elif 12 < a10 <= 18:
            score = score - 11
        elif a10 > 18:
            score = score - 12
        else:
            score = score - 12

    # print(score)

    # Макс. полученная сумма за историю
    if a11:
        if a11 == 0:
            score = score - 1
        elif 0 < a11 <= 10000:
            score = score + 13
        elif 10000 < a11 <= 27000:
            score = score + 1
        elif 27000 < a11 <= 45000:
            score = score - 2
        elif 45000 < a11 <= 55000:
            score = score + 5
        elif 55000 < a11 <= 80000:
            score = score + 0
        elif 80000 < a11 <= 100000:
            score = score + 0
        elif a11 > 100000:
            score = score - 25
        else:
            score = score - 25

    # print(score)

    # Кол-во предыдущих кредитов в Компаньоне
    if a12:
        if a12 == 0:
            score = score - 20
        elif a12 == 1:
            score = score - 7
        elif a12 == 2:
            score = score - 10
        elif a12 == 3:
            score = score - 1
        elif a12 == 4:
            score = score + 1
        elif a12 >= 5:
            score = score + 27

    # print(score)

    # Кол-во активных кредитов не в Компаньоне
    if a13:
        if a13 == 0:
            score = score + 0
        elif a13 == 1:
            score = score - 5
        elif a13 == 2:
            score = score - 11
        elif a13 >= 3:
            score = score - 12

    # print(score)

    # Сумма активных кредитов не в Компаньоне
    if a14:
        if a14 == 0:
            score = score + 19
        elif 0 < a14 <= 20000:
            score = score + 1
        elif 20000 < a14 <= 40000:
            score = score + 0
        elif 40000 < a14 <= 60000:
            score = score - 10
        elif 60000 < a14 <= 80000:
            score = score - 17
        elif a14 > 80000:
            score = score - 3

    # print(score)

    # Кол-во предыдущих кредитов не в Компаньоне
    if a15:
        if a15 <= 2:
            score = score - 9
        elif 2 < a15 <= 4:
            score = score - 15
        elif 4 < a15 <= 6:
            score = score - 21
        elif 6 < a15 <= 10:
            score = score - 26
        elif a15 > 10:
            score = score - 25
        else:
            score = score - 25

    # print(score)

    # Кол-во активных кредитов всего
    if a16 and a16 > 2:
        score = score - 500

    # print(score)

    # Худшая максимальная и суммарная просрочка
    if a17:
        if a17 > 10 or a18 > 30:
            score = score - 500

    # print(score)

    # print()

    # Работа со взносами, PTI

    pos_install = (final_income - komp_inst * 2 - nonkomp_inst * 2) / 2

    percent = 0.299

    try:
        x0 = ((1 + percent / 12) ** a10) * (percent / 12) / (((1 + percent / 12) ** a10) - 1)
    except:
        x0 = None

    try:
        x1 = math.floor((pos_install / x0) / 1000) * 1000
    except:
        x1 = None

    try:
        if a26 == 'Онлайн кредит для МП для ПИ':
            if x1 <= 100000:
                x2 = x1
            else:
                x2 = 100000
        elif a26 == 'Онлайн кредит для МП для УИ':
            if x1 <= 15000:
                x2 = x1
            else:
                x2 = 15000
        else:
            x2 = 0
    except:
        x2 = None

    try:
        x3 = 0
        if x2 >= 2000: x3 = x2
    except:
        x3 = None

    try:
        if x3 == 0:
            cur_inst = 0
        else:
            cur_inst = ((1 + percent / 12) ** a10) * (percent / 12) * x3 / (((1 + percent / 12) ** a10) - 1)
    except:
        cur_inst = None

    try:
        tot_inst = cur_inst + komp_inst + nonkomp_inst
    except:
        tot_inst = None

    try:
        max_loan_gr = a11 * 1.25
    except:
        max_loan_gr = None

    try:
        if max_loan_gr < x3:
            x4 = max_loan_gr
        elif max_loan_gr >= x3:
            x4 = x3
        else:
            x4 = 0
        x4 = math.floor(x4 / 1000) * 1000
    except:
        x4 = None

    try:
        if a11 == 0 and a12 == 0 and a13 == 0 and a14 == 0 and a15 == 0:
            is_new = 'Новый клиент'
        else:
            is_new = 'Старый клиент'
    except:
        is_new = 'Новый клиент'

    if is_new == 'Новый клиент':
        x5 = 5000
    else:
        x5 = x4

    try:
        if a21:
            is_car = 0
        else:
            is_car = 1
    except:
        is_car = 1

    try:
        if a22 == 4 or a22 == 6 or a22 == 8:
            is_home = 1
        else:
            is_home = 0
    except:
        is_home = 0

    redline = is_car + is_home

    if is_new == 'Новый клиент':
        if redline == 2:
            x6 = 2000
        else:
            x6 = x5
    else:
        x6 = x5

    try:
        if x3 == 0:
            x7 = 0
        else:
            if a27 <= x6:
                x7 = a27
            else:
                x7 = x6
    except:
        x7 = None

    # Подбор суммы в 2 круга

    score_after_sum = score

    if x7:
        if x7 == 0:
            score_after_sum = score_after_sum + 0
        elif 0 < x7 <= 10000:
            score_after_sum = score_after_sum + 71
        elif 10000 < x7 <= 20000:
            score_after_sum = score_after_sum + 68
        elif 20000 < x7 <= 30000:
            score_after_sum = score_after_sum + 55
        elif 30000 < x7 <= 40000:
            score_after_sum = score_after_sum + 45
        elif 40000 < x7 <= 50000:
            score_after_sum = score_after_sum + 29
        elif 50000 < x7 <= 60000:
            score_after_sum = score_after_sum + 23
        elif 60000 < x7 <= 80000:
            score_after_sum = score_after_sum + 13
        elif 80000 < x7 <= 100000:
            score_after_sum = score_after_sum - 5
        elif x7 > 100000:
            score_after_sum = score_after_sum + 0

    x8 = 0
    if score_after_sum >= 517: x8 = x7

    x9 = 517 - score

    x10 = 0
    if x8 == 0:
        if x9 <= 13:
            x10 = 70000
        elif 13 < x9 <= 23:
            x10 = 60000
        elif 23 < x9 <= 29:
            x10 = 50000
        elif 29 < x9 <= 45:
            x10 = 40000
        elif 45 < x9 <= 55:
            x10 = 30000
        elif 55 < x9 <= 68:
            x10 = 20000
        elif 68 < x9 <= 71:
            x10 = 10000
        elif x9 > 71:
            x10 = 0
        else:
            x10 = 0

    try:
        if x10 < x7:
            x11 = x10
        else:
            x11 = x7
    except:
        x11 = None

    score_second_round = 0

    if x11:
        if x11 == 0:
            score_second_round = score_second_round + 0
        elif 0 < x11 <= 10000:
            score_second_round = score_second_round + 71
        elif 10000 < x11 <= 20000:
            score_second_round = score_second_round + 68
        elif 20000 < x11 <= 30000:
            score_second_round = score_second_round + 55
        elif 30000 < x11 <= 40000:
            score_second_round = score_second_round + 45
        elif 40000 < x11 <= 50000:
            score_second_round = score_second_round + 29
        elif 50000 < x11 <= 60000:
            score_second_round = score_second_round + 23
        elif 60000 < x11 <= 80000:
            score_second_round = score_second_round + 13
        elif 80000 < x11 <= 100000:
            score_second_round = score_second_round - 5
        elif x11 > 100000:
            score_second_round = score_second_round + 0

    # Финальный результат
    try:
        if score_after_sum > 517:
            final_score = score_after_sum
        else:
            final_score = score + score_second_round
    except:
        final_score = 0

    try:
        if x8 == 0:
            final_amount = x11
        else:
            final_amount = x8
    except:
        final_amount = 0

    return {'final_score': final_score, 'final_amount': final_amount}

# -*- coding: utf-8 -*-
# Тестовый скрипт для тестового вебсервиса, для написания ТЗ ФинанСофту

from datetime import datetime
from dateutil.relativedelta import *

import math
import sys

ScoreSystem = 'test_1.0'

def get_score(kwargs):
    '''
    Скрипт скоринга обернутый в функцию
    '''

    # если не itn значение, возвращаем None
    try:
        CustomerId = int(kwargs.get('CustomerId'))
    except:
        CustomerId = None

    # если не itn значение, возвращаем None
    try:
        LoanId = int(kwargs.get('LoanId'))
    except:
        LoanId = None

    if (CustomerId == None)|(LoanId == None ):
        return {'CreditAmmount':None, 'CreditPeriod':None, 'ScoreSystem':ScoreSystem, 'AutoApproval':'No'}

    # псевдо расчет суммы
    CreditAmmount = (CustomerId*1000 + LoanId*1000)
    while CreditAmmount>200000:
        CreditAmmount = CreditAmmount/3
    CreditAmmount = int(round(CreditAmmount, -2))
    
    # псевдо расчет срока
    CreditPeriod = (CustomerId*1000 + LoanId*1000)
    while CreditPeriod>24:
        CreditPeriod = CreditPeriod/2
    CreditPeriod = int(round(CreditPeriod))    
    
    # псевдо автоодобрение
    if (CustomerId+LoanId)%2 == 0: 
        AutoApproval = 'Yes'
    else:
        AutoApproval = 'No' 
    
    return {'CreditAmmount':CreditAmmount, 'CreditPeriod':CreditPeriod, 'ScoreSystem':ScoreSystem, 'AutoApproval':AutoApproval}    
    
    

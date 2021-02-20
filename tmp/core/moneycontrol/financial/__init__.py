import enum

from tmp.core.moneycontrol.financial.financialData import getFinancialData
from tmp.core.moneycontrol.financial.enumsFinancial import FinancialType, FinancialFrequency, FinancialRequestType


#  GET CONSOLIDATED DATA
# print(getFinancialData('RI', FinancialType.CONSOLIDATED.value, ConsolidatedType.OVERVIEW.value, ''))
# print(getFinancialData('RI', FinancialType.CONSOLIDATED.value, ConsolidatedType.INCOME.value,
#                        ConsolidatedDuration.QUARTERLY.value))
# print(getFinancialData('RI', FinancialType.CONSOLIDATED.value, ConsolidatedType.BALANCE_SHEET.value, ''))
# print(getFinancialData('RI', FinancialType.CONSOLIDATED.value, ConsolidatedType.CASH_FLOW.value, ''))
# print(getFinancialData('RI', FinancialType.CONSOLIDATED.value, ConsolidatedType.RATIOS.value, ''))

#  GET STANDALONE DATA
# print(getFinancialData('RI', FinancialType.STANDALONE.value, ConsolidatedType.OVERVIEW.value, ''))
# print(getFinancialData('RI', FinancialType.STANDALONE.value, ConsolidatedType.INCOME.value,
#                        ConsolidatedDuration.QUARTERLY.value))
# print(getFinancialData('RI', FinancialType.STANDALONE.value, ConsolidatedType.BALANCE_SHEET.value, ''))
# print(getFinancialData('RI', FinancialType.STANDALONE.value, ConsolidatedType.CASH_FLOW.value, ''))
# print(getFinancialData('RI', FinancialType.STANDALONE.value, ConsolidatedType.RATIOS.value, ''))

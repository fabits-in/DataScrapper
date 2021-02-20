import enum


class FinancialType(enum.Enum):
    OVERVIEW = 'overview'
    INCOME = 'income'
    BALANCE_SHEET = 'balance-sheet'
    CASH_FLOW = 'cash-flow'
    RATIOS = 'ratios'


class FinancialFrequency(enum.Enum):
    QUARTERLY = '3'
    HALF_YEARLY = '6'
    NINE_MONTH = '9'
    ANNUAL = '12'


class FinancialRequestType(enum.Enum):
    CONSOLIDATED = 'C'
    STANDALONE = 'S'

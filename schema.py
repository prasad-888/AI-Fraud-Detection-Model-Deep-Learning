from pydantic import BaseModel

class Transaction(BaseModel):
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float
    isFlaggedFraud: int   
    hour_of_day: int
    day: int
    log1p_amount: float
    amount_to_balance_ratio: float
    is_high_amount: int
    balance_diff_org: float
    balance_error: float
    type_CASH_OUT: int
    type_DEBIT: int
    type_PAYMENT: int
    type_TRANSFER: int

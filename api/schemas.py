from pydantic import BaseModel
from typing import List, Optional

class Transaction(BaseModel):
    id: int
    amount: float
    date: str
    phone_number: str
    transaction_type: str
    description: Optional[str] = None

class TransactionResponse(BaseModel):
    transactions: List[Transaction]

class AnalyticsResponse(BaseModel):
    total_transactions: int
    total_amount: float
    transaction_types: dict[str, int]  # Mapping of transaction type to count
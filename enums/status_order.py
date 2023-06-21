from enum import Enum

class StatusOrder(Enum):
    AWAINTING_CONFIRMATION = (1, 'Awaiting Confirmation')
    CONFIRMED = (2, 'Confirmed')
    IN_PREPARATION = (3, 'In Preparation')
    DELIVERED = (4, 'Delivered')
    CANCELLED = (5, 'Cancelled')

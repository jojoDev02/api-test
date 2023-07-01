from enum import Enum

class StatusOrder(Enum):
    AWAINTING_CONFIRMATION = (1, 'Awaiting Confirmation')
    CONFIRMED = (2, 'Confirmed')
    IN_PREPARATION = (3, 'In Preparation')
    DELIVERED = (4, 'Delivered')
    ON_THE_WAY = (5, 'On the Way')
    CANCELLED = (6, 'Cancelled')

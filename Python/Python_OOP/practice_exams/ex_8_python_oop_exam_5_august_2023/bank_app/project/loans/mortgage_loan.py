from project.loans.base_loan import BaseLoan


class MortgageLoan (BaseLoan):
    START_INTEREST_RATE = 3.5   # in percent
    START_AMOUNT = 50_000

    def __init__(self):
        super().__init__(self.START_INTEREST_RATE, self.START_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5


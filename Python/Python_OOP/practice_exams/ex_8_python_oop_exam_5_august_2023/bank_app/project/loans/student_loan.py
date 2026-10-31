from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    START_INTEREST_RATE = 1.5   # in percent
    START_AMOUNT = 2_000

    def __init__(self):
        super().__init__(self.START_INTEREST_RATE, self.START_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2



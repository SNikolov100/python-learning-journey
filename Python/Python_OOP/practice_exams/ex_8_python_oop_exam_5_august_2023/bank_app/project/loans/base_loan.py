from abc import ABC, abstractmethod


class BaseLoan(ABC):
    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate  #the interest rate of the loan лихвен процент на заема
        self.amount = amount                #the amount of the loan

    @abstractmethod
    def increase_interest_rate(self):
        pass




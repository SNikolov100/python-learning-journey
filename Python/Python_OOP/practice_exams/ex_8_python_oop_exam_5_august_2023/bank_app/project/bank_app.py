from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPE = {"StudentLoan": StudentLoan,
                      "MortgageLoan": MortgageLoan}

    VALID_CLIENT_TYPE = {"Student": Student,
                      "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity        #number of clients а Bank can have
        self.loans: list[BaseLoan] = []              #contain all loans (objects) that are created
        self.clients: list[BaseClient] = []                             #contain all clients (objects) that are created

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPE:
            raise Exception("Invalid loan type!")
        cls_loan = self.VALID_LOAN_TYPE[loan_type]()
        self.loans.append(cls_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPE:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        cls_client = self.VALID_CLIENT_TYPE[client_type](client_name, client_id, income)
        self.clients.append(cls_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        valid_types = {"Student": "StudentLoan",
                       "Adult": "MortgageLoan" }
        client_object = self.get_client_object(client_id)
        if valid_types[client_object.__class__.__name__] != loan_type:
            raise Exception("Inappropriate loan type!")
        loan_object = next((l for l in self.loans if l.__class__.__name__ == loan_type), None)
        client_object.loans.append(loan_object)
        self.loans.remove(loan_object)
        return f"Successfully granted {loan_type} to {client_object.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client_object = self.get_client_object(client_id)
        if client_object not in self.clients:
            raise Exception("No such client!")

        if client_object.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client_object)
        return f"Successfully removed {client_object.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        laon_objects = [l for l in self.loans if l.__class__.__name__ == loan_type]
        for loan in laon_objects:
            loan.increase_interest_rate()
        return f"Successfully changed {len(laon_objects)} loans."

    def increase_clients_interest(self, min_rate: float):
        clients_list = [c for c in self.clients if c.interest < min_rate]
        for client in clients_list:
            client.increase_clients_interest()
        return f"Number of clients affected: {len(clients_list)}."

    def get_statistics(self):
        avg_client_interest_rate = 0
        total_amount = 0

        for client in self.clients:
            total_amount += sum(l.amount for l in client.loans)

        sum_interests = sum(cl.interest for cl in self.clients)

        if self.clients:
            avg_client_interest_rate = sum_interests / len(self.clients)

        result = [f"Active Clients: {len(self.clients)}",
                  f"Total Income: {sum(cl.income for cl in self.clients):.2f}",
                  f"Granted Loans: {sum(len(cl.loans) for cl in self.clients)}, Total Sum: {total_amount:.2f}",
                  f"Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}",
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"]
        return '\n'.join(result)

    def get_client_object(self, client_number):
        return next((c for c in self.clients if c.client_id == client_number), None)





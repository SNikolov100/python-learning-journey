class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass

domain_match = ("com", "bg", "org", "net")

while True:
    command = input()

    if command == "End":
        break

    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")
    name = command.split("@")

    if len(name[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    domain = command.split(".")

    if domain[-1] not in domain_match:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")





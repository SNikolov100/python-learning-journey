import calendar


class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, from_date_id: int, name: str, date: str, age_restriction: int):
        _, month, creation_year = date.split(".")
        return cls(name, from_date_id, int(creation_year), calendar.month_name[int(month)], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {'not ' if not self.is_rented else ''}rented"




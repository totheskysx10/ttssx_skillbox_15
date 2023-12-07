class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, entered_date):
        try:
            day, month, year = map(int, entered_date.split('-'))
            date = cls(day, month, year)
            if date.is_valid_date():
                return date
            else:
                raise ValueError("Некорректная дата")
        except ValueError:
            raise ValueError("Некорректный формат строки даты")

    def is_valid_date(self):
        if self.day < 1 or self.month < 1 or self.month > 12 or self.year < 1:
            return False
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Проверка на високосный год
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            days_in_month[2] = 29

        return 1 <= self.day <= days_in_month[self.month]

    def __str__(self):
        return f"День: {self.day}   Месяц: {self.month}   Год: {self.year}"

date = Date.from_string('10-12-2077')
print(date)
print(Date.from_string('10-12-2077'))
print(Date.from_string('40-12-2077'))

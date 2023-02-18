class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.month:02}/{self.day:02}/{self.year:04}"

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"

    def is_leap_year(self):
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            return True
        return False

    def is_valid(self):
        if self.month < 1 or self.month > 12:
            return False
        if self.day < 1 or self.day > 31:
            return False
        if self.month == 2 and self.is_leap_year():
            return self.day <= 29
        elif self.month == 2:
            return self.day <= 28
        elif self.month in [4, 6, 9, 11]:
            return self.day <= 30
        else:
            return self.day <= 31

    def tomorrow(self):
        days_in_month = [31, 28 + int(self.is_leap_year()), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.day == days_in_month[self.month - 1]:
            if self.month == 12:
                self.year += 1
                self.month = 1
            else:
                self.month += 1
            self.day = 1
        else:
            self.day += 1









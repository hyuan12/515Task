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



def test_Date():
    d = Date(2021, 11, 8)
    assert repr(d) == "Date(2021, 11, 8)"
    assert str(d) == "11/08/2021"

    d2 = Date(1776, 7, 4)
    assert repr(d2) == "Date(1776, 7, 4)"
    assert str(d2) == "07/04/1776"

    d3 = Date(76, 1, 24)
    assert repr(d3) == "Date(76, 1, 24)"
    assert str(d3) == "01/24/0076"

def test_is_leap_year():
    d = Date(2020, 1, 1)
    assert d.is_leap_year() == True

    d2 = Date(2021, 1, 1)
    assert d2.is_leap_year() == False

def test_is_valid():
    d = Date(2021, 2, 29)
    assert d.is_valid() == False

    d2 = Date(2020, 2, 29)
    assert d2.is_valid() == True

def test_tomorrow():
    d = Date(2021, 1, 31)
    d.tomorrow()
    assert str(d) == "02/01/2021"

    d2 = Date(2021, 2, 28)
    d2.tomorrow()
    assert str(d2) == "03/01/2021"

    d3 = Date(2020, 2, 29)
    d3.tomorrow()
    assert str(d3) == "03

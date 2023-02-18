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


# doctests
def test_date():
    d = Date(2022, 2, 18)
    assert repr(d) == "Date(2022, 2, 18)"
    assert str(d) == "02/18/2022"

    d2 = Date(1999, 12, 31)
    assert repr(d2) == "Date(1999, 12, 31)"
    assert str(d2) == "12/31/1999"

    d3 = Date(2000, 2, 29)
    assert d3.is_leap_year() == True
    d4 = Date(1900, 2, 29)
    assert d4.is_leap_year() == False

    assert d.is_valid() == True
    assert d2.is_valid() == True
    assert d3.is_valid() == True
    assert d4.is_valid() == False

    d.tomorrow()
    assert str(d) == "02/19/2022"
    d.tomorrow()
    assert str(d) == "02/20/2022"

    d5 = Date(2022, 2, 28)
    d5.tomorrow()
    assert str(d5) == "03/01/2022"
    d6 = Date(2020, 2, 28)
    d6.tomorrow()
    assert str(d6) == "02/29/2020"
    d6.tomorrow()
    assert str(d6) == "03/01/2020"

    d = Date(2022, 2, 18)
    assert repr(d) == "Date(2022, 2, 18)"
    assert str(d) == "02/18/2022"

    d2 = Date(1999, 12, 31)
    assert repr(d2) == "Date(1999, 12, 31)"
    assert str(d2) == "12/31/1999"

    d3 = Date(2000, 2, 29)
    assert d3.is_leap_year() == True
    d4 = Date(1900, 2, 29)
    assert d4.is_leap_year() == False

    assert d.is_valid() == True
    assert d2.is_valid() == True
    assert d3.is_valid() == True
    assert d4.is_valid() == False

    d.tomorrow()
    assert str(d) == "02/19/2022"
    d.tomorrow()
    assert str(d) == "02/20/2022"

    d5 = Date(2022, 2, 28)
    d5.tomorrow()
    assert str(d5) == "03/01/2022"
    d6 = Date(2020, 2, 28)
    d6.tomorrow()
    assert str(d6) == "02/29/2020"
    d6.tomorrow()
    assert str(d6) == "03/01/2020"
test_date()





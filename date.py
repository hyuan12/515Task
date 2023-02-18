class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"Date({self.year}, {self.month:02}, {self.day:02})"

    def __str__(self):
        return f"{self.month:02}/{self.day:02}/{self.year}"

    def is_leap_year(self):
        """
        Returns True if the year is a leap year, False otherwise.

        >>> d = Date(2024, 1, 1)
        >>> d.is_leap_year()
        True

        >>> d = Date(2023, 1, 1)
        >>> d.is_leap_year()
        False
        """
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            return True
        else:
            return False

    def is_valid(self):
        """
        Returns True if the date is valid, False otherwise.

        >>> d = Date(2023, 2, 28)
        >>> d.is_valid()
        True

        >>> d = Date(2023, 2, 29)
        >>> d.is_valid()
        False
        """
        if self.month < 1 or self.month > 12:
            return False

        if self.day < 1 or self.day > self.days_in_month():
            return False

        if self.year == 0:
            return False

        return True

    def tomorrow(self):
        """
        Update the Date object to refer to the next day.

        >>> d = Date(2023, 2, 28)
        >>> d.tomorrow()
        >>> d
        Date(2023, 03, 01)

        >>> d = Date(2022, 12, 31)
        >>> d.tomorrow()
        >>> d
        Date(2023, 01, 01)
        """
        if self.day < self.days_in_month():
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

    def days_in_month(self):
        """
        Returns the number of days in the month.

        >>> d = Date(2023, 2, 1)
        >>> d.days_in_month()
        28

        >>> d = Date(2024, 2, 1)
        >>> d.days_in_month()
        29
        """
        if self.month == 2:
            if self.is_leap_year():
                return 29
            else:
                return 28
        elif self.month in {4, 6, 9, 11}:
            return 30
        else:
            return 31

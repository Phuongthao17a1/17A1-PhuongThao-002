class Date:
    def __init__(self,day,month,year):
        self.day =day
        self.month=month
        self.year=year
    def dislay(self):
        print('currently is',self.day,'/',self.month,'/',self.year)
    def is_leap_year(self, year):
        
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def days_in_month(self, month, year):
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if self.is_leap_year(year) else 28
        return 0  

    def next(self):
        
        if self.day < self.days_in_month(self.month, self.year):
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

date=Date(30,4,2005)
date.dislay()
date.next()
date.dislay()
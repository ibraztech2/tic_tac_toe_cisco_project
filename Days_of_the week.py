class WeekdayError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Weeker:
    def __init__(self, __string):
        self.__string = __string
        self.__valid_weekdays = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
        if self.__string not in self.__valid_weekdays:
            raise WeekdayError("Sorry i can\'t serve your request .")
    def __str__(self):
        return self.__string

    def add_days(self,n):
        current_date =  self.__valid_weekdays.index(self.__string)
        currentDay_num = current_date + n
        # while currentDay_num > 6:
        # currentDay_num  = currentDay_num % 6
        while currentDay_num > 6:
            currentDay_num = currentDay_num - 7
        return self.__valid_weekdays[- currentDay_num]

    def subtarct_day(self,n):
        current_date = self.__valid_weekdays.index(self.__string)
        current_date_num = n  - current_date - 1

        while current_date_num > 6:
            current_date_num = current_date_num - 7
            print(current_date_num)
        return self.__valid_weekdays[- current_date_num]
try:
    weekday  = Weeker("Mon")
    # print(weekday)
    # print(weekday.add_days(15))
    # print(weekday)
    print(weekday.subtarct_day(23))
    # print(weekday)
    weekday = Weeker("Mondqay")
except WeekdayError as wk:
    print("Sorry i can\'t serve your request .")


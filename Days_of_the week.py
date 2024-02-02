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
        currentDay_num = current_date + n -1
        if currentDay_num > 6:
            currentDay_num = currentDay_num - 6
        return self.__valid_weekdays[currentDay_num]

    def subtarct_day(self,n):
        current_date = self.__valid_weekdays.index(self.__string)
        current_date_num = n -1 - current_date

        if current_date_num < -6:
            current_date_num = 6 - current_date_num
        return self.__valid_weekdays[current_date_num]
weeker1 = Weeker("Sun")
try:
    print(weeker1)
    print(weeker.add_days(7))
    print(weeker.subtarct_day(7))
except WeekdayError as wk:
    print(wk.args)


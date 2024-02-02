class Timer:
    def __init__(self,__hour = 00,__minutes = 00,__seconds = 00):
        self.__hour = __hour
        self.__minutes = __minutes
        self.__seconds = __seconds
        self.__h = 0
        self.__m = 0
        self.__s = 0
        if self.__minutes > 9:
            self.__m= 0
        else:
            self.__m= ''
        if self.__hour < 10:
            self.__h = 0
        else:
            self.__h = ''
        if self.__seconds > 9:
            self.__s = 0
        else:
            self.__s = ''

    def __str__(self):
        return f"0{self.__hour}:0{self.__minutes}:0{self.__seconds}"

    def next_second(self):
        if self.__seconds != 59 :
            self.__seconds += 1
        else:
            if self.__seconds == 59 and self.__minutes != 59:
                self.__seconds = 0

            if self.__minutes == 59 and self.__seconds == 59:
                self.__hour += 1
                self.__seconds,self.__minutes = 0,0
            else:
                self.__minutes += 1
        return f"0{self.__hour}:0{self.__minutes}:0{self.__seconds}"

    def previous_second(self):
        if self.__seconds != 0:
            self.__seconds -= 1
        else:
            if self.__seconds == 0 and self.__minutes != 0:
                self.__minutes -= 1
                print(self.__minutes)
                self.__seconds = 59
                return self.__minutes
            else:
                # self.__seconds -= 1
                pass
            if self.__seconds ==0 and self.__minutes == 0:
                self.__hour -=1
                self.__minutes = 59
                self.__seconds = 59
            else:
                self.__minutes -= 1
        return f"{self.__h}{self.__hour}:{self.__m}{self.__minutes}:{self.__s}{self.__seconds}"
timer = Timer(2,0,0)
print(timer)
for i in range(5):
    print(timer.previous_second())

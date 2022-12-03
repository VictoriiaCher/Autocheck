from collections import UserString
import re


class NumberString(UserString):
    def number_count(self):
        num = re.findall(r"\d", self.data)
        return len(num)


str_data = NumberString("hhk4k5l15ll8khh7")
print(str_data.number_count())

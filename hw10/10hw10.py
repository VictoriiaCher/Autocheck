from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        sum = 0
        for value in self.data:
            if value > 0:
                sum = sum + value
        return sum


user_list = AmountPaymentList([2, 6, -5, 5, 9])
print(user_list.amount_payment())

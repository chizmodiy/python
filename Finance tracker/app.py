from models import Transaction, Wallet


x1 = Transaction(23, 'їжа', 'булка')
x2 = Transaction(150, 'розваги', 'кіно')
x3 = Transaction(500, 'оренда', 'квартира')
x4 = Transaction(70, 'транспорт', 'автобус')
x5 = Transaction(2000, 'дохід', 'зарплата')
filename = "Finance tracker/data.json"

y = Wallet(filename)

y.add()



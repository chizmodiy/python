"""Клас Transaction (models.py):
Атрибути: amount (сума), category (їжа, розваги, оренда), type (Дохід/Витрата).
Користувач може додавати транзакції, бачити баланс та фільтрувати витрати по категоріям.
"""
from utils import filter_by_category,calculate_balance,save
import json


class Transaction:
    def __init__(self, amount,category,type):
        self.amount = amount
        self.category = category
        self.type = category
    

class Wallet:
    def __init__(self ,directory):
        self.directory = directory
        self.transactions = []
        try :
            with open(directory) as obj:
                self.transactions = json.load(obj)
        except FileNotFoundError :
            save([],self.directory)
            self.transactions = []
        except json.decoder.JSONDecodeError:
            save([],self.directory)
            self.transactions= []

    def add(self,amount,category,type):
        new = Transaction(amount,category,type)
        self.transactions.append(new.__dict__)
        save(self.transactions,self.directory)
        
        

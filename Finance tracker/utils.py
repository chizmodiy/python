import json

def calculate_balance(transactions):
    return sum([x['amount'] for x in transactions])


def filter_by_category(transactions, category):
    if category in [x['category'] for x in transactions]:
        return sum([x['amount'] for x in transactions if x['category'] == category ])
    else:
        return "Такої категорії немає"
    
def save(data , directory):
    with open(directory,'w') as obj:
        json.dump(directory,data)
        


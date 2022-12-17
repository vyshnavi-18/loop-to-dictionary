
from typing import counter
list={'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1','amount':750}
b=counter()
for d in list:
    b[d['item']]+=d['amount']
print(b)
    
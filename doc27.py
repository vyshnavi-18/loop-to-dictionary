student = [{'id': 1, 'success': True, 'name': 'Lary'},
{'id': 2, 'success': False, 'name': 'Rabi'},
{'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(a['id'] for a in student))
print(sum(a['success'] for a in student))
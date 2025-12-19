# Given a list of dictionaries, each representing a person with 'name' and 'age' keys,
# use lambda functions to filter out people under 18 and then map the remaining peoples
# names to a new list
from decorator import append

People_info = [
    {'name' : 'Gayathri', 'age' : 48},
    {'name' : 'Yashaswini', 'age' : 15},
    {'name' : 'Shreenidhi', 'age' : 17}
]
filtered_name=['']
filtered_data =list(filter(lambda d: d['name'] if d['age'] < 18 else '', People_info))
for i in People_info:
    for key, val in i.items():
        if key == 'name':
            filtered_name.append(val)
print(filtered_name)
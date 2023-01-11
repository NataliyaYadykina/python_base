users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary))
# проходит по минимальному набору данных salary
print(data)


data_enum = list(enumerate(users))
print(data_enum)
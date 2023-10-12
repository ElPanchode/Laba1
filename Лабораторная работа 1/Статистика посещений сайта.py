users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
users1 = set(users)
users2 = len(users)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
slovar1 = {'Общее количество': users2, 'Уникальные посещения': len(users1)}
print(slovar1)
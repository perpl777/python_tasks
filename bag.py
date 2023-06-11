bag = 10
newbag = {}

inventory = {
    'sleeping bag':3,
    'canned food':0.3,
    'plaid':1.8,
    'watter bottles':0.5,
    'medicine chest':0.1,
    'dishes':0.5,
    'compas':0.05,
    'warm clothes':1.5,
    'torch':0.02,
    'bower hat':0.5,
    'axe':0.5,
    'blancket':1,
    'knife':0.05,
    'thermos':0.5,
    'map':0.01
}

list_key = []
for key in inventory:
    list_key.append(key)

list_value = []
for key in inventory: 
    list_value.append(inventory.get(key))


for i in range(len(list_value) - 1): #сортируем список с ключами и значениями в порядке убывания пузырьком
    for j in range(len(list_value)-i-1):
        if list_value[j] < list_value[j+1]:
            list_value[j], list_value[j+1] = list_value[j+1], list_value[j]
            list_key[j], list_key[j+1] = list_key[j+1], list_key[j]


for i in range(len(list_value)):
    if bag - list_value[i] >= 0:
        bag -= list_value[i]
        newbag[list_key[i]] = list_value[i]
        

print('you took: ')
for key in newbag:
    print(f"{key}:{str(newbag[key]).replace('[', '').replace(']', '')}")
    


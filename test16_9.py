from practic16_9 import MagicStr, прямоугольник, Client
#16.9.1
test = MagicStr(5,10,50,100)
print(test.__str__())
#16.9.2
площь_1 = прямоугольник(20,40)
print(площь_1.get_площадь())

#16.9.3
client_1 = Client('Иван', 'Петров','Москва', 50)
print(client_1.get_client())

#16.9.4
client_2 = Client('Леонид','Сидоров','Магадан', 500)
client_3 = Client('Марфа', 'Оболенская', 'Васюки', 100000)
clients = [client_1, client_2, client_3]
n = 0
for client in clients:
    print(n+1, client.get_corporativ_client())
    n += 1

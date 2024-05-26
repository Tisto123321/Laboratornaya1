from replit import db

#Вставляем данные клиентов в Replit DB



def insert_client_information_data():
    client_information_data = [{
        'client_code': '12345',
        'fname': 'Peter',
        'lname': 'Griffin',
        'age': '59',
        'sex': 'm',
        'city': 'Paris'
    }, {
        'client_code': '54321',
        'fname': 'Homer',
        'lname': 'Simpson',
        'age': '43',
        'sex': 'm',
        'city': 'London'
    }, {
        'client_code': '67890',
        'fname': 'Elena',
        'lname': 'Irving',
        'age': '23',
        'sex': 'f',
        'city': 'Madrid'
    }, {
        'client_code': '12345345',
        'fname': 'Katty',
        'lname': 'Filgenton',
        'age': '36',
        'sex': 'f',
        'city': 'New-York'
    }, {
        'client_code': '1234564445',
        'fname': 'Jimmy',
        'lname': 'MgGill',
        'age': '51',
        'sex': 'm',
        'city': 'Moscow'
    }, {
        'client_code': '12334545',
        'fname': 'Saul',
        'lname': 'Goodman',
        'age': '34',
        'sex': 'm',
        'city': 'Tula'
    }, {
        'client_code': '1235646445',
        'fname': 'Diana',
        'lname': 'Zhukova',
        'age': '54',
        'sex': 'f',
        'city': 'Tokyo'
    }, {
        'client_code': '2334243',
        'fname': 'Michel',
        'lname': 'Starling',
        'age': '28',
        'sex': 'f',
        'city': 'Barcelona'
    }, {
        'client_code': '122343254345',
        'fname': 'Walter',
        'lname': 'White',
        'age': '29',
        'sex': 'm',
        'city': 'Liverpool'
    }, {
        'client_code': '12212345',
        'fname': 'Gustav',
        'lname': 'Fring',
        'age': '20',
        'sex': 'm',
        'city': 'Samara'
    }]

    # db insertion logic here
    for idx, client in enumerate(client_information_data):
        if db is not None:
            db[f"client_{idx}"] = client

    return client_information_data

        
#Получаем данные по клиентам из Replit DB
def get_client_information():
    client_information_data = []
    if db is not None:
        for key in db.keys():
            if key.startswith("client_"):
                        client_information_data.append(db[key])
    return client_information_data


#Вставляем данные клиентов в Replit DB
insert_client_information_data()

#Получаем и выводим данные по клиентам из Replit DB
print(get_client_information())

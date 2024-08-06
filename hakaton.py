database = {
    'Шевченко': {
        'position': 'Асистент',
        'EC': 0.944,
        'last three projects': ['Допомога з встановленням модулів', 'Виправлення помилок', 'Допомога з поділом коду']
    },
    'Солонський': {
        'position': 'Головний інструктор',
        'EC': 0.868,
        'last three projects': ['Таймер за допомогою модулю  time', 'Списки, команди для роботи з ними', 'Малювання змійкою']
    },
    'Коваленко': {
        'position': 'Координатор проєктів',
        'EC': 0.932,
        'last three projects': ['Дописування підказок', 'База 3 майбутніх проєктів', 'Дописування змін до коду']
    }
}

print('Прізвища співробітників:')
for surnames in database:
    print('-', surnames)

max_ec = 0
sur_ec = 0

for surname, details in database.items():
    ec_value = details['EC']
    if ec_value > max_ec:
        max_ec = ec_value
        sur_ec = surname

print('\nНайефективніший співробітник:', sur_ec, 'з коефіцієнтом ефективності', max_ec)

print('\nПосади співробітників:')
for surname in database:
    print(surname, '-', database[surname]['position'])

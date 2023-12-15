def shop(hero) -> bool:
    print(f'{hero[0]}, приехал в лавку')
    print('1 - Купить предметы')
    print('2 - Продать предметы')
    print('0 - Выход из игры')
    option = input('Введите номер опции: ')
    if option == '1':
        print('1 - Купить зелье лечения за 5')
        print('2 - Купить зелье копчения за 7')
        option = input('Введите номер опции: ')
        if option == '1':
            buy_item(hero, 'зелье лечения', 5)
        if option == '2':
            buy_item(hero, 'зелье копчения', 7)
    if option == '2':
        # TODO вывести на экран названия всех предметов с порядковым номером
        number = 1
        while number < len(hero[5]):
            print(hero[number])
            number += 1
            pass
    elif option == '0':
        return False
    return True


def buy_item(hero: list, item_name: str, item_price: int) -> None:
    if hero[2] >= item_price:
        hero[5].append(item_name)
        hero[2] -= item_price
        print(f'{hero[0]} купил {item_name}')
    else:
        print(f'У {hero[0]} недостаточно денег')


hero = ['Вася', 100, 20, 1, 0, []]
is_game = True
while True:
    print(hero)
    is_game = shop(hero)
    if not is_game:
        break


'''
number = 1
        for element in hero[5]:
            option = print(f'{number} - {hero[5]}')
            number += 1
'''
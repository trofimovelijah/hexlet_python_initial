# 1. Приветствие
# 2. Мануал
# 3. Вывод списка валют
# 4. Запрос имеющийся валюта
# 5. Количество этой валюты
# 6. Валюту для конвертации
# 7. Вывод расчёта

CURRENCIES = {
    "USD": 1,
    "EUR": 1.08,
    "GPB": 1.24,
    "RUB": 0.012
}

# 1.
print("Добро пожаловать в конвертер валют!")

# 2.
print("""
Наша программа поможет Вам конвертировать валюту.
- Введение имеющийся валюты
- Количество этой валюты
- Выбор валюты для конвертации
""")

# 3.
print("Вам предложены следующие валюты:")
key_counter = 0
for key in CURRENCIES:
    key_counter += 1
    print(f'{key_counter} -> {key}')


# 4.
def input_currency():
    while True:
        selected_currency = input("Введите имеющуюся валюту: ")
        if selected_currency not in CURRENCIES.keys():
            print('Вы ввели неверный код валюты')
        else:
            return selected_currency


selected_currency = input_currency()


# 5.
def input_amount():
    while True:
        selected_amount = float(input("Введите имеющуюся сумму: "))
        if selected_amount <= 0:
            print("Укажите сумму больше 0 для конвертации")
        else:
            return selected_amount


selected_amount = input_amount()


# 6.
def input_conversion_currency():
    while True:
        exchanged_currency = input("Выберите валюту для конвертации: ")
        if exchanged_currency not in CURRENCIES.keys():
            print("Вы ввели неверный код валюты")
        else:
            return exchanged_currency


exchanged_currency = input_conversion_currency()

# 7.
# def calculation_amount(user_currency, conversion_currency, current_amount):
converted_amount = CURRENCIES.get(selected_currency) / CURRENCIES.get(exchanged_currency) * selected_amount
print(f"Итого: {round(converted_amount, 2)} {exchanged_currency}")

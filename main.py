# Calc
# add_record() — сохраняет новую запись о расходах
# get_today_stats() — считает сколько денег потрачено сегодня
# get_today_cash_remained(currency) — сколько еще можно потратить сегодня в RUR, USD, EUR
# get_week_stats() — сколько денег потрачено за 7 дней

# Calories
# add_record() — сохраняет новую запись о приеме пищи
# get_today_stats() — считает сколько калорий съедено сегодня
# get_calories_remained() — сколько еще можно/нужно получить калорий сегодня
# get_week_stats() — сколько калорий получено за 7 дней

# class Calculator(limit) — родительский, с общими методами (лимит трат / калорий, пустой список records для записей)
# class CaloriesCalculator() — дочерний
# class CashCalculator() — дочерний
# class Record() — для записей:
#   amount — сумма / калории.
#   date — дата создания записи передается или присваивается автоматом.
#   comment — на что потрачены деньги / откуда появились калории

# для CashCalculator
# r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
# r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
# r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

# для CaloriesCalculator
# r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
# r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
# r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")


from datetime import date, datetime, timedelta

# Общие методы:


class Calculator:
    records = []

    def __init__(self, limit):
        self.limit = limit

    def add_record(self, record):
        self.records.append([record.amount, record.comment, record.date])

    def get_today_stats(self):
        result = [x[0] for x in self.records if x[2] == date.today()]  # перебор сумм, если в записи сегодняшняя дата
        print('Сегодня потрачено', sum(result))
        return sum(result)

    def get_week_stats(self):
        weeksum = [w[0] for w in self.records if w[2] >= date.today() - timedelta(days=7)]
        print('За неделю потрачено', sum(weeksum))
        return sum(weeksum)


# Калькулятор денег:


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        usd_rate = 65
        euro_rate = 62
        if currency == 'rub':
            print('Сегодня можно потратить еще', self.limit - self.get_today_stats(), 'рублей')
        if currency == 'usd':
            print('Сегодня можно потратить еще', self.limit / usd_rate - self.get_today_stats() / usd_rate, 'баксов')
        if currency == 'eur':
            print('Сегодня можно потратить еще', self.limit / euro_rate - self.get_today_stats() / euro_rate, 'евро')


# Калькулятор калорий:


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

# Новая запись:


class Record:
    def __init__(self, **kwargs):
        self.amount = kwargs['amount']
        self.comment = kwargs['comment']
        if len(kwargs) == 3:
            self.date = datetime.strptime(kwargs['date'], '%d.%m.%Y').date()
        else:
            self.date = date.today()


cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
cash_calculator.add_record(Record(amount=400, comment="Кафе", date="06.11.2022"))
cash_calculator.add_record(Record(amount=145, comment="кофе"))

print(cash_calculator.get_today_stats())
print(cash_calculator.get_week_stats())
print(cash_calculator.get_today_cash_remained("eur"))

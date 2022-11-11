from datetime import date, datetime, timedelta


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append([record.amount, record.comment, record.date])

    def get_today_stats(self):
        daysum = [x[0] for x in self.records if x[2] == date.today()]
        return f'Сегодня потрачено {sum(daysum)}'

    def today_stats(self):
        return sum([x[0] for x in self.records if x[2] == date.today()])

    def get_week_stats(self):
        weeksum = [w[0] for w in self.records if w[2] >= date.today() - timedelta(days=6)]
        return f'За неделю потрачено {sum(weeksum)}'


class CashCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        usd_rate = 65
        euro_rate = 62

        if currency == 'rub':
            cur = 'руб.'
            lim = self.limit
            todaysum = self.today_stats()
        elif currency == 'usd':
            cur = 'USD'
            lim = self.limit / usd_rate
            todaysum = self.today_stats() / usd_rate
        elif currency == 'eur':
            cur = 'Euro'
            lim = self.limit / euro_rate
            todaysum = self.today_stats() / euro_rate

        ostatok = round(lim - todaysum, 2)
        dolg = round(todaysum - lim, 2)

        if todaysum < lim:
            return f'На сегодня осталось {ostatok} {cur}'
        elif todaysum == lim:
            return f'Денег нет, держись'
        elif todaysum > lim:
            return f'Денег нет, держись: твой долг - {dolg} {cur}'


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        lim = self.limit
        todaysum = self.today_stats()

        if todaysum < lim:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более \
{round(lim - todaysum, 2)} кКал'
        elif todaysum >= lim:
            return f'Хватит есть!'


class Record:
    def __init__(self, **kwargs):
        self.amount = kwargs['amount']
        self.comment = kwargs['comment']
        if len(kwargs) == 3:
            self.date = datetime.strptime(kwargs['date'], '%d.%m.%Y').date()
        else:
            self.date = date.today()


cash_calculator = CashCalculator(1000)
calories_calculator = CaloriesCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment="Безудержный шопинг", date="08.03.2019"))
cash_calculator.add_record(Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019"))
cash_calculator.add_record(Record(amount=691, comment="Катание на такси", date="08.11.2022"))
cash_calculator.add_record(Record(amount=1001, comment="Летание на параплане"))

calories_calculator.add_record(Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019"))
calories_calculator.add_record(Record(amount=84, comment="Йогурт.", date="23.02.2019"))
calories_calculator.add_record(Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019"))
calories_calculator.add_record(Record(amount=678, comment="Cтарбакс"))

print(cash_calculator.get_today_stats())
print(cash_calculator.get_week_stats())
print(cash_calculator.get_today_cash_remained("rub"))
print(calories_calculator.get_calories_remained())

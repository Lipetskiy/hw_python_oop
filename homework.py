import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, entry):
        self.records.append(entry)

    def get_today_stats(self):
        now = dt.datetime.now()

        today_amount = 0
        for data in self.records:
            if data.date == now.date():
                today_amount += data.amount
            else:
                pass
        return today_amount

    def get_today_cash_remained(self, currency):
        now = dt.datetime.now()

        today_amount = 0
        for data in self.records:
            if data.date == now.date():
                today_amount += data.amount
            else:
                pass
        if today_amount == 0:
            print("Денег нет, держись")
        elif self.limit < today_amount:
            print(f"Денег нет, держись: твой долг - {self.limit - today_amount} {currency}")
        elif self.limit > today_amount:
            print(f"На сегодня осталось {self.limit - today_amount} {currency}")

    def get_week_stats(self):
        now = dt.datetime.now()
        yesterday = now - dt.timedelta(days=1)
        get_week = now + dt.timedelta(weeks=1)
        date_format = '%d.%m.%Y'

        today_amount = 0
        for data in self.records:
            date_adjustment = dt.datetime.strptime(data.date, date_format)
            if yesterday < date_adjustment < get_week:
                today_amount += data.amount
            else:
                pass
        return today_amount

    def get_calories_remained(self):
        now = dt.datetime.now()

        today_amount = 0
        for data in self.records:
            if data.date == now.date():
                today_amount += data.amount
            else:
                pass

        if self.limit > today_amount:
            calorie_difference = self.limit - today_amount
            print(f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calorie_difference} кКал")
        else:
            print("Хватит есть!")


class Record:
    now = dt.datetime.now()

    def __init__(self, amount, comment, date=now.date()):
        self.amount = amount
        self.date = date
        self.comment = comment


class CaloriesCalculator(Calculator):
    pass


class CashCalculator(Calculator):

    USD_RATE = 75.00
    EURO_RATE = 90.00
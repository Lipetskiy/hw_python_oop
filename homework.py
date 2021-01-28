import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, entry):
        self.records.append(entry)

    def get_today_stats(self):
        now = dt.datetime.now()
        for data in self.records:
            convert_date = dt.datetime.strptime(data.date, '%d.%m.%Y')
            if convert_date.date() == now.date():
                self.limit -= data.amount
            else:
                pass
        return self.limit

    def get_today_cash_remained(self, currency):
        Calculator.get_today_stats()
        if self.limit == 0:
            convert = "Денег нет, держись"
        elif self.limit > 0:
            convert = f"На сегодня осталось {round(self.limit, 2)} {currency}"
        else:
            convert = f"Денег нет, держись: твой долг - {round(self.limit, 2)} {self.currency}"
        return convert

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
        Calculator.get_today_stats()
        if self.limit > 0:
            print(f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit} кКал")
        else:
            print("Хватит есть!")

class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.date = date or dt.datetime.now()
        self.comment = comment


class CaloriesCalculator(Calculator):
    def get_today_stats(self):
        return Calculator.get_today_stats(self)

    def get_calories_remained(self):
        CaloriesCalculator.get_today_stats(self)
        # print("Каллорийность", self.limit)
        if self.limit > 0:
            print(f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit} кКал")
        else:
            print("Хватит есть!")


class CashCalculator(Calculator):
    USD_RATE = 75.11
    EURO_RATE = 90.11

    def __init__(self, limit):
        super().__init__(limit)
        self.currency = "руб"

    def get_today_stats(self):
        return Calculator.get_today_stats(self)

    def get_today_cash_remained(self, currency):
        self.currency = currency
        CashCalculator.get_today_stats(self)
        convert = 0
        if self.currency == "usd":
            convert = self.limit / CashCalculator.USD_RATE
            self.currency = "USD"
        elif self.currency == "eur":
            convert = self.limit / CashCalculator.EURO_RATE
            self.currency = "Euro"
        elif self.currency == "rub":
            convert = self.limit
            self.currency = "руб"

        if self.limit == 0:
            answer = "Денег нет, держись"
        elif self.limit > 0:
            answer = f"На сегодня осталось {abs(round(convert,2))} {self.currency}"
        else:
            answer = f"Денег нет, держись: твой долг - {abs(round(convert, 2))} {self.currency}"
        return answer


cash_calculator = CashCalculator(1000)
calories_calculator = CaloriesCalculator(1000)
cash_calculator.add_record(Record(amount=1110, comment="кофе", date='28.01.2021'))
calories_calculator.add_record(Record(amount=900, comment="Кофе", date='28.01.2021'))
# print(cash_calculator.get_today_cash_remained("rub"))
print(cash_calculator.get_today_cash_remained("rub"))
print(calories_calculator.get_calories_remained())
# print(cash_calculator.get_today_cash_remained("eur"))

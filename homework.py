import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, entry):
        self.records.append(entry)

    def get_today_stats(self):
        now = dt.datetime.now().date()
        total_amount = 0

        for data in self.records:
            if data.date == now:
                total_amount += data.amount
            else:
                pass
        return total_amount

    def get_week_stats(self):
        now = dt.datetime.now().date()
        tomorrow = now + dt.timedelta(days=1)
        last_get_week = now - dt.timedelta(days=7)

        week_amount = 0
        for data in self.records:
            if last_get_week < data.date < tomorrow:
                week_amount += data.amount
            else:
                pass
        return week_amount


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()
        self.comment = comment


class CaloriesCalculator(Calculator):
    def get_today_stats(self):
        return Calculator.get_today_stats(self)

    def get_calories_remained(self):
        result = CaloriesCalculator.get_today_stats(self)
        total = self.limit - result
        if total > 0:
            answer = f"Сегодня можно съесть что-нибудь ещё," \
                f" но с общей калорийностью не более {total} кКал"
        else:
            answer = "Хватит есть!"
        return answer


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
        result = CashCalculator.get_today_stats(self)
        convert = 0
        if self.currency == "usd":
            convert = (self.limit - result) / CashCalculator.USD_RATE
            self.currency = "USD"
        elif self.currency == "eur":
            convert = (self.limit - result) / CashCalculator.EURO_RATE
            self.currency = "Euro"
        elif self.currency == "rub":
            convert = (self.limit - result)
            self.currency = "руб"
        if (self.limit - result) == 0:
            answer = "Денег нет, держись"
        elif (self.limit - result) > 0:
            answer = f"На сегодня осталось" \
                f" {abs(round(convert, 2))} {self.currency}"
        else:
            answer = f"Денег нет, держись: твой долг" \
                f" - {abs(round(convert, 2))} {self.currency}"
        return answer

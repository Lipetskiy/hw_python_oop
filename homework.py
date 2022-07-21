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
        return total_amount

    def get_week_stats(self):
        now = dt.datetime.now().date()
        tomorrow = now + dt.timedelta(days=1)
        last_get_week = now - dt.timedelta(days=7)

        week_amount = 0
        for data in self.records:
            if last_get_week < data.date < tomorrow:
                week_amount += data.amount
        return week_amount


class Record:
    def __init__(self, amount, comment, date=dt.datetime.today()):
        self.amount = amount
        if isinstance(date, str):
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()
        else:
            self.date = dt.datetime.now().date()
        self.comment = comment


class CaloriesCalculator(Calculator):
    def get_today_stats(self):
        return Calculator.get_today_stats(self)

    def get_calories_remained(self):
        result = CaloriesCalculator.get_today_stats(self)
        total = self.limit - result
        if total > 0:
            return (f"Сегодня можно съесть что-нибудь ещё,"
                    f" но с общей калорийностью не более {total} кКал")
        return "Хватит есть!"


class CashCalculator(Calculator):
    USD_RATE = 75.11
    EURO_RATE = 90.11

    def __init__(self, limit):
        super().__init__(limit)
        self.currency = "руб"

    def get_today_stats(self):
        return Calculator.get_today_stats(self)

    def get_today_cash_remained(self, currency):
        result = CashCalculator.get_today_stats(self)
        total = self.limit - result

        currency_dictionary = {
            'usd': f'{abs(round(total / CashCalculator.USD_RATE, 2))} USD',
            'eur': f'{abs(round(total / CashCalculator.EURO_RATE, 2))} Euro',
            'rub': f'{abs(round(total, 2))} руб'}

        if total == 0:
            return "Денег нет, держись"
        elif total > 0:
            return (f"На сегодня осталось"
                    f" {currency_dictionary[currency].format(total)}")
        else:
            return (f"Денег нет, держись: твой долг"
                    f" - {currency_dictionary[currency].format(total)}")

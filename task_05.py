import datetime

class Date:
    current_datetime = datetime.datetime.now()

    def check_value(self, number_day):
        if type(number_day) != int:
            number_day = int(number_day)

        number_day_in_future = self.current_datetime + datetime.timedelta(days=number_day)
        return number_day_in_future

    def formatted_current_date(self):
        return self.current_datetime.strftime("%d-%m-%Y %H:%M:%S")

    def date_in_future(self, number_day = None):
        if number_day == None:
            return self.formatted_current_date()

        if number_day == []:
            return self.formatted_current_date()

        return self.check_value(number_day).strftime("%d-%m-%Y %H:%M:%S")


def tests():
    test = Date()
    print(test.date_in_future([]))  # => текущая дата
    print(test.date_in_future(2))  # => текущая дата + 2 дня


tests()

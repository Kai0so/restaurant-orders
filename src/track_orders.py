from .analyze_log import (
    get_ordered_meals,
    get_all_meals,
    get_all_days,
    get_order_days
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        order = [customer, order, day]
        self.orders.append(order)

    def get_most_ordered_dish_per_customer(self, customer):
        ordered_meals = get_ordered_meals(self.orders, customer)
        frequency = dict()
        most_frequent_meal = ordered_meals[0]
        for meal in ordered_meals:
            if meal not in frequency:
                frequency[meal] = 1
        else:
            frequency[meal] += 1
        if frequency[meal] > frequency[most_frequent_meal]:
            most_frequent_meal = meal
        return most_frequent_meal

    def get_never_ordered_per_customer(self, customer):
        all_meals = get_all_meals(self.orders)
        ordered_meals = get_ordered_meals(self.orders, customer)
        for meal in ordered_meals:
            if meal in all_meals:
                del all_meals[meal]
        meals_never_ask = set()
        for meal in all_meals.keys():
            meals_never_ask.add(meal)
        return meals_never_ask

    def get_days_never_visited_per_customer(self, customer):
        all_days = get_all_days(self.orders)
        order_days = get_order_days(self.orders, customer)
        for day in order_days:
            if day in all_days:
                del all_days[day]
        days_never_ordered = set()
        for day in all_days.keys():
            days_never_ordered.add(day)
        return days_never_ordered

    def get_busiest_day(self):
        frequency = dict()
        most_busiest_day = self.orders[0][2]
        for order in self.orders:
            if order[2] not in frequency:
                frequency[order[2]] = 1
            else:
                frequency[order[2]] += 1
            if frequency[order[2]] > frequency[most_busiest_day]:
                most_busiest_day = order[2]
        return most_busiest_day

    def get_least_busy_day(self):
        frequency = dict()
        least_busiest_day = self.orders[0][2]
        for order in self.orders:
            if order[2] not in frequency:
                frequency[order[2]] = 1
            else:
                frequency[order[2]] += 1
            if frequency[order[2]] < frequency[least_busiest_day]:
                least_busiest_day = order[2]
        return least_busiest_day

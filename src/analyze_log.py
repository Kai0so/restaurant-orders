import csv


def analyze_log(path_to_file):
    csv_data = csv_importer(path_to_file)
    get_maria_orders = get_ordered_meals(csv_data, "maria")
    get_maria_favorite_meal = maria_favorite_meal(get_maria_orders)
    get_arnaldo_orders = get_ordered_meals(csv_data, "arnaldo")
    get_arnaldo_hamburguer_orders = arnaldo_hamburguer_orders(
        get_arnaldo_orders)
    get_meals = get_all_meals(csv_data)
    get_joao_orders = get_ordered_meals(csv_data, "joao")
    get_meals_joao_never_ask = meals_joao_never_ask(get_joao_orders, get_meals)
    get_days = get_all_days(csv_data)
    get_joao_order_days = get_order_days(csv_data, "joao")
    get_days_joao_never_ordered = days_joao_never_ordered(
        get_joao_order_days, get_days)
    f = open("data/mkt_campaign.txt", "w")
    f.write(
        f"{get_maria_favorite_meal}\n"
        f"{get_arnaldo_hamburguer_orders}\n"
        f"{get_meals_joao_never_ask}\n"
        f"{get_days_joao_never_ordered}"
    )
    f.close()


def csv_importer(path):
    if path.endswith(".csv") is not True:
        raise FileNotFoundError(f"Extensão inválida: {path}")
    try:
        with open(path, encoding="utf8") as file:
            file_reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = file_reader
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path}")


def get_ordered_meals(all_orders, name):
    ordered_meals = []
    for order in all_orders:
        if order[0] == name:
            ordered_meals.append(order[1])
    return ordered_meals


def get_order_days(all_orders, name):
    order_days = []
    for order in all_orders:
        if order[0] == name:
            order_days.append(order[2])
    return order_days


def get_all_meals(all_orders):
    all_meals_dict = dict()
    for order in all_orders:
        if order[1] not in all_meals_dict:
            all_meals_dict[order[1]] = ""
    return all_meals_dict


def get_all_days(all_orders):
    all_days_dict = dict()
    for order in all_orders:
        if order[2] not in all_days_dict:
            all_days_dict[order[2]] = ""
    return all_days_dict


def maria_favorite_meal(maria_orders):
    frequency = dict()
    most_frequent_meal = maria_orders[0]
    for meal in maria_orders:
        if meal not in frequency:
            frequency[meal] = 1
        else:
            frequency[meal] += 1
        if frequency[meal] > frequency[most_frequent_meal]:
            most_frequent_meal = meal
    return most_frequent_meal


def arnaldo_hamburguer_orders(arnaldo_orders):
    hamburguer_orders = 0
    for meal in arnaldo_orders:
        if meal == "hamburguer":
            hamburguer_orders += 1
    return str(hamburguer_orders)


def meals_joao_never_ask(joao_orders, all_meals):
    for meal in joao_orders:
        if meal in all_meals:
            del all_meals[meal]
    meals_never_ask = set()
    for meal in all_meals.keys():
        meals_never_ask.add(meal)
    return meals_never_ask


def days_joao_never_ordered(joao_order_days, all_days):
    for day in joao_order_days:
        if day in all_days:
            del all_days[day]
    days_never_ordered = set()
    for day in all_days.keys():
        days_never_ordered.add(day)
    return days_never_ordered

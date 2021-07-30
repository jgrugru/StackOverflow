# import pycraigslist

# miatas = pycraigslist.forsale.cta(site="sfbay", area="eby", query="Mazda Miata")
# for miata in miatas.search():
#     print(miata)

# import pycraigslist

# bike_filters = {
#     'posted_today': True,
#     'bundle_duplicates': True,
#     'make': 'Harley',
#     'model': 'Softail'
# }

# bikes = pycraigslist.forsale.mca(site='miami', area='brw', filters=bike_filters)

# for bike in bikes.search(limit=5):
#     print(bike)

# from re import search
# from ifcollector import ifandstatement
# from ifcollector import iforstatement

# def matches_email_regex(value):
#     match_object = search(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
#                           value)
#     return bool(match_object)

# is_valid_gmail = [
#     "len(value) > 5",
#     "'@' in value",
#     matches_email_regex,
#     "'gmail.com' in value",
#     lambda value: bool(search(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
#                               value))
# ]

# my_email = "jeff.gruenbaum@gmail.com"

# if ifandstatement(my_email, *is_valid_gmail):
#     print("The email is valid!")


from ifcollector import ifandstatement


def add_digits(n):
    sum = 0
    for digit in str(n):
        sum += abs(int(digit))
    return sum

def do_digits_add_up_to_10(n):
    return add_digits(n) == 10

is_valid_input = [
    "value in range(0, 100)",
    do_digits_add_up_to_10,
    lambda value: int(str(value)[0]) % 2 == 1  # is the first digit odd?
]

if ifandstatement(73, *is_valid_input):
    print("The input is valid!")
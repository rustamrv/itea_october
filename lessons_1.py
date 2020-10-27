
def print_list():
    print("1. List :")
    for i in range(0, 10, 1):
        print(i)


def country():
    country_list = ['Ukraine', 'Belarus', 'Russia', 'USA']
    country_dict = {
        'Ukraine': 'Kiev',
        'Belarus': 'Minsk',
        'USA': 'Washington'
    }
    print("2. Dict and list: ")
    for i in country_list:
        if i in country_dict:
            print(country_dict[i])


def fizz_buzz():
    print('3. FizzBuzz ')
    for i in range(0, 100):
        if i % 15 == 0:
            print("FizzBuzz", i)
        elif i % 5 == 0:
            print('Buzz', i)
        elif i % 3 == 0:
            print("Fizz", i)


def bank(sum_dep, years, procent):
    print('4. Bank')
    sum_all = 0
    for i in range(0, years):
        sum_dep = sum_dep + sum_dep*procent/100
        sum_all = sum_dep + sum_dep
    print(sum_all)


if __name__ == "__main__":
    print_list()
    country()
    fizz_buzz()
    bank(1000, 1, 15)
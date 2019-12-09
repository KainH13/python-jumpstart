
def main():
    print_the_header()

    code = input("What zipcode do you want the weather for? ")

    # get html from web
    print(code)
    # parse html
    # display for the forecast


def print_the_header():
    print('---------------------------------------')
    print('             WEATHER APP')
    print('---------------------------------------')
    print()


if __name__ == '__main__':
    main()
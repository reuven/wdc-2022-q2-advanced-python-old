def menu(*args):
    while True:
        user_choice = input(f'Choose from: {"/".join(args)}').strip()

        if user_choice in args:
            return user_choice

        print(f'{user_choice} is not valid; try again')


if __name__ == '__main__':
    print('Example menu!')
    user_choice = menu('a', 'b', 'c', 'd')
    print(f'You chose {user_choice}!')

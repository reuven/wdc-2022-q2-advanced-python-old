def menu(*args):
    while True:
        user_choice = input(f'Choose from: {"/".join(args)}').strip()

        if user_choice in args:
            return user_choice

        print(f'{user_choice} is not valid; try again')

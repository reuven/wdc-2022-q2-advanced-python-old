def menu(*args):

    user_choice = input(f'Choose from: {args}').strip()

    if user_choice in args:
        return user_choice

    print(f'{user_choice} is not valid; try again')

def main():
    import random
    dice_roll = int(input('How many dices would you like to roll?'))
    dice_size = int(input('What is the size of the dice?'))
    dice_sum = 0
    for i in range(0, dice_roll):
        roll = random.randint(0, dice_size)
        dice_sum += roll
        if roll == 1:
            print(f'You rolled a {roll}!critical fail')
        elif roll == 6:
            print(f'You rolled a {roll}! critical sucess')
        else:
            print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')


if __name__ == "__main__":
    main()

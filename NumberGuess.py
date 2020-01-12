"""This is to roll a dice, total it and compare it to the estimate of the player, thereby determining the winner"""
from random import randint
from time import sleep
def get_user_guess():
  guess = int(raw_input('What\'s your guess?: '))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print 'The maximum value obtainable is %d' % (max_val)
  guess = get_user_guess()
  if guess > max_val:
    print 'Your value is invalid'
  else:
    print 'Rolling...'
    sleep(2)
    print 'The first roll is %d' % (first_roll)
    sleep(1)
    print 'The second rolls is %d' % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print 'Result...'
    sleep(1)
    if guess == total_roll:
        print 'Congrats! You\'re correct'
    else:
        print 'Oops! You\'re incorrect'
        
roll_dice(7)
"""In case, you're too sleepy or my product is too ugly for you to understand, this is a calendar."""

from time import sleep, strftime
user_first_name = 'Asa'
calendar = {}
def welcome():
  print 'Yo, ' + user_first_name + ', glad you\'re back'
  print 'We\'re turning this thang on!'
  sleep(1)
  print 'Today is: ' + strftime('%A %B %d, %Y,')
  print 'Time is ' + strftime('%H:%M:%S')
  print 'What would you like to do?'
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input('Enter A to Add, U to Update, V to View, D to Delete, X to Exit')
    user_chooice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print 'Your calendar\'s empty'
      else:
        print calendar
    elif user_choice == 'U':
      date = raw_input('What date?: ')
      update = raw_input('Enter the update: ')
      calendar[date] = update
      print 'Update successful'
      print calendar
    elif user_choice == 'A':
      event = raw_input('Enter a new event: ')
      date = raw_input('Enter date (MM/DD/YYYY): ')
      if len(date) > 10 or int(date[6:]) < int(strftime('%Y')):
        print 'You entered an invalid date!'
        try_again = raw_input('Try again? Y for Yes, N for No')
        try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calendar[date] = event
    elif user_choice == 'D':
      if len(calendar.key()) < 1:
        print 'The calendar is already empty'
      else:
        event = raw_input('What we tryna get rid of?: ')
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print 'The event has been cleared'
            print calendar
          else:
            print 'Uh, not sure about that'
    elif user_choice == 'X':
      start = False
    else:
      print 'Yeah, I don\'t recognise that'
      start = False
          
start_calendar()

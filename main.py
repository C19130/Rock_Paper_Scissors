import random


#functions go here
def check_rounds():
  while True:
    response = input("How many rounds: ")

    round_error = "Please type either <enter> " \
     "or an integer that is more than 0"
    if response != "":
      try:
        response = int(response)

        if response <1:
          print(round_error)
          continue

      except ValueError:
        print(round_error)
        continue

    return response

def choice_checker(question, valid_list, error):

  valid = False
  while not valid:

    #ask user for choice
    response = input(question).lower()

    for item in valid_list:
      if response == item[0] or response == item:
        return item

    #output error if item not in list
    print(error)
    print()


#main routine goes here

#lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

rounds_played = 0
choose_instruction = "Please choose rock (r), paper "\
"(p) or scissors (s)"
# Main routine goes here...

rounds_played = 0
choose_instruction = "Please choose rock (r), paper "\
"(p) or scissors (s)"

#ask user for # rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":


  #rounds heading
  print()
  if rounds == "":
    heading = "Continuous Mode: " \
    "Round {} of ".format(rounds_played + 1)
  else:
    heading = "Round {} of "\
    "{}".format(rounds_played + 1, rounds)

  print(heading)

  choose_error = "Please choose from rock " \
  "paper / scissors (or 'xxx' to quit)"

  #ask user for choice and check it's valid
  choose = choice_checker(choose_instruction, rps_list, choose_error)
  
  # End game if exit code is typed
  if choose == "xxx":
    break

  #  **** rest of loop / game ****
  print("you chose {}".format(choose))

  rounds_played += 1

  #end game if requested # of rounds have been played
  if rounds_played == rounds:
    break

print("Thank you for playing")




#Ask user if they have played before.
#if 'no', show instructions


#ask user for # of rounds then loop...

#ask user if they want to see their game history.
#if 'yes' show game history
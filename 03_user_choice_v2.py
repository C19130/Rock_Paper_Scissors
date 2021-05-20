# version 2 - checks the ersponse is in  given list



#Functions go here
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

#lists for checking purposes
rps_list = ["rock", "paper", "scissors", "xxx"]

#looping for testin purposes
user_choice = ""
while user_choice != "xxx":

  #ask user for choice and check it's valid
  user_choice = choice_checker("Choose Rock / Paper /  Scissors (r/p/s): ", rps_list, "Please choose from rock / paper/ scissors (or xxx to quit)" )

  # print out choice for comparison purposes
  print("You Chose {}".format(user_choice))
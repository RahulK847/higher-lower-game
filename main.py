from replit import clear
from art import logo, vs 
from game_data import data
import random
def get_random_acc():
  """Return random account"""
  return random.choice(data)

def info(account):
  """Give details of a give account in formated string"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country} "
def check_ans(guess,a_follower,b_follower):
  if a_follower>b_follower:
    return guess=="a"
  else:
   return guess=="b"

def Game():
  scores=0
  a_account = get_random_acc()
  b_account = get_random_acc()
  while True:
    a_account = b_account
    b_account = get_random_acc()

    a_follower = a_account["follower_count"]
    b_follower = b_account["follower_count"]

    print(f"Canpare A: {info(a_account)}")
    print(vs)
    print(f"Against B: {info(b_account)}")

    guess=input("Who have more followers? Type 'A' or 'B': ").lower()
    
    is_corrent= check_ans(guess,a_follower,b_follower)
    
    print(is_corrent)
    if is_corrent:
      scores+=1
      clear()
      print(logo)
      print(f"You're right! Current score: {scores}.")
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {scores}")
      scores=0
      break
while True:
  clear()
  print(logo)
  Game()
  if input("Do you want to play again? Y or N?: ").lower()=="n":
    break
  
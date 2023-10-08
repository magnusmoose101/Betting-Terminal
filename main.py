import time
import json
import os
import hashlib
import random
import colorama
from colorama import Fore

def Print(string):
  print(Fore.GREEN + "~/ ", end="")
  for i in string:
    time.sleep(0.05)
    print(i, end="", flush=True)
  print("")
    
Print(Fore.GREEN + "Welcome to the hacking terminal.")
Print(Fore.GREEN + "Do you have an account?")
Print(Fore.GREEN + "  1) Yes")
Print(Fore.GREEN + "  2) No")

accountOrNot = str(input(Fore.YELLOW + "~/ "))

while True:
  if accountOrNot == "1" or accountOrNot.lower() == "yes":
    Print(Fore.GREEN + "Username:")
    username = str(input(Fore.YELLOW + "~/ "))
    Print(Fore.GREEN + "Password:")
    password = str(input(Fore.YELLOW + "~/ "))
  
    if os.path.exists("sessions/" + username + ".json"):
      with open("sessions/" + username + ".json") as openJsonReadable:
        user = json.load(openJsonReadable)
    
      if user["password"] == hashlib.sha256(password.encode()).hexdigest():
        Print(Fore.GREEN + "You're succesfully logged in.")
        loggedIn = True
        break
      else:
        Print(Fore.GREEN + "Your username or password is incorrect.")
        loggedIn = False
        break
    else:
      Print(Fore.GREEN + "Your username or password is incorrect.")
      loggedIn = False
      break
  elif accountOrNot == "2" or accountOrNot.lower() == "no":
    Print(Fore.GREEN + "Username:")
    username = str(input(Fore.YELLOW + "~/ "))
    Print(Fore.GREEN + "Password:")
    password = str(input(Fore.YELLOW + "~/ "))
    Print(Fore.GREEN + "First name:")
    firstName = str(input(Fore.YELLOW + "~/ "))
    Print(Fore.GREEN + "Last name:")
    lastName = str(input(Fore.YELLOW + "~/ "))
  
    if os.path.exists("sessions/" + username + ".json") == False:
      user = {"username": username, "password": hashlib.sha256(password.encode()).hexdigest(), "firstName": firstName.lower(), "lastName": lastName.lower()}
      
      with open("sessions/" + username + ".json", "w") as openJsonWritable:
        json.dump(user, openJsonWritable, indent=2)

      with open("users.json", "r") as openJsonReadable:
        usernames = json.load(openJsonReadable)

      usernames.append(username)
      
      with open("users.json", "w") as openJsonWritable:
        json.dump(usernames, openJsonWritable, indent=2)
        
      loggedIn = True
      break
    else:
      Print(Fore.GREEN + "This account already exists.")
      loggedIn = False
      break
  else:
    Print(Fore.GREEN + "That isn't an option.")
    Print(Fore.GREEN + "Do you have an account?")
    Print(Fore.GREEN + "  1) Yes")
    Print(Fore.GREEN + "  2) No")
    accountOrNot = str(input(Fore.YELLOW + "~/ "))

Print(Fore.GREEN + "")
Print(Fore.GREEN + "Searching for opponent.")

with open("users.json", "r") as openJsonReadable:
  usernames = json.load(openJsonReadable)

usernamesLength = len(usernames) - 1
userNumber = random.randint(0, usernamesLength)
user = usernames[userNumber]

with open("sessions/" + user + ".json", "r") as openJsonReadable:
  userFile = json.load(openJsonReadable)

Print(Fore.GREEN + "Scanning network.")
Print(Fore.GREEN + "Opponent found.")
Print(Fore.GREEN + "Opponent: " + userFile["username"])
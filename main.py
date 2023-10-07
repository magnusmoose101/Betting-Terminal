import time
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


  
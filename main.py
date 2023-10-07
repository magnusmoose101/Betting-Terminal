import time
import colorama
from colorama import Fore

def Print(string):
  for i in string:
    time.sleep(0.05)
    print(i, end="", flush=True)
    
Print(Fore.GREEN + "Hi my name is Magnus")
import time

def Print(string):
  for i in string:
    time.sleep(0.05)
    print(i, end="", flush=True)

Print("Hi my name is Magnus")
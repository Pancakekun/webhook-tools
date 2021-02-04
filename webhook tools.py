import requests
import time
import json
from tqdm import tqdm
for i in tqdm(range(10)):
    time.sleep(0.1)

print("Made by Pancakes#4891")
time.sleep(1)
print('''╦ ╦┌─┐┌┐ ┬ ┬┌─┐┌─┐┬┌─  ┌┬┐┌─┐┌─┐┬  ┌─┐
║║║├┤ ├┴┐├─┤│ ││ │├┴┐   │ │ ││ ││  └─┐
╚╩╝└─┘└─┘┴ ┴└─┘└─┘┴ ┴   ┴ └─┘└─┘┴─┘└─┘
''')

def main():
  a = input('''
  [1] webhook spammer
  [2] webhook deleter
  ==> ''')

  if a == "1":
    webhook = input("webhook to spam: ")
    message = input("message to spam: ")
    amount = int(input("amount to spam: "))
    wait = float(input("delay: "))
    hook = webhook

    headers = {"content-type": "application/json"}
    data = {"content": message}
    for x in range(amount):
      time.sleep(wait)
      requests.post(hook, json=data,headers=headers)
      main()

  if a == "2":
    print("made by Pancakes\n")
    webhookdelete = input("what is the webhook?\n") 
    requests.delete(webhookdelete)
    print("webhook has been deleted!\n") 
    main()

if __name__ == "__main__":
  main()

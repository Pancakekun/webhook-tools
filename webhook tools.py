import requests
import time
import json
from tqdm import tqdm
for i in tqdm(range(10)):
    time.sleep(0.1)

print('''Made by Pancakes#4891
and laika#9603''')
time.sleep(1)
print('''╦ ╦┌─┐┌┐ ┬ ┬┌─┐┌─┐┬┌─  ┌┬┐┌─┐┌─┐┬  ┌─┐
║║║├┤ ├┴┐├─┤│ ││ │├┴┐   │ │ ││ ││  └─┐
╚╩╝└─┘└─┘┴ ┴└─┘└─┘┴ ┴   ┴ └─┘└─┘┴─┘└─┘
''')

def main():
    a = input('''
    [1] webhook spammer
    [2] webhook deleter
    [3] dump webhook info
    [4] edit webhook
    [5] 
    ==> ''')

    if a == "1":
        webhook = input("webhook to spam: ")
        message = input("message to spam: ")
        amount = int(input("amount to spam: "))
        wait = float(input("delay: "))
        hook = webhook

        headers = {"content-type": "application/json"}
        data = {"content": message}
        time.sleep(wait)
        for x in range(amount):
            r = requests.post(hook, json=data,headers=headers)
            print("done sending",amount,"messages")
            if r.status_code == 200:
              print("sent message successfully")
        main()

    if a == "2":
        print("made by Pancakes\n")
        webhookdelete = input("what is the webhook?\n") 
        requests.delete(webhookdelete)
        print("webhook has been deleted!\n") 
        main()

    if a == "3":
        hook1 = input("webhook: ")
        r = requests.get(hook1)
        print(r.content)
        main()
        
    if a == "4":
      hook = input("webhook: ")
      wbname = input("name: ")
      requests.patch(hook, json={"name": wbname})
      print("succsesfully changed webhook name to: ",wbname)
      main()

      

      
if __name__ == "__main__":
  main()

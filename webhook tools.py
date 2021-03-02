import requests, time, json

print("Made by Pancakes#4891\nand laika#9603")

time.sleep(1)

print('''╦ ╦┌─┐┌┐ ┬ ┬┌─┐┌─┐┬┌─  ┌┬┐┌─┐┌─┐┬  ┌─┐
║║║├┤ ├┴┐├─┤│ ││ │├┴┐   │ │ ││ ││  └─┐
╚╩╝└─┘└─┘┴ ┴└─┘└─┘┴ ┴   ┴ └─┘└─┘┴─┘└─┘
''')

def main():
    while True:
        option = input('''
        [1] webhook spammer
        [2] webhook deleter
        [3] dump webhook info
        [4] edit webhook
        [5] 
        ==> ''')
        hook = input("webhook: ")
        
        if option == "1":
            message = input("message to spam: ")
            amount = int(input("amount to spam: "))
            wait = float(input("delay: "))

            headers = {"content-type": "application/json"}
            data = {"content": message}
            time.sleep(wait)

            for _ in range(amount):
                r = requests.post(hook, json=data,headers=headers)
                print("done sending",amount,"messages")
                
                if r.status_code == 200:
                    print("sent message successfully")

        if option == "2":
            requests.delete(hook)
            print("webhook has been deleted!\n") 

        if option == "3":
            r = requests.get(hook)
            print(r.content)
                
        if option == "4":
            wbname = input("name: ")
            requests.patch(hook, json={"name": wbname})
            print("succsesfully changed webhook name to: ",wbname)

if __name__ == "__main__":
  main()

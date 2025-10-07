import threading
import time


def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(1)


def brew_tea():
    for i in range(1, 4):
        print(f"Brewing tea for #{i}")
        time.sleep(2)


order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_tea)

order_thread.start()
brew_thread.start()

order_thread.join()
brew_thread.join()

print(f"All orders taken and tea brew")

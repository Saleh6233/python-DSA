from multiprocessing import Process
import time


def brew_tea(name):
    print(f"start of {name} tea brewing")

    time.sleep(3)

    print(f"End of {name} tea brewing")


if __name__ == "__main__":

    tea_makers = [
        Process(target=brew_tea, args=(f"Tea maker #{i+1}", ))
        for i in range(3)
    ]

    for p in tea_makers:
        p.start()

    for p in tea_makers:
        p.join()

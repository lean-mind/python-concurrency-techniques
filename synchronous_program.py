import colorama
import time
from datetime import datetime


def main():
    start_time = datetime.now()
    print(f"{colorama.Fore.GREEN} -> Program started")
    print(f"{colorama.Fore.GREEN} -> first task result = ", first_task())
    print(f"{colorama.Fore.GREEN} -> second task result = ", second_task())
    print(f"{colorama.Fore.GREEN} -> Program ended")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))


def first_task():
    addition = 0
    for i in range(5):
        print(f"{colorama.Fore.RED} -> [{i}] - running the first task")
        addition += i
        time.sleep(1)
    return addition


def second_task():
    addition = 0
    for i in range(4):
        print(f"{colorama.Fore.CYAN} -> [{i}] -  running the second task")
        addition += i
        time.sleep(1)
    return addition


if __name__ == '__main__':
    main()

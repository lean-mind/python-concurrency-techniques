import colorama
import asyncio
from datetime import datetime


def main():
    start_time = datetime.now()
    print(f"{colorama.Fore.GREEN} -> Program started")
    tasks = gather_tasks()
    result = asyncio.run(tasks)
    print(f"{colorama.Fore.GREEN} -> First task result = ", result[0])
    print(f"{colorama.Fore.GREEN} -> Second task result = ", result[1])
    print(f"{colorama.Fore.GREEN} -> Program ended")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))


async def gather_tasks():
    tasks = await asyncio.gather(first_task(), second_task())
    return tasks


async def first_task():
    addition = 0
    for i in range(5):
        print(f"{colorama.Fore.RED} -> [{i}] - Running the first task")
        addition += i
        await asyncio.sleep(1)
    return addition


async def second_task():
    addition = 0
    for i in range(4):
        print(f"{colorama.Fore.CYAN} -> [{i}] - Running the second task")
        addition += i
        await asyncio.sleep(1)
    return addition


if __name__ == '__main__':
    main()

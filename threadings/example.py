import threading as th
import time

def task(name, delay):
    print(f"thread: {name}")
    for i in range(3):
        time.sleep(delay)

        print(f"thread: {name} executing task {i + 1}")
        print(f"thread: {name} ending...")


t1 = th.Thread(target=task, args=('Thread 01', 1))
t2 = th.Thread(target=task, args=('Thread 02', 4))

t1.start()
t2.start()

print(f"Threads booting...")

t1.join()
t2.join()
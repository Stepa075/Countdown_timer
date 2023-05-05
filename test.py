import time

timer = 30
for k in range(timer):
    time.sleep(1)
    print(timer)
    timer -= 1
    if timer == 0:
        break

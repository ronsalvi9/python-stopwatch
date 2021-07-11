import time

print("Press ENTER to begin")
print("Press ENTER again to start the stopwatch.")
print("Press Ctrl-c to quit.")
input()

print("Started.")
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time()-lastTime, 2)
        totalTime = round(time.time()-startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap


except KeyboardInterrupt:
    print('\Done.')

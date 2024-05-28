import time
import random

while True:
    time.sleep(1)
    f = open("Request.txt", "r")
    read_text = f.readline()

    # change from Raul Preciado
    # I commented out the line below so that it doesn't keep
    # printing blank lines as it scans for a reqest.

   # print(read_text)
    f.close()

    if read_text == "Send a number":
        value = random.randint(1, 10)
        print(value)
        f = open("Request.txt", "w")
        f.write(str(value))
    f.close()

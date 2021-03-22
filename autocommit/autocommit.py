import schedule
import time
import os
import uuid

def genrandom():
    rnd = str(uuid.uuid4())
    return rnd

def operation():
    print("running operation!")
    with open("random","w+") as f:
        f.write(genrandom)
    os.system("bash autocommit.sh")

schedule.every(15).minutes.do(operation)

while True:
    schedule.run_pending()
    time.sleep(59)

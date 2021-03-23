import uuid

def genrandom():
    rnd = str(uuid.uuid4())
    return rnd

def operation():
    with open("random","w+") as f:
        f.write(genrandom)

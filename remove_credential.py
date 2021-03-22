import os
os.system('bash -c "cat ~/.git-credentials"')
target = input("provide the keyword to remove credentials:\n")
import random
rnd = random.choice(list(range(1000)))
rnd = std(rnd)
rnd = "tmp_script{}.sh".format(rnd)
with open(rnd,"w+") as f:
    f.write('sed -i "/{}/d" ~/.git-credentials"'.format(target))
os.system("bash {}".format(rnd))
os,remove(rnd)

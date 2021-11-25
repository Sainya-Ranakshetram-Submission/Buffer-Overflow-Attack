# Buffer Overflow Attack
### Problem Statement
Buffer Overflow is a common vulnerability in applications which allows hackers to exploit the system using unsanitised input. The given application is known to have buffer overflow vulnerability. Develop an executable code snippet to crash the given application using Buffer Overflow vulnerability. No payload is required for the application.

## Solution
```
Flag: In line 16 "arr[i]= arr_num;" This could lead to potential memory clogging
```
I was given a c++ file under the [question.cpp](https://github.com/Sainya-Ranakshetram-Submission/Buffer-Overflow-Attack/blob/master/question.cpp) and it was stated it had a Buffer Overflow Attack vulnerability, and I was to create a application in order to crash that application.

So I made [application_crasher.py](https://github.com/Sainya-Ranakshetram-Submission/Buffer-Overflow-Attack/blob/master/application_crasher.py) which is written in `python3.8` in order to crash that [question.cpp](https://github.com/Sainya-Ranakshetram-Submission/Buffer-Overflow-Attack/blob/master/question.cpp).
The [application_crasher.py](https://github.com/Sainya-Ranakshetram-Submission/Buffer-Overflow-Attack/blob/master/application_crasher.py) just communicate with console and since [question.cpp](https://github.com/Sainya-Ranakshetram-Submission/Buffer-Overflow-Attack/blob/master/question.cpp) just needed a random number so the [application_crasher.py](https://github.com/Sainya-Ranakshetram-Submission/Buffer-Overflow-Attack/blob/master/application_crasher.py) just give a random number to console whenever there is a activity in the console.

Thus for [application_crasher.py](https://github.com/Sainya-Ranakshetram-Submission/Buffer-Overflow-Attack/blob/master/application_crasher.py) to work, just run
```console
python application_crasher.py
```

## Youtube Video Explaining all

[![Buffer Overflow Attack Challenge | Submission](http://img.youtube.com/vi/_au5GWGmick/0.jpg)](http://www.youtube.com/watch?v=_au5GWGmick "Buffer Overflow Attack | Submission")

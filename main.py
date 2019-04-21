import interpreter
import path_finder
import server
import time

interpreter = interpreter.Interpreter()
#srv = server.Server(interpreter)
follow = path_finder.Path_finder(interpreter)
follow.start_automodus()

try:
    while True:
        time.sleep(4)

except KeyboardInterrupt:
    print("Stopping everything")
    interpreter.__end__()
    #srv.__end__()

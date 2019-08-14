import threading

def hello(id, times):
    for i in range(times):
        print ("hello %s time is %d\n" % (id , i))


if __name__ == "__main__":
    t = threading.Thread(target=hello, args=("hawk", 5))
    t.start()
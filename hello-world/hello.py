import sys

def hello(name):
    print("Hello", name)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        hello(str(sys.argv[1]))
    else:
        print("Wrong Usage. Must pass a name")

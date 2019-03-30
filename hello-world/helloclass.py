import sys

class HelloClass():

    def __init__(self):
        self.name = "World"

    def hello(self):
        print("Hello", self.name)

if __name__ == "__main__":
    delegate = HelloClass()

    if len(sys.argv) == 2:
        delegate.name =  str(sys.argv[1])

    delegate.hello()

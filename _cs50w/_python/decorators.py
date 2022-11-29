# Wrapping function
def annouce(f):
    def wrapper():
        print("About to run a function...")
        f()
        print("Done with the function.")
    return wrapper

@annouce
def hello():
    print("Hello, world!")

hello()

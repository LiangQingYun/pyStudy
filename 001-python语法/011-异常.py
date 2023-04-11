num_str = "hello"
try:
    num = int(num_str)
except ValueError:
    print("Cannot convert string to integer")
except TypeError:
    print("Cannot convert string to integer")
except Exception:
    print("Unknown error")
else:
    print("No error")
finally:
    print("This will always be executed")


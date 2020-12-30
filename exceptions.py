import sys

print(dir(locals()['__builtins__'])) # shows list of built in exceptions

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("Entry is:", entry)
        r = 1/int(entry)
        break
    except ValueError:
        print(sys.exc_info()[0], "occurred")
        print("Trying next entry.")
        print()
    except (TypeError, ZeroDivisionError):
        print("... no.")
        print()
print("The reciprocal of", entry, "is", r)
import sys, time

def slow_print(string_to_print):
    for letter in string_to_print:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print("")
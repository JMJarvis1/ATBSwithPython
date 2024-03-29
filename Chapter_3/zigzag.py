import time
import sys

indent = 0  # How many spaces tp indent.
indentIncreasing = True  # Whether the indentation is increasing or not.

try:
    while True:  # The main program loop.
        print("  " * indent, "*" * 8)
        time.sleep(0.1)  # Pause for 1/10th of a second.

        if indentIncreasing:
            # Increase the number of spaces
            indent += 1
            if indent == 20:
                # Change direction.
                indentIncreasing = False

        else:
            # Decrease the nmumber of spaces
            indent -= 1
            if indent == 0:
                # Change direction.
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

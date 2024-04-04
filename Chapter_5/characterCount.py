import pprint

message = "It was a cold day in April, and the clocks were striking thirteen."

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(pprint.pformat(count))

"""A program for taking in a table and displaying it
to the screen, neatly formatted."""

tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


transposed = [[row[i] for row in tableData] for i in range(len(tableData[0]))]

colWidths = [0] * len(tableData)

for index, list in enumerate(tableData):
    for word in list:
        if len(word) > colWidths[index]:
            colWidths[index] = len(word)

print()
for row in transposed:
    for index, word in enumerate(row):
        print(word.rjust(colWidths[index]), end=" ")
    print()
print()

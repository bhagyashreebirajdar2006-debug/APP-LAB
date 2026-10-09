
with open("input.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))

print("First 2 lines:")
i = 0
while i < len(lines) and i < 2:
    print(lines[i], end="")
    i = i + 1

with open("output.txt", "w") as file:
    i = 0
    while i < len(lines) and i < 2:
        file.write(lines[i])
        i = i + 1

print("\nFirst 2 lines are successfully written to output.txt")

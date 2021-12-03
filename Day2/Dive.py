text_file = open("input.txt", "r")
instructions = text_file.readlines()
text_file.close()

horizontal = 0
depth = 0
aim = 0

instructions_dict = {}
for i in range(len(instructions)):
    instructions[i].rstrip("\n")

    instructions_split = instructions[i].split(" ")

    if instructions_split[0] == "forward":
        horizontal += int(instructions_split[1])
        depth += aim * int(instructions_split[1])
    if instructions_split[0] == "up":
        aim -= int(instructions_split[1])
        # depth -= int(instructions_split[1])
    if instructions_split[0] == "down":
        # depth += int(instructions_split[1])
        aim += int(instructions_split[1])

print("horizontal", horizontal)
print("depth", depth)
print(horizontal * depth)

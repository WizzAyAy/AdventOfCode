# --- Day 1: Sonar Sweep ---
text_file = open("input.txt", "r")
depths_report = text_file.readlines()
text_file.close()

measurement_increases = 0

for index, depth in enumerate(depths_report):
    if index == 0:
        # print(depth, ", (N/A - no previous measurement)")
        continue
    if depth > depths_report[index - 1]:
        measurement_increases += 1
        # print(depth, ", (increased)")
    # else:
        # print(depth, ", (decreased)")

print("number of times depth was increasing : ", measurement_increases)

# --- Day 1: Sonar Sweep ---
depths_report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
measurement_increases = 0

for index, depth in enumerate(depths_report):
    if index == 0:
        print(depth, ", (N/A - no previous measurement)")
        continue
    if depth > depths_report[index - 1]:
        measurement_increases += 1
        print(depth, ", (increased)")
    else:
        print(depth, ", (decreased)")

print("number of times depth was increasing : ", measurement_increases)

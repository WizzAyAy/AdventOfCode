# --- Day 1: Sonar Sweep ---
text_file = open("input.txt", "r")
depths_report = (list(map(int, text_file.readlines())))
text_file.close()

measurement_increases = sum(depths_report[i] > depths_report[i - 1] for i in range(1, len(depths_report)))
measurement_increases_part_2 = 0
for i in range(len(depths_report) - 3):
    A = depths_report[i] + depths_report[i+1] + depths_report[i+2]
    B = depths_report[i+1] + depths_report[i+2] + depths_report[i+3]
    if A < B:
        measurement_increases_part_2 += 1

print("number of times depth was increasing : ", measurement_increases)
print("number of times depth was increasing part 2: ", measurement_increases_part_2)

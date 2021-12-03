def have_bit_at_position(bit, btc, index):
    return bit[index] == btc


def rating_binaries(binaries, is_oxygen):
    index = 0
    while len(binaries) > 1:
        bits_0_index = 0
        bits_1_index = 0

        for i in range(len(binaries)):
            if binaries[i][index] == "0":
                bits_0_index += 1
            if binaries[i][index] == "1":
                bits_1_index += 1

        if bits_0_index > bits_1_index:
            if is_oxygen:
                bit_to_check = "0"
            else:
                bit_to_check = "1"
        else:
            if is_oxygen:
                bit_to_check = "1"
            else:
                bit_to_check = "0"

        binaries = list(
            filter(lambda x: have_bit_at_position(x, bit_to_check, index), binaries))
        index += 1

    return binaries


def main():
    text_file = open("input.txt", "r")
    binaries = text_file.readlines()
    text_file.close()

    gamma_rate = ""
    epsilon_rate = ""

    size_bit = len(binaries[0].rstrip("\n"))

    occurrence_0 = [0 for x0 in range(size_bit)]
    occurrence_1 = [0 for x1 in range(size_bit)]

    for i in range(len(binaries)):
        binaries[i] = (binaries[i].rstrip("\n"))

    for i in range(len(binaries)):
        binary = binaries[i]
        for y in range(len(binary)):
            if binary[y] == "0":
                occurrence_0[y] += 1
            if binary[y] == "1":
                occurrence_1[y] += 1

    for i in range(size_bit):
        if occurrence_0[i] > occurrence_1[i]:
            gamma_rate = gamma_rate + "0"
            epsilon_rate = epsilon_rate + "1"
        if occurrence_0[i] < occurrence_1[i]:
            gamma_rate = gamma_rate + "1"
            epsilon_rate = epsilon_rate + "0"

    consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

    print("consumption", consumption)

    oxygen_binaries = rating_binaries(binaries, True)
    scrubber_binaries = rating_binaries(binaries, False)

    life_support_rating = int(oxygen_binaries[0], 2) * int(scrubber_binaries[0], 2)

    print("life_support_rating", life_support_rating)


main()

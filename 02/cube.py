red_max = 12
green_max = 13
blue_max = 14

def valid_round(color_splits):
    for color_split in color_splits:
        real = color_split.split()
        if real[1] == "red":
            if int(real[0]) > red_max:
                return False
        if real[1] == "green":
            if int(real[0]) > green_max:
                return False
        if real[1] == "blue":
            if int(real[0]) > blue_max:
                return False
    return True


def main():
    total = 0
    i = 1
    input_file = open("input.txt", 'r')
    line = input_file.readline()
    while line:
        game_string = line.split(':')[1]
        round_strings = game_string.split(';')
        # print(str(i) + " size = " + str(len(round_strings)))
        round_good = True
        for round_string in round_strings:
            color_splits = round_string.split(',')
            if not valid_round(color_splits):
                # print("bad" + str(i))
                round_good = False
            # else:
                # print("good" + str(i))
        if round_good:
            # print("add" + str(i))
            total += i
        line = input_file.readline()
        i += 1
    input_file.close()
    print(total)


if __name__ == "__main__":
    main()

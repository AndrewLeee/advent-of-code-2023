def replace_string_with_nums(string):
    string = string.replace('one', 'one1one')
    string = string.replace('two', 'two2two')
    string = string.replace('three', 'three3three')
    string = string.replace('four', 'four4four')
    string = string.replace('five', 'five5five')
    string = string.replace('six', 'six6six')
    string = string.replace('seven', 'seven7seven')
    string = string.replace('eight', 'eight8eight')
    string = string.replace('nine', 'nine9nine')
    return string


def main():
    calibration_value = 0

    input_file = open('input.txt', 'r')
    line = input_file.readline()
    while line:
        # remove the below line for part 1
        # leave it in for part 2
        line = replace_string_with_nums(line)
        nums = [int(i) for i in list(line) if i.isdigit()]
        calibration_value += (nums[0] * 10 + nums[len(nums) - 1])
        line = input_file.readline()
    input_file.close()

    print(calibration_value)


if __name__ == "__main__":
    main()

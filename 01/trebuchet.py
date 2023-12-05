def main():
    calibration_value = 0

    input_file = open('input.txt', 'r')
    line = input_file.readline()
    while line:
        nums = [int(i) for i in list(line) if i.isdigit()]
        calibration_value += (nums[0] * 10 + nums[len(nums) - 1])
        line = input_file.readline()
    input_file.close()

    print(calibration_value)


if __name__ == "__main__":
    main()

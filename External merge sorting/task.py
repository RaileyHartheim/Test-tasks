def read_non_empty_line(input):
    while True:
        line = input.readline()
        if line == "":
            return ""
        if line.isspace() == False:
            return line.strip()

def part_file(file, prefix, counter, lines=5):
    with open(file, 'r') as input_file:
        suffix = 0
        while True:
            with open(f"{prefix}.{suffix}.txt", 'w') as temp:
                list_part = []
                written = 0
                while written < lines:
                    data = input_file.readline()
                    if data == "":
                        break
                    list_part.append(data)
                    written += 1
                transformed_list_part = [int(item) for item in list_part]
                sorted_list = sorted(transformed_list_part)
                str_list = [str(item) for item in sorted_list]
                for item in str_list:
                    temp.write(f"{item}\n")
                if data == "":
                    break
                suffix += 1
                counter += 1
                list_part.clear()
                transformed_list_part.clear()
                sorted_list.clear()
                str_list.clear()
        return counter

counter_first = 0
counter_second = 0

first_counter = part_file('input_001.txt', 'temporary-first', counter_first)
second_counter = part_file('input_002.txt', 'temporary-second', counter_second)

def combine_sorted_files(file1, file2, output):

    read_file1, read_file2 = True, True

    with open(output,'w') as output_file:
        with open(file1,'r') as input_file1:
            with open(file2,'r') as input_file2:
                while True:
                    if read_file1:
                        line1 = read_non_empty_line(input_file1)
                    if read_file2:
                        line2 = read_non_empty_line(input_file2)

                    if line1 == "" or line2 == "":
                        break

                    read_file1, read_file2 = False, False
                    if int(line1) < int(line2):
                        smaller = line1
                        read_file1 = True
                    else:
                        smaller = line2
                        read_file2 = True

                    output_file.write(smaller+"\n")

                while line1 != "":
                    output_file.write(line1+"\n")
                    line1 = read_non_empty_line(input_file1)
                while line2 != "":
                    output_file.write(line2+"\n")
                    line2 = read_non_empty_line(input_file2)

combine_sorted_files('temporary-first.0.txt', 'temporary-first.1.txt', 'first-output_1.txt')
output_file_1 = "1"
input_file_1 = "2"
suffix = 2
while True:
    if suffix > first_counter:
        break
    else:
        if output_file_1 == "1":
            output_file_1 = "2"
            input_file_1 = "1"
        else:
            output_file_1 = "1"
            input_file_1 = "2"
        combine_sorted_files(f'temporary-first.{suffix}.txt', f'first-output_{input_file_1}.txt', f'first-output_{output_file_1}.txt')
        suffix += 1

combine_sorted_files('temporary-second.0.txt', 'temporary-second.1.txt', 'second-output_1.txt')
output_file_2 = "1"
input_file_2 = "2"
suffix = 2
while True:
    if suffix > second_counter:
        break
    else:
        if output_file_2 == "1":
            output_file_2 = "2"
            input_file_2 = "1"
        else:
            output_file_2 = "1"
            input_file_2 = "2"
        combine_sorted_files(f'temporary-second.{suffix}.txt', f'second-output_{input_file_2}.txt', f'second-output_{output_file_2}.txt')
        suffix += 1

combine_sorted_files(f'first-output_{output_file_1}.txt', f'second-output_{output_file_2}.txt', 'final-output.txt')
print("Finished. Please check it.")
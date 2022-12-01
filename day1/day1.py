def hungry_elf(calorie_file: str) -> list: #Input file is a string and output is a list
    elf_sum = 0
    cal_lst = []
    with open(calorie_file) as input_file:
        for line in input_file:
            if line != '\n':
                elf_sum += int(line)
            else:
                cal_lst.append(elf_sum)
                elf_sum = 0
    cal_lst.append(elf_sum)
    return(cal_lst)


def find_top_3_calorie_sum(elf_cals: list) -> int:
    """Take in a list of elf calories, sort, and sum the top 3."""
    elf_cals.sort(reverse=True)
    return elf_cals[0] + elf_cals[1] + elf_cals[2]



if __name__ == "__main__":
    elf_calories = hungry_elf("input.txt")
    max_calorie_elf = max(elf_calories)
    print(f"The Strongest Elf carries {max_calorie_elf} calories.")
    top_three_cals = find_top_3_calorie_sum(elf_calories)
    print(f"The top 3 elves are carrying {top_three_cals} calories.")


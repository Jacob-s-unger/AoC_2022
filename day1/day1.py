def hungry_elf(input_file: str) -> list: #Input file is a string and output is a list
    elf_sum = 0 #value for a single elf's payload
    cal_lst = [] #The list for all of the calorie values that we get from the elves
    with open(input_file) as cal_file: #open the file as cal_file
        for snack in cal_file: #FOr individual line in the cal_file
            if snack != '\n': #as long as its not a a new line character meaning a new elf 
                elf_sum += int(snack) #Add that snack to the sum for that individual elf
            else: #else, as in it is a new line character
                cal_lst.append(elf_sum) #append that value to the list of the calorie total list for all the elves
                elf_sum = 0 #reset that value
    cal_lst.append(elf_sum) #this is for the last elf in the list, cant forget him!
    return(cal_lst) #return the list of the added values

def hungriest_3(elf_cals: list) -> int: #input a list and return a int. THe inout is the list genereated in the first function
    elf_cals.sort(reverse=True) #sort the list in reverse. reverse = True will sort in descending order, meaning highest first so then we can take the index of 0,1, and 2 to grab the best three
    return elf_cals[0] + elf_cals[1] + elf_cals[2] #return those 3 added up and theres the total of the top three

if __name__ == "__main__": #main
    elf_calories = hungry_elf("input.txt") #cap the file and call the function
    max_calorie_elf = max(elf_calories) #Function on the input file
    print(f"The Strongest Elf carries {max_calorie_elf} calories.") #return input
    top_three_cals = hungriest_3(elf_calories) #functin call for top three
    print(f"The strongest 3 elves are carrying a total of {top_three_cals} calories.") #retunr top 3 input


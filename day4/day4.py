with open("input.txt") as file:
    pairs = file.readlines()


num_overlapping_pairs = 0
prt_2 = 0


for pair in pairs:
    ass1, ass2 = pair.strip().split(",")

    #Book keeping to get in a readable format. Showout to a redditor for formatting help
    ass1_start, ass1_end = map(int, ass1.split("-"))
    ass2_start, ass2_end = map(int, ass2.split("-"))

    #Part one solve to determine haw many overlaps occure
    if(ass1_start <= ass2_start and ass1_end >= ass2_end) or (ass2_start <= ass1_start and ass2_end >= ass1_end):
        num_overlapping_pairs +=1

    #part 2 solve to determine n how many assignment pairs do the ranges overlap? 
    if (ass1_start <= ass2_start <= ass1_end) or (ass2_start <= ass1_start < ass2_end) or (ass1_start <= ass2_end < ass1_end) or (ass2_start <= ass1_end <= ass2_end):
        prt_2 += 1



print(num_overlapping_pairs)
print(prt_2)
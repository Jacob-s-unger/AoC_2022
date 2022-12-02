def score(input_file: str) -> int:
    total_score = 0
    with open(input_file) as cheat_sheet: #open the file 
        s = cheat_sheet.read() #read the file 
        x = [i.split() for i in s.splitlines()] #One liner for loop to splits the characters into tokens to analyze
        
        for i in x: #for i in the split tokens, x. i is the token of the round
            them = 'ABC'.index(i[0]) #Opponents choice capture the value
            you = 'XYZ'.index(i[1]) #Your choice capture the value
            end = (you - them + 1) % 3
            
            total_score += (end * 3) + (you + 1)

    return total_score #return the total score



def outcome_guide(input_file: str) -> int:
    
    total_score = 0
    with open(input_file) as cheat_sheet: #open the file 
        s = cheat_sheet.read() #read the file 
        x = [i.split() for i in s.splitlines()] #One liner for loop to splits the characters into tokens to analyze

        for i in x: #for i in the split tokens, x. i is the token of the round
            opp = 'ABC'.index(i[0]) #Opponents choice capture the value
            end = 'XYZ'.index(i[1]) #Your choice capture the value
            you = (opp + end - 1 ) % 3 #Calculate the score from the game
            total_score += (end * 3) + (you + 1)
    return total_score


if __name__ == "__main__": #main
    final = score("input.txt") #cap the file and call the function
    print(f"Following the guide, you will end with {final} points.") #return input
    prt2 = outcome_guide("input.txt")
    print(f"Following the outcome guide, you will score {prt2} points.")
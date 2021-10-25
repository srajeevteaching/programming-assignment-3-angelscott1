# Programmer: Angel Scott
# Course: CS151, Dr. Rajeev
# Date: 10/25/21
# Programming Assignment: 3
# Program Input: Choice of Sport
# Program Inputs for Football: Completions, Passing Attempts, Passing Yards, Touchdown Passes, Interceptions
# Program Inputs for Quidditch: Goal, Snitch
# Program Inputs for Gymnast: 5 Execution Scores, Difficulty Score
# Program Outputs: Quarterback Rating, Quidditch Team Score, or Gymnast Final Score

# Define function for determining quarterback rating in American football
def football(completions, attempts, yards, touchdowns, interceptions):
    qb_rating = 100 * ((5*((completions/attempts)-0.3)) + (0.25*((yards/attempts)-3)) +
                       (20*(touchdowns/attempts)) + 2.375 - (25*(interceptions/attempts)))/6
    return qb_rating

# Define function for calculating the score for a team in a game of Quidditch
def quidditch(goal, snitch):
    if snitch == "yes":
        score = 10*goal + 30
    elif snitch == "no":
        score = 10*goal
    else:
        return "Error. Invalid answer."
    return score

# Define function for calculating the final score for a gymnast on any apparatus.
def gymnast(score1, score2, score3, score4, score5, difficulty_score):
    final_score = difficulty_score + ((score1 + score2 + score3 + score4 + score5)/5)
    return final_score

# Define main function
def main():

    # Output program purpose
    print("This program will calculate a statistic relevant to your choice of sport.")

    # Get user choice of sport
    choice_of_sport = input("Enter your choice of sport: football, quidditch, gymnast")
    choice_of_sport = choice_of_sport.strip().lower()

    # Calculations and input if user choice is football
    if choice_of_sport == "football":
        qb_completions = input("Enter the number of completions")
        qb_yards = input("Enter the number of passing yards")
        qb_touchdowns = input("Enter the number of touchdown passes")
        qb_interceptions = input("Enter the number of interceptions")
        qb_attempts = input("Enter the number of passing attempts made")
        if (qb_completions.isdigit() == False) or (qb_yards.isdigit() == False) or \
                (qb_touchdowns.isdigit() == False) or (qb_interceptions.isdigit() == False) or \
                (qb_attempts.isdigit() == False):
            print("Error. Score is 0.")
        else:
            qb_completions = int(qb_completions)
            qb_yards = int(qb_yards)
            qb_touchdowns = int(qb_touchdowns)
            qb_interceptions = int(qb_interceptions)
            qb_attempts = int(qb_attempts)
            if qb_attempts <= 0:
                print("Error. Rating is 0.")
            else:
                qb_rating = football(qb_completions, qb_attempts, qb_yards, qb_touchdowns, qb_interceptions)
                print("The rating is: %.2f"%qb_rating)
                if qb_rating >= 158.3:
                    print("The quarterback is a perfect passer")
                else:
                    print("The quarterback is not a perfect passer")

    # Calculations and input if user choice is quidditch
    elif choice_of_sport == "quidditch":
        number_of_goals = input("Enter the number of goals")
        if number_of_goals.isdigit():
            number_of_goals = int(number_of_goals)
            snitch = input("Did the team catch the snitch: yes or no")
            score = quidditch(number_of_goals, snitch)
            print("The score is:", score)
        else:
            print("Error. Score is 0.")

    # Calculations and input if user choice is gymnast
    elif choice_of_sport == "gymnast":
        execution1 = input("Enter the first execution score")
        execution2 = input("Enter the second execution score")
        execution3 = input("Enter the third execution score")
        execution4 = input("Enter the fourth execution score")
        execution5 = input("Enter the fifth execution score")
        difficulty = input("Enter the difficulty score")
        if (execution1.isdigit() == False) or (execution2.isdigit() == False) or (execution3.isdigit() == False) \
                or (execution4.isdigit() == False or (execution5.isdigit() == False) or \
                    (difficulty.isdigit() == False)):
            print("Error. Score is 0")
        else:
            execution1 = int(execution1)
            execution2 = int(execution2)
            execution3 = int(execution3)
            execution4 = int(execution4)
            execution5 = int(execution5)
            difficulty = int(difficulty)
            final_score = gymnast(execution1, execution2, execution3, execution4, execution5, difficulty)
            print("The final score is:", final_score)

    # If user choice is invalid
    else:
        print("Error. Invalid sport choice.")

# Call main function
main()

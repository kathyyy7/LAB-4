
"""""
this program allows a user three tries to guess the correct answer to the question
question = "What is the capital of California". The answer is Sacremento"

We first set max_tries = 3. Then we create a loop to iterate three times. For each iteration,
we ask for the user for the answer (user input). Then based on the answer the user gives, we check 
to see if the user input matches the answer. If so, print "Correct!", then terminate the loop with 
a break statement.

If the user could not guess the correct answer within the max_tries, then print 
"You have used up your allotment of the guesses." the print "The correct answer is 'California'.

"""""

"""""
main
    question = "What is the capital of California"
    answer = "California"
    ask(question, answer)

ask
    tries = 0
    loop three times
        increment tries
        ask user input()
        check to esee of user input is equal to answer
            if so, print "Correct" the exit loop
    if not correct
        print to the user
        print the correct answer "the correct answer is California"

main

"""""

from asyncore import loop


def main():
    question = "What is the capital of California"
    answer = "California"
    ask(question, answer, 5) 

def ask(question, answer, max_tries=3):
    tries = 0
    while tries < max_tries:
        tries += 1
        ans = input(question)
        if ans == answer:
            print("Correct!")
            break
        if ans != answer:
            print("You have used up your allotment of guess.")


main()
        
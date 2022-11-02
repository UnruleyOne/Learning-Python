# Counting duplicate words in a paragraph
# The opening of Moby Dick (Herman Melville)
test_paragraph = 'Call me Ishmael Some years ago never mind how long precisely having little or no money in my purse and nothing particular to interest me on shore I thought I would sail about a little and see the watery part of the world It is a way I have of driving off the spleen and regulating the circulation Whenever I find myself growing grim about the mouth whenever it is a damp drizzly November in my soul whenever I find myself involuntarily pausing before coffin warehouses and bringing up the rear of every funeral I meet and especially whenever my hypos get such an upper hand of me that it requires a strong moral principle to prevent me from deliberately stepping into the street and methodically knocking people’s hats off then I account it high time to get to sea as soon as I can This is my substitute for pistol and ball With a philosophical flourish Cato throws himself upon his sword I quietly take to the ship There is nothing surprising in this If they but knew it almost all men in their degree some time or other cherish very nearly the same feelings towards the ocean with me'

# Python code to convert string to list
def Convert(string):
    li = list(string.split(" "))
    return li
  
# Driver code    
#str1 = "Geeks for Geeks"
#print(Convert(str1))
# Use .count for counting duplicate words in a string
#str1.count('Geeks')
# print the test_paragraph
#list1 = test_paragraph
#print(Convert(list1))
# Use .count method for a couple of words in the paragraph to count
#print("The number of times it says 'I' in the test paragraph is:", list1.count('I'))
#list1.count('and')
#list1.count('in')

# Get user input
def get_user_input():
    '''Ask user for a sentence'''
    s1 = input("Enter a sentence:")
    s2 = Convert(s1)
    return s2
# Put all functions into main
def main():
    sentence = get_user_input()
    print(sentence)
    # Python convert code
    #sentence = Convert(s)
    #print(sentence)
# Create a Dictionary that goes in your for loop
# Create a for loop that counts number of words if they are repeated 
# Add one everytime
    for word in sentence:
        sentence = dict()
        sentence[word] += 1
    print("The number of words duplicated are:", sentence[word])
main()
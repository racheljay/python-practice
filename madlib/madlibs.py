# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to ___"

# youtuber = "Kylie Ying" #some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)

# print("subscribe to {}".format(youtuber)) #takes the value of youtuber and puts into curly braces

# print(f"subscribe to {youtuber}") #an f string makes it to where you can put the variable name directly in the curly braces

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
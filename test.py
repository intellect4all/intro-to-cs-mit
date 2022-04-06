an_letters = 'aefhilmnorsaxAEFHILMNORSXX'
word = input("I am expecting a word: Enter one: ")
times = int(input("Enthusiasm level (1-10): "))


for char in word:
    
    if char in an_letters:
        print(" Give me an " + char + "! " + char)
    else:
        print(" Give me a " + char + "! " + char)
    

print("What does that spell")
for i in range(times):
    print(word, "!!!")
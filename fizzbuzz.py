def fizz_buzz():
    for i in range (1, 101): # from 1 - 100
        if i % 3 == 0 and i % 5 == 0: # if divisible by 3 and 5 with no remainder;
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
fizz_buzz()

# Sequential Search
def seq_search(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(100)
search1 = seq_search(numbers, 2)
print(search1)
search2 = seq_search(numbers, 202)
print(search2)


# Palindrome
def palindrome(word):
    word = word.lower()
    return word[::-1] == word  # [::-1] returns entire slice in reverse!

print(palindrome("Mother"))
print(palindrome("Racecar"))

# Anagram
def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2) # sorted() returns string in alphabetical order

print(anagram("iceman", "cinema"))
print(anagram("icecream", "cinema"))

# store a count of character occurences in dictionary
def char_count(string):
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(char_dict)
    
char_count("SoldiersS")

#_____________RECURSION
# Recursion involves a function calling itself in the function. It changes on each run through, and has a base case that ends the loop. 

def bottles_of_beer(count):
    if count < 1: # Base case, recursion ends.
        print(f"No more bottles of beer on the wall, no more bottles of beer!")
        return
    temp = count # Before count is reduced, use it as a temp number for poem.
    count -= 1 # Reduce count for next round.
    print(f"""{temp} bottles of beer on the wall, {temp} bottles of beer, take one down, pass it around,
          {count} bottles of beer on the wall!""")
    bottles_of_beer(count) # Call function from within function, placing new product from itself as param.
    
bottles_of_beer(99)

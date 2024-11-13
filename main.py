# import mood_response
# mood = input("How are you feeling today?")
# print(mood_response.mood_response(mood))

#I also placed the calls for the other modules here for efficiency

from text_utils import capitalize_string as cap_string

s = "I'm about to start yelling, put in your earplugs!!"

print(s)

print(cap_string(s))

from text_utils import reverse_string as rev_string

string = "Put that thang down flip and reverse it!!"

print(string)

print(rev_string(string))
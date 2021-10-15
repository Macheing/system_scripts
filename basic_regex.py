import re

def check_aei (text):
  '''
  check if text contain any "aei".
  '''
  result = re.search(r".a.e.i", text)
  return result != None


print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

print(re.search(r'mach','MacHien', re.IGNORECASE))
print(re.search(r"[Pp]ython","Python"))
print(re.search(r'[a-z]mpossible', 'Aiming for greatness is by conquering impossible problems,'))
print(re.search(r'Wind[a-zA-Z]','Today it is a such windy day.', re.IGNORECASE))
print(re.search(r'Windows [a-zA-Z0-9]*','Windows 11 is out already.', re.IGNORECASE))


def check_punctuation (text):
  '''
  check if the text passed contains punctuation
  symbols: commas, periods, colons, semicolons,
  question marks, and exclamation points
  '''
  result = re.search(r"[.,.:.;.?.!..]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

print(re.search(r"[^a-zA-Z]", 'typical case for a regular expression'))
print(re.search(r"lovely pet|dangerous", 'Dog is a lovely pet while snake is dangerous to be petted.'))
print(re.search(r"dangerous pet|lovely pet", 'Snake is a dangerous pet while dog is a lovely pet.'))
print(re.findall(r'dangerous pet|lovely pet', 'Snake is a dangerous pet while dog is a lovely pet.'))
print(re.search(r'py[a-z]*n','I love Python as my favorite programming language.', re.IGNORECASE))
print(re.search(r'py[a-zA-Z].*','I love Python as my favorite programming language.', re.IGNORECASE))
print(re.search(r"p[a-z]+n", 'warm passion burning in summer.'))


def repeating_letter_a(text):
  # check if letter is repeated twice in a word.
  result = re.search(r"a.+a", text,re.IGNORECASE)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

print(re.search(r"[a-zA-Z]*\.com",'welcome to passion.com'))
print(re.search(r'\w*', "Life is beautiful when you're happy."))
print(re.search(r'\w*', "Life_is_beautiful_when_you_are_happy."))


def check_character_groups(text):
  result = re.search(r"\d", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

print(re.search(r'^A.*a$', 'Austrialia', re.IGNORECASE))
print(re.findall(r'^S.*n$', 'South Sudan, South Africa, Ethiopia, Sudan',re.IGNORECASE))


def isvalid_python_variable(variable):
  '''
  check if variable name is valid in accordance with python standard naming of variables.
  '''
  isvalid = re.search(r"^[a-zA-Z_][a-zA-Z0-9_]*$",variable)
  return isvalid != None

print(isvalid_python_variable('item1_')) # true
print(isvalid_python_variable('_item1_')) # true
print(isvalid_python_variable('it_em_1')) # true
print(isvalid_python_variable('item 1')) # false 
print(isvalid_python_variable('1_item_')) # false


def check_sentence(text):
  '''
  check if sentence is a standard sentence, meaning that it
  starts with an uppercase letter, followed by at least some lowercase letters 
  or a space, and ends with a period, question mark, or exclamation point
  '''
  result = re.search(r"^[A-Z][a-z]*(\s[a-z]+)*[\.!\?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True


def check_web_address(text):
  '''
  checks if the text passed qualifies as a top-level web address, 
  meaning that it contains alphanumeric characters (which includes letters, 
  numbers, and underscores), as well as periods, dashes, and a plus sign, 
  followed by a period and a character-only top-level domain such as ".com", 
  ".info", ".edu", etc.
  '''
  pattern = r'([a-zA-Z0-9_-]+\.[a-zA-Z]+$)'
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


def check_time(text):
  '''
  checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12,
  with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional 
  space, and then AM or PM, in upper or lower case.
  '''
  pattern = r'^(?:1[0-2]|0?[1-9]):(?:[0-5]?[0-9])(?:\s?[APap][Mm])?$'
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


def contains_acronym(text):
  '''
  checks the text for the presence of 2 or more characters or digits surrounded by parentheses, 
  with at least the first character in uppercase (if it's a letter), returning True if the condition is met, 
  or False otherwise.
  '''
  pattern = r"\([A-Za-z0-9]{2,}\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True



def check_zip_code (text):
  '''
  check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, 
  and sometimes, but not always, followed by a dash with 4 more digits
  '''
  result = re.search(r"\s[0-9]{5,}|\s[0-9]{5,}\-?[0-9]{4,}", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False
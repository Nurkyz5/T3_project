# ===========Strings============
# It's unchangeable type of data


string7="A"*8
print(string7) #AAAAAAAA

title='Iphone13'
price='100'
format1="Name: {}\nPrice: {}"
print(format1.format(title,price))



# ==========Methods of strings=======

# methods - functions, which belong to definite type of data
# we call the by dot(.)

# to see methods, we use dir

print(dir(str))
string_test='heLLo WorLd1!-'
print(string_test.swapcase()) #меняет регистр

print(string_test.count("L"))
print(string_test.count("LL"))
print(string_test.capitalize())
print(string_test.title())
print(string_test.lower().count("hello"))

print(string_test.startswith('h'))
print(string_test.startswith("L"))
print(string_test.islower())
print(string_test.isupper())
print(string_test.isnumeric())
print(string_test.isalpha())
print(string_test.isalnum())


string='    hi my name is Uson'
print(string.lstrip())
print(string.rstrip())
print(len(string))


# ============Indexes=========
str_='hello ai academy'
print(str_[::2])

# Task 
str_='Python'
print(f"First element: {str_[0]}, second element: {str_[-1]}")

str_='banana'
print(str_.count('a'))
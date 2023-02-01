# ask for user input
name = input("What is your name? ")
age = input("What is your age? ")
username = input("What is your Reddit username? ")

# format the output string
output = "Your name is {}, you are {} years old, and your Reddit username is {}.".format(name, age, username)

# write the output to a file
with open("user_info.txt", "w") as f:
    f.write(output)

# print the output
print(output)
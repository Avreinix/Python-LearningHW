types_of_people=10 #setting how many types of people there are
x=f"There are {types_of_people} types of people." #putting a formatted text with the types of people variable in it on the variable x

binary="Binary"#Just setting the binary to a binary string which it is
do_not="Don't"#do not is just a variable containing the string don't
y=f"Those who know {binary} and those who {do_not}."#y is a formatted variable which is incorporating the previous 2 variables

print(x)#just printing the string in the viariable x
print(y)#same here but for y
print(f"I said {x}")#a formatted text which incorporated the string in x in it
print(f"I also said '{y}'")#a formatted text which incorporates the string in y in it

hilarious=False#A boolean expression set to false
joke="Isnt that joke funny?! {}"#a regular nonformatted string
print(joke.format(hilarious))#here we format the string by adding the value of hilarious to the {} in the joke variablr
w="This is the left side of..."#A normal string
e="a string with a right side"#a normal string
print(w+e)#addition of strings 

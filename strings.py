#python program
#python version used is P3.5
#this program will help to understand diffeent methods that can be used on a string

name = "shraya biswas"
print(name.title()) #use .title() to make the first alphabets of the string in upper case
#output will be as follows : Shraya Biswas

print(name.upper()) #use .upper() method to chnage all the alphabets of the string to upper case
#output will be as follows : SHRAYA BISWAS

print(name.lower()) #use .lower() method to change all the alphabets of the string to lower case
#output will be as follows : shraya biswas

first_name = "shraya"
last_name = "biswas"
full_name = first_name + " " + last_name
print(full_name) #in python we use the  '+' symbol to concatenate 2 strings

print("Manojit\tBallav") #in python we use '\t' to add white space
#output of the above will be as follows : Manojit Ballav

print("Languages Known: \nBengali\nHindi\nEnglish\nTelugu") # in python use '\n' to add a newline 

#similarly use:
#.rstrip() to remove whites space from the right side of the string
#.lstrip() to remove white space from the left side of the string
#.strip() to remove white space from the string

age = 20
#uncomment the below line and you will get an error
#message = "Your age is : " + age 
# the error will be that you cannot concatenate a integer and a string
#so you will have to convert the int to string explicitly that can be done as shown below
message = "your age is : " + str(age)
print(message)


#python version: P3.5
# Favorite Numbers: Use a dictionary to store people’s favorite numbers . Think of five names, and use them as keys in your dictionary . Think of a favorite number for each person, and store each as a value in your dictionary . Print each person’s name and their favorite number .
fnumber = {
    'shraya':1,
    'shubham':2,
    'abhishek':3,
    'yashwant':4
}
for key, value in fnumber.items():
    print('\nKey: ' + key)
    print("Value: " + str(value))

#looping through all key value pairs
for name, number in fnumber.items():
    print(name.title() + "'s favourite number is "+str(number))
#looping through dictionary's keys in order
for name in sorted(fnumber.keys()):
    print(name.title() + ", Thank you for taking the poll.")
    
#thug mode
print("\n\nThug mode starts here")
for ite in fnumber:
    print("\nKey: "+ ite + "\nValue:" + str(fnumber[ite]))
for ite in fnumber:
     print(ite.title() + "'s" + ' favourite number is ' + str(fnumber[ite]))

for val in sorted(fnumber,reverse=True):
    print(val.title() + ", Thank you for taking the poll.")
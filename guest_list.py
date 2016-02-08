#python program
#python version used is P3.5
#Question
#If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
people = ['Shubham', 'Melissa', 'Shraya', 'Abhishek', 'Yashwant', 'Preethi', 'Sunny']
person = "I would like to go out for a dinner are  " + people[-1]+" " + people[0] + " "+ people[1]
print ("The invites are as follows")
print (person)
#You have heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
re_people = people.pop()
print(re_people + ' will not be able to make it to the dinner')
people[-1] = "Joy"
person = "So the revised I would like to go out for a dinner are  " + people[-1]+" " + people[0]+" " + people[1]
print(person)

cars = ['lamborghini', 'bmw', 'honda', 'maserati', 'audi', 'bugatti']
cars.sort() #this inbuilt method of pythin sorts the list in ascending order
print(cars)
cars.sort(reverse=True) #sorts the car in reverse order
print(cars)

bikes = ['ducati', 'kawasaki','honda', 'suzuki', 'harley']
print("Original list is as follows: ")
print(bikes)
print("Temporarily sorted list is as follows: ")
print(sorted(bikes)) # temporarily sorts a list
print(sorted(bikes,reverse=True)) #temporarily sorts a list in reverse
bikes.reverse() #reverses the list
print(bikes)
print(len(bikes)) #prints the length of the list
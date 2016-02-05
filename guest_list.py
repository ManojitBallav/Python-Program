#python program
#python version used is P3.5
#Question
#If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
people = ['Shubham', 'Melissa', 'Shraya', 'Abhishek', 'Yashwant', 'Preethi', 'Sunny']
person = "I would like to go out for a dinner are  " + people[-1] + people[0] + people[1]
print ("The invites are as follows")
print (person)
#You have heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
re_people = people.pop()
print(re_people + 'will not be able to make it to the dinner')

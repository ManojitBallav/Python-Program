#python program
#python version used is P3.5
#this program is to display various uses of list

vehicles = ['car', 'bike', 'streamer', 'airplane']
print(vehicles) #prints the entire list
print(vehicles[0]) #prints the first element of the list
#index position of the list starts at 0 and not 1
# here we can perform all the operations that can be performed on a string
print(vehicles[0].title())
print(vehicles[-1]) #the ordering of the lists goes in a loopback so printing the index -1 will return the last element of the list

vehicles[0] = "hovercraft"
print(vehicles) #doing this will replace the 0th element in the list


vehicles.append("submarine")
print(vehicles) # this will add submarines to the end of the list

vehicles.insert(1, "tuk-tuk")
print(vehicles) # this insert's tuk-tuk at the defined position

del vehicles[1]
print(vehicles) # removes the element from the defined position

#there is more method of removing a element from a list, that is by using the pop() method, we use this method because sometimes we want to use the variable which we remove.
#pop method follows the rules of a stack which is FIFO (first in first out) so the element which is first entered is removed
re_vehicles = vehicles.pop()
print(re_vehicles)

vehicles.remove("streamer") #removing elements by value
print(vehicles) 

#for the above we can store the value in a variable and use the variable as a value
#remove only removes the element only if the element is non-repititive in the list ,if the list repeats itself then we will have to use a loop to remove the recurring one

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

#loops start from here
teacher = ['annte', 'jessy', 'rebecca','fatima']
for names in teacher:
    print(names)
#we can use all the methods that come with the lists
for names in teacher:
    print(names.title() + ", You were an awesome teacher")


#creating numerical lists
#python's range make it easy to generate the range of numbers
for items in range(1,50):
    print(items)
numbers = list(range(1,11)) #using range to create a list of numbers
print(numbers) 
even_numbers = list(range(2,11,2)) #using range to create a number pattern skipping few digits
print(even_numbers)

squares =[]
for value in range(1,11):
    squares.append(value**2) #adds the recent value to thesquares list
print(squares)

#simple statistics with a list of numbers
digits = list(range(1,101))
print(min(digits)) #gives the minimum value in the list
print(max(digits)) #gives the maximum value in the list
print(sum(digits)) #gives the sum of all the values in the list

#list comprehensions
#thug mode of python :P
squares = [value**2 for value in range(1,11)]
print(squares)

#m not going thru slicing since we dont use it often
# also m not gonna use tuple since the operations are same as list the diffrence is that it uses round braces and it cannot be modified once declared but items can be added after its declaration

#if condition
cars = ['audi', 'bmw', 'honda', 'tesla']
for cas in cars:
    if cas == 'tesla':
        print('I love to own a '+cas)
    else:
        print('I also love '+cas)
        
# the condition checking things are all the same as in the other programming languages
#few noreworthy one's are
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
# this wil return a false statement

#checking whether a value is in a list
requested_toppings = ['mushrooms', 'cherry tomatoes', 'pineapple']
'mushrooms' in requested_toppings
#other way around
topngs = 'mushrooms'
if topngs not in requested_toppings:
    print("add new toopings")
else:
   print("hole in wall")

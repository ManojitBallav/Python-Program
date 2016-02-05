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

#python program
#python version used : P3.5
#Seeing the World: Think of at least five places in the world you’d like to visit .
#Store the locations in a list . Make sure the list is not in alphabetical order.Print your list in its original order . Don’t worry about printing the list neatly, just print it as a raw Python list .Use sorted() to print your list in alphabetical order without modifying the actual list .Show that your list is still in its original order by printing it .Use sorted() to print your list in reverse alphabetical order without changing the order of the original list .Show that your list is still in its original order by printing it again .Use reverse() to change the order of your list . Print the list to show that its order has changed .Use reverse() to change the order of your list again .Print the list to show it’s back to its original order .Use sort() to change your list so it’s stored in alphabetical order.Print the list to show that its order has been changed .Use sort() to change your list so it’s stored in reverse alphabetical order . Print the list to show that its order has changed.
locations = ['moscow', 'istanbul', 'phuket', 'sao paulo', 'malaysia']
print("List in original order: ")
print(locations)
print("List temporarily sorted: ")
print(sorted(locations))
print("List is still in original order")
print(locations)
print("List temporarily sorted in reverse order: ")
print(sorted(locations,reverse=True))
print("List is still in original order")
print(locations)
locations.reverse()
print("List in reverse order")
print(locations)
locations.reverse()
print("Re changing to the original form")
print(locations)
print("sorted list: ")
locations.sort()
print(locations)
print("sorted list in reverse order: ")
locations.sort(reverse=True)
print(locations)

#Python Program
#Python version : P3.5
#Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million . Also, use the sum() function to see how quickly Python can add a million numbers
million = list(range(1,1000001))
print("The minimum value is: " + str(min(million)))
print("The maximum value is: " + str(max(million)))
print("Sum of 1 million numbers is: " + str(sum(million)))
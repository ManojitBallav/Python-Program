#python Program
#python version used: P3.5
alien_0 = {'color': 'blue','points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
# a dictionary in python is a collection of key value pairs
alien_0['friend'] = 5 #adding new pair
print(alien_0)
alien_0 = {'color': 'green'} #modifying values in a dictionary
print(alien_0['color'])
del alien_0['color']
print(alien_0)

#dictionary of similar objects
favourite_languages = {'arup':'c','bedo':'c++','rituraj':'java','santanu':'jsp','mono':'python'}
print(favourite_languages)
print("Arups's favourite language is "+ favourite_languages['arup'].title() + '.')

fav_numbers = [13, 27, 33, 159, 15]

print(len(fav_numbers))

#add a item in the list

fav_numbers.append(77)

print(len(fav_numbers))

print(fav_numbers)

#add item in a specifc place

fav_numbers.insert(0, 7)
print(fav_numbers)

#delete an item
del(fav_numbers[0])
print(fav_numbers)

#Remove enough items from fav_numbers until there's only one number left
del(fav_numbers[1:])
print(fav_numbers)
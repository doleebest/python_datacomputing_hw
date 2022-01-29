
fruitdict = {'banana': 400, 'mango': 3000,
             'apple': 1000, 'grape': 800, 'watermelon': 5000}

fruits = ['mango', 'apple', 'grape', 'apple', 'mango',
          'banana', 'mango', 'apple', 'mango', 'mango',
          'grape', 'mango', 'watermelon', 'grape', 'banana',
          'apple', 'mango', 'mango', 'banana', 'mango']

sum=0
for i in range (len(fruits)) :
    sum+=fruitdict[fruits[i]]

print(sum)

# Age ratings for movies

```
print("Please enter your age")
while True:
    try:
        age = int(input())
    except ValueError:
        print("Please enter digits only")
        continue
    else:
        break
```
The above code asks the user for their age and ensures that they enter an integer and not any other data type. It is called a while True loop. In the 4th line we have specified an integer by using "int" before the input. If the user does not use an integer then the statement "Please enter digits only" will print out.
```
if age < 1:
    print("You must be at least one years old")
elif age < 8:
    print("You may watch universal movies")
elif age < 12:
    print("You may watch universal movies and pg movies")
elif age < 15:
    print("You may watch universal movies, pg movies and movies rated 12")
elif age < 18:
    print("You may watch universal movies, pg movies, movies rated 12 and movies rated 15")
elif age <= 117:
    print("You may watch all movies")
else:
    print("Please enter a real age")
```
This code gives a range of ages and the corresponding rated movies that the person can watch. The range is from 1 to 117 as you must be at least 1 to watch a movie and the oldest person on record is 117. If the user provides a value outside of the range then the statement "Please enter a real age" will be printed.
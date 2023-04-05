print("Please enter your age")
while True:
    try:
        age = int(input())
    except ValueError:
        print("Please enter digits only")
        continue
    else:
        break


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

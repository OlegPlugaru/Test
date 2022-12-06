
friends = ["Jim", "Karen", "Kevin"]
for letter in "Giraffe Academy":
    print(letter)

for friend in friends:
    print(friend)
    
for index in range(3, 10):
    print(index)

for index in range(len(friends)):
     print(friends[index])
  
for index in range(5):
    if index == 0:
        print(str(index + 1) + " Iteration")
    elif index == 1:
        print("Second Iteration")
    else:
        print("Not first")
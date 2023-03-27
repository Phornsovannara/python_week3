for number in range(1,21):
    if number%2==0:
        if number==4:
          print(f"{number} UNLUCKY!")
        else:
          print(f"{number} is even")
    elif number%2 !=0:
        if number==13:
          print(f"{number} UNLUCKY!")
        else:
          print(f"{number} is odd")
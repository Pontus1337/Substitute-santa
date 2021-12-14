# Substitute santa



def main():
    while True:
        a=input("do you want to make a wishlist or read a wishlist?\n")
        if "read" or "make" in a:
            break
        else:
            print("looks like you wrote something wrong :(")

    if "make" in a:
        ad=""
        nam=""
        wish=""
        ad=input("What do you wnat your wishlist to be called\n").lower()
        nam=input("What is your name?")
        while True:
            wish=input("What do you wish for christmas?, press enter to go out of this mode\n")
            if wish=="":
                break
            else:
                with open(f"{ad}.txt","w", encoding="utf8") as f:
                    f.write(f"{wish}\n")
        with open(f"{ad}.txt","w", encoding="utf8") as f:
            f.write(f"\n{nam}")
    elif "read" in a:
        ad=""
        ad=input("What is the wishlist that you want to read called?\n").lower()
        with open(f"{ad}.txt","r", encoding="utf8") as f:
            print(f.read())


if __name__=="__main__":
    main()
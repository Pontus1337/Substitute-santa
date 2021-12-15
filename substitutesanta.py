# Substitute santa

#naughtylist
def rn():
    with open("naughtylist.txt","r",encoding="utf8") as f:
        for i in f.readlines():
            print(i.strip("\n"))

def rr():    
    with open("naughtylist.txt","a",encoding="utf8") as f:
        kol=input("who has been naugty?\n")
        print("These are alredy in the list")
        f.writelines(f"\n{kol}")

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
        with open(f"{ad}.txt","w", encoding="utf8") as f:
            f.write(f"n{nam}\n")
        while True:
            wish=input("What do you wish for christmas?, press enter to go out of this mode\n")
            if wish=="":
                break
            else:
                with open(f"{ad}.txt","a", encoding="utf8") as f:
                    f.write(f"\n{wish}")

    elif "read" in a:
        ad=""
        ad=input("What is the wishlist that you want to read called?\n").lower()
        with open(f"{ad}.txt","r", encoding="utf8") as f:
            print(f.read())


    
    val=input("read or write naughty list\n")
    if "read" in val:
        rn()
    elif "write" in val:
        rn()
        rr()








if __name__=="__main__":
    main()
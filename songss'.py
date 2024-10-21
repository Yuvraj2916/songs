import time
songs=[]
c="y"
while(c=="y"):
    print("     MOOD    ")
    print("1. HAPPY")
    print("2. EMOTIONAL")
    print("3. ROMANTIC")
    print("4. Display")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        p=input("Enter song name:")
        abc=(p)
        songs.append(abc)
    elif(choice==2):
        a=input("Enter song name:")
        nvm=(a)
        songs.append(nvm)
    elif(choice==3):
        g=input("Enter song name:")
        gms=(g)
    elif(choice==4):
        l=len(songs)
        for i in range(0,1):
            print(songs[i])
    else:
        print("Wrong choice")
        time.sleep(2)
        print("Exitting")
    c=input("Do you want to continue or not:")
    

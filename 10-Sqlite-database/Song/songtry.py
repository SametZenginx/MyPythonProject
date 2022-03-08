from songmodul import *
import time

print("""
********************************************************************

Welcome to the Repertoire...

Operations:

1-)Add Song
2-)Delete Song
3-)Show Songs
4-)Total Song Duration

Please 'q' for exiting.
********************************************************************
""")

reperToire = Repertoire()

while True:
    operation = input("Please enter the operation: ")

    if operation=="q":
        time.sleep(1)
        print("Exiting the program...")
        time.sleep(1)
    elif operation=="1":
        time.sleep(1)
        name = input("Name: ")
        artist = input("Artist: ")
        album = input("Album: ")
        productionCompany = input("Production Company: ")
        songDuration = input("Song Duration: ")

        newSong = Song(name,artist,album,productionCompany,songDuration)

        print("Adding the song...")
        time.sleep(2)
        reperToire.addSong(newSong)

        print("Added the song.")
    elif operation=="2":
        time.sleep(1)
        
        name = input("Which books you want to delete?: ")

        answer = input("Are you sure?(Y)(N): ")

        if answer =="Y":
            print("Deleting...")
            Repertoire.deleteSong(name)
        
        elif answer =="N":
            print("Not deleting. Exiting the delete part..")
        
        else:
            print("Invalid operation.")
    elif operation=="3":
        reperToire.showSongs()
    
    elif operation=="4":
        reperToire.totalSongDuration()
        

    else:
        print("Invalid operation.")

    
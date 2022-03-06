import sqlite3

class Song():

    def __init__(self,songName,artist,album,productionCompany,songDuration):
        self.songName = songName
        self.artist = artist
        self.album = album
        self.productionCompany = productionCompany
        self.songDuration = songDuration

    def __str__(self):

        return "\n\n****************************\nSong Name: {}\nArtist: {}\nAlbum: {}\nProduction Company: {}\nSong Duration: {}\n*****************************".format(self.songName,self.artist,self.album,self.productionCompany,self.songDuration)

class Repertoire():

    def __init__(self):

        self.createConnect()

    def createConnect(self):
        self.connection = sqlite3.connect("repertoire.db")
        self.cursor = self.connection.cursor()

        query = "CREATE Table IF NOT EXISTS Repertoire(SongName TEXT,Artist TEXT,Album TEXT,ProductionCompany TEXT,SongDuration INT)"

        self.cursor.connection(query)

        self.connection.commit()
    
    def disconnect(self):
        self.connection.close()
    
    def showSongs(self):

        query = "SELECT * From Repertoire"

        self.cursor.execute(query)

        lists = self.cursor.fetchall()

        if len(lists) == 0:
            print("There are no songs in the repertoire.")
        else:
            for i in lists:
                
                singnow = Song(i[0],i[1],i[2],i[3],i[4],i[5])
                print(singnow)
    
    def totalSongDuration(self):

        pass

    def addSong(self,newsong):

        query = "Insert into Repertoire(?,?,?,?,?)"

        self.cursor.execute(query,(newsong.songName,newsong.artist,newsong.album,newsong.productionCompany,newsong.songDuration))
        
        self.connection.commit()

    def deleteSong(self,delsong):

        query = "DELETE From Repertoire where Name = ?"

        self.cursor.execute(query,(delsong,))

        self.connection.commit()

    




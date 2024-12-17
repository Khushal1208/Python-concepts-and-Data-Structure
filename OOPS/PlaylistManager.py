# class Song:
#     def __init__(self):
#         self.song_name = ""
#         self.singer = ""
    
#     def setSongName(self,song_name):
#         self.song_name = song_name
#     def getSongName(self):
#         return self.song_name
    
#     def setSongName(self,singer):
#         self.singer = singer
#     def getSongName(self):
#         return self.singer
 
class Playlist:
    
    def __init__(self):
        self.playlist = []


    def addSong(self,song):
        # song = Song()
        # song.setSongName(input("enter song :"))
        
        if song in self.playlist:
            print("already exist")
        else:
            self.playlist.append(song)

    def removeSong(self,song_name):
        if song_name in self.playlist:
            self.playlist.remove(song_name)
            return True
        else :
            return False
    
    def playNext(self):
        return self.playlist.pop(0)
    
    def getPlaylist(self):
        return self.playlist

    
playlist = Playlist()
playlist.addSong("song A")
playlist.addSong("song B")
playlist.addSong("song C")
print(playlist.getPlaylist())
print(playlist.playNext())
print(playlist.getPlaylist())
print(playlist.removeSong("song C"))
print(playlist.getPlaylist)




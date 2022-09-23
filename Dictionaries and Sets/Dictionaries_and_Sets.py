"""
This is my favorite song
"""
#song ="playlist" #Song's name
#Artist="Jonas Monar"#Singer's name from Germany
#TimeMinutes = 3#Song's Duration


favorite_song = {"Artist":"JonasMonar" ,"Song":"playlist" , "Time(Minutes)":"3"}
print(favorite_song)


for key in favorite_song:
    print("{0:s}: \"{1:s}\"".format(key.capitalize(), favorite_song[key]))

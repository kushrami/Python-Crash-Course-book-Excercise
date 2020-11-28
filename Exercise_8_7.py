#Album:

def make_album(artist_name,album_title,number_of_tracks=0):
    if number_of_tracks > 0:
        Dictionary = {'artist name' : artist_name,'album title': album_title,'Number of tracks':number_of_tracks}
    else:
        Dictionary = {'artist name' : artist_name,'album title': album_title}
    print(Dictionary)
    return Dictionary


MJ = make_album('MJ','Dangerous')
CP = make_album('charlie Puth','Voicenotes',3)
ARR = make_album('A R Raheman','Vande matram')


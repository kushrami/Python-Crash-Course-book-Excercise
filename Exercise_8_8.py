#User albums:
def make_album(artist_name,album_title,number_of_tracks=0):
    if number_of_tracks > 0:
        Dictionary = {'artist name' : artist_name,'album title': album_title,'Number of tracks':number_of_tracks}
    else:
        Dictionary = {'artist name' : artist_name,'album title': album_title}
    print(Dictionary)
    return Dictionary

Flag = True
while Flag:
    Artist = input("Please enter Artist name or enter 'q' for exit:")
    if Artist != 'q':
        Album = input("Please enter That Artist album or enter 'q' for exit:")
        if Album != 'q':
            make_album(Artist,Album)
        else:
            Flag = False
            break
    else:
        Flag = False
        break
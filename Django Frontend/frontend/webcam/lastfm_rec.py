# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 23:55:44 2018

@author: Saurav
"""
import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "b7e4cd326135060d2dc2aca003db3cf0"  # this is a sample key
API_SECRET = "8702313603d5be55e6845300d67bbbdd"

# In order to perform a write operation you need to authenticate yourself
username = "SAURAV7SAHA"
password_hash = pylast.md5("Slayer@77")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

# Now you can use that object everywhere
#artist = network.get_artist("System of a Down")
#artist.shout("<3")

'''
track = network.get_track("Iron Maiden", "The Nomad")
track.love()
track.add_tags(("awesome", "favorite"))
print(track.love())
'''
# Type help(pylast.LastFMNetwork) or help(pylast) in a Python interpreter
# to get more help about anything and see examples of how it works

def nameinput(name):

    artist = network.get_artist(name)

    print(type(artist))

    print()

    img=artist.get_cover_image()
    print(img)

    track_prime=[]
    tracks=artist.get_top_tracks(5)
    #print(tracks)
    for t in tracks:
        co=0
        for i in t:
            if(co==0):
                #print(i)
                track_prime.append(str(i))
                co=co+1
    print(track_prime)


    #print()

    cart = artist.get_bio_content()
    #print(cart)
    #print()
    test = artist.get_similar(5)
    #print(test)
    #print()
    #print()

    art_l=[]
    sub_tracks=[]
    sub_tr_l=[]

    for x in test:
        #print(type(x))
        c=0
        for y in x:
            if(c==0):
                #print(str(y))
                art_l.append(str(y))
                art = network.get_artist(str(y))
                track=art.get_top_tracks(5)
                #print(track)
                for tr in track:
                    cou=0
                    for n in tr:
                        if(cou==0):
                            #print(n)

                            sub_tr_l.append(str(n))
                            cou=1
                sub_tracks.append(str(sub_tr_l))
                #sub_tracks=sub_tracks+(sub_tr_l)
                #print(sub_tracks)
                sub_tr_l=[]
                c=1
            #print(type(y))
                print()
    #print(sub_tr_l)

    for l in sub_tracks:
        #printing tracks from similar artists
        print([l])

    print()
    #art_l displays similar artists
    print(art_l)

    xx=track_prime+sub_tracks+art_l
    return xx

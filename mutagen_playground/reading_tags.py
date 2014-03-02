__author__ = 'Charlie'

import mutagen
FILES = ["../music_files/m4asample.m4a", "../music_files/mp3sample.mp3"]

from mutagen.easyid3 import EasyID3

mk = EasyID3

# Hack mutagen EasyID3 to enformce convention: TPE2 = albumartist...
for frameid, key in {
    "TPE2": "albumartist"
}.iteritems():
    mk.RegisterTextKey(key, frameid)
    mutagen.easyid3.EasyID3 = mk



def get_tags(filename):
    return mutagen.File(filename, easy = True)

# Monkey patch easyid3


def main():
    for f in FILES:
        tags = get_tags(f)

        print "----------- ", f, " -------------------------"
        print tags.mime[0]
        # print help(tags)

        # Fix albulmartist if it isn't included.
        if "albumartist" not in tags and "artist" in tags:
            print "artist but no albumartist"
            tags["albumartist"] = tags["artist"]

            #Attempt to save:
            tags.save()


        for k, v in tags.items():
            print k, v



if __name__ == "__main__":
    main()
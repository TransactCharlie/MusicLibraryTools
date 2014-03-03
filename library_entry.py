__author__ = 'Charlie'

import mutagen
from collections import defaultdict

# Monkey patch mutagen easyid3 to accept 'albumartist' as an mp3 tag (TPE2)
# Note this results in albumartist and performer being the same mp3 key
# Most software uses PTE2 as the albumartist key.
# M4a files work out of the box.
from mutagen.easyid3 import EasyID3
EasyID3.RegisterTextKey("albumartist", "TPE2")

class LibraryEntry(object):

    tags = defaultdict(lambda: None)

    def __init__(self, filename):
        self.filename = filename
        self.etags = mutagen.File(filename, easy = True)
        self.mimetype = self.etags.mime[0]

        # Populate the self tags
        for k, v in self.etags.items():
            self.tags[k] = v

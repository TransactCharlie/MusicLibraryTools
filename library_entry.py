__author__ = 'Charlie'

import mutagen
from collections import defaultdict

# Monkey patch mutagen easyid3 to accept 'albumartist' as an mp3 tag (TPE2)
# Note this results in albumartist and performer being the same mp3 key
# so we map "performer" to a nonexistent mp3 tag entity
# Most software uses PTE2 as the albumartist key.
# M4a files work out of the box.
from mutagen.easyid3 import EasyID3
EasyID3.RegisterTextKey("albumartist", "TPE2")
EasyID3.RegisterTextKey("performer", "XXX")

class LibraryEntry(object):

    def __init__(self, filename):
        self.filename = filename
        self.etags = mutagen.File(filename, easy = True)
        self.mimetype = self.etags.mime[0]

    @property
    def tags(self):
        tags = defaultdict(lambda: None)
        # Populate the self tags
        for k, v in self.etags.items():
            tags[k] = v
        return tags

    def remove_unwanted_tags(self):
        """removes any extraneous information from tags (comments, etc)"""
        keep_tags = ["artist", "albumartist", "title", "tracknumber", "album", "discnumber", "date", "genre"]
        for k in (k for k in self.etags.keys() if k not in keep_tags):
            del(self.etags[k])
__author__ = 'Charlie'

import unittest
from library_entry import LibraryEntry

class TestLibraryEntry(unittest.TestCase):

    def setUp(self):
        self.mp3 = LibraryEntry("music_files/mp3sample.mp3")
        self.m4a = LibraryEntry("music_files/m4asample.m4a")

    def tearDown(self):
        self.mp3 = None
        self.m4a = None

    def test_can_read_m4a_tag(self):
        self.assertIsNotNone(self.m4a.etags)

    def test_can_read_mp3_tag(self):
        self.assertIsNotNone(self.mp3.etags)

    def test_can_get_albumartist_from_mp3_tag(self):
        self.assertIsNotNone(self.mp3.etags["albumartist"])

    def test_can_set_albumartist_in_mp3_file(self):
        self.mp3.etags["albumartist"] = "test1"
        self.assertEqual(self.mp3.etags["albumartist"], ["test1"])

    def test_can_get_unused_tag_from_tags(self):
        self.assertEqual(self.mp3.tags['NO_SUCH_TAG'], [])
        self.assertEqual(self.m4a.tags['NO_SUCH_TAG'], [])

    def test_can_delete_unwanted_tags(self):
        self.mp3.etags["albumartist"] = "keep"
        self.mp3.etags["composer"] = "to_be_deleted"
        self.mp3.remove_unwanted_tags()
        self.assertTrue("albumartist" in self.mp3.etags)
        self.assertTrue("composer" not in self.mp3.etags)

        self.m4a.etags["albumartist"] = "keep"
        self.m4a.etags["comment"] = "to_be_deleted"
        self.m4a.remove_unwanted_tags()
        self.assertTrue("albumartist" in self.m4a.etags)
        self.assertTrue("comment" not in self.m4a.etags)

    def test_delete_etag(self):
        self.mp3.remove_tag("artist")
        self.assertTrue("artist" not in self.mp3.etags)

        self.m4a.remove_tag("artist")
        self.assertTrue("artist" not in self.m4a.etags)

    def test_populate_albumartist_from_artist(self):
        self.mp3.remove_tag("albumartist")
        self.mp3.etags["artist"] = "populate_albumartist"
        self.mp3.populate_albumartist_from_artist()
        self.assertEqual(self.mp3.tags["albumartist"], ["populate_albumartist"])

        self.m4a.remove_tag("albumartist")
        self.m4a.etags["artist"] = "populate_albumartist"
        self.m4a.populate_albumartist_from_artist()
        self.assertEqual(self.m4a.tags["albumartist"], ["populate_albumartist"])
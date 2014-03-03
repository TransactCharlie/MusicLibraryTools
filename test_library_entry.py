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
        self.assertIsNone(self.mp3.tags['foo'])
        self.assertIsNone(self.m4a.tags['foo'])
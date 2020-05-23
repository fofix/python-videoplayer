#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import urllib

from videoplayer._VideoPlayer import VideoPlayer
from videoplayer._VideoPlayer import VideoPlayerError


if sys.version_info.major == 3:
    urllib = urllib.request


class VideoPlayerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # set urls
        url_ogg = "http://download.blender.org/peach/trailer/trailer_400p.ogg"
        #url_m4v = "http://mirror.cessen.com/blender.org/peach/trailer/trailer_iphone.m4v"
        url_m4v = "http://download.blender.org/peach/trailer/trailer_iphone.m4v"
        # set paths
        dirname = os.path.dirname(__file__)
        filename_ogg = "trailer_bick-buck-bunny_400p.ogg"
        filename_m4v = "trailer_bick-buck-bunny_iphone.m4v"
        filepath_ogg = os.path.join(dirname, filename_ogg)
        filepath_m4v = os.path.join(dirname, filename_m4v)
        # download dataset
        ## test if file exists
        if not os.path.isfile(filepath_ogg):
            urllib.urlretrieve(url_ogg, filepath_ogg)
        if not os.path.isfile(filepath_m4v):
            urllib.urlretrieve(url_m4v, filepath_m4v)

    def setUp(self):
        # set paths
        self.dirname = os.path.dirname(__file__)
        filename_ogg = u"trailer_bick-buck-bunny_400p.ogg"
        filename_m4v = u"trailer_bick-buck-bunny_iphone.m4v"
        filepath_ogg = os.path.join(self.dirname, filename_ogg).encode()
        self.filepath_m4v = os.path.join(self.dirname, filename_m4v).encode()
        # setup the video player
        self.player = VideoPlayer(filepath_ogg)

    def test_play(self):
        self.player.play()
        self.assertFalse(self.player.eof())

    def test_play_video_error(self):
        with self.assertRaises(VideoPlayerError):
            VideoPlayer(self.filepath_m4v)

    def test_play_bad_file(self):
        bad_filepath = os.path.join(self.dirname, 'bad_filename').encode()
        with self.assertRaises(IOError):
            VideoPlayer(bad_filepath)

    def test_pause(self):
        self.player.pause()

    def test_advance(self):
        new_position = 33  # in seconds
        self.assertFalse(self.player.eof())
        self.player.advance(new_position)
        self.assertTrue(self.player.eof())

    def test_bind_frame(self):
        self.player.bind_frame()

    def test_eof(self):
        self.assertFalse(self.player.eof())

    def test_aspect_ratio(self):
        ratio = self.player.aspect_ratio()
        self.assertIsInstance(ratio, float)

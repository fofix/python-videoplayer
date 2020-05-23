#####################################################################
# -*- coding: iso-8859-1 -*-                                        #
#                                                                   #
# Frets on Fire X (FoFiX)                                           #
# Copyright (C) 2010 FoFiX Team                                     #
#               2010 John Stumpo                                    #
#                                                                   #
# This program is free software; you can redistribute it and/or     #
# modify it under the terms of the GNU General Public License       #
# as published by the Free Software Foundation; either version 2    #
# of the License, or (at your option) any later version.            #
#                                                                   #
# This program is distributed in the hope that it will be useful,   #
# but WITHOUT ANY WARRANTY; without even the implied warranty of    #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     #
# GNU General Public License for more details.                      #
#                                                                   #
# You should have received a copy of the GNU General Public License #
# along with this program; if not, write to the Free Software       #
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,        #
# MA  02110-1301, USA.                                              #
#####################################################################

# First a thin wrapper around VideoPlayer from graphics.VideoPlayer.c...

__version__ = "1.0"

cdef extern from "VideoPlayer.h":
    ctypedef struct CVideoPlayer "VideoPlayer":
        pass

    ctypedef int GQuark
    ctypedef struct GError:
        GQuark domain
        char* message
    GQuark G_FILE_ERROR
    GQuark VIDEO_PLAYER_ERROR
    void g_error_free(GError*)

    CVideoPlayer* video_player_new(char*, GError**)
    void video_player_destroy(CVideoPlayer*)
    void video_player_play(CVideoPlayer*)
    void video_player_pause(CVideoPlayer*)
    bint video_player_advance(CVideoPlayer*, double, GError**)
    bint video_player_bind_frame(CVideoPlayer*, GError**)
    bint video_player_eof(CVideoPlayer*)
    double video_player_aspect_ratio(CVideoPlayer*)

class VideoPlayerError(Exception):
    pass

cdef object raise_from_gerror(GError* err):
    assert err is not NULL
    if err.domain == VIDEO_PLAYER_ERROR:
        exc = VideoPlayerError(err.message)
    elif err.domain == G_FILE_ERROR:
        exc = IOError(err.message)
    else:
        exc = Exception(err.message)
    g_error_free(err)
    raise exc

cdef class VideoPlayer(object):
    cdef CVideoPlayer* player

    def __cinit__(self, char* filename):
        cdef GError* err = NULL
        self.player = video_player_new(filename, &err)
        if self.player is NULL:
            raise_from_gerror(err)

    def __dealloc__(self):
        if self.player is not NULL:
            video_player_destroy(self.player)

    def play(self):
        video_player_play(self.player)

    def pause(self):
        video_player_pause(self.player)

    def advance(self, double newpos):
        cdef GError* err = NULL
        if not video_player_advance(self.player, newpos, &err):
            raise_from_gerror(err)

    def bind_frame(self):
        cdef GError* err = NULL
        if not video_player_bind_frame(self.player, &err):
            raise_from_gerror(err)

    def eof(self):
        return video_player_eof(self.player)

    def aspect_ratio(self):
        return video_player_aspect_ratio(self.player)

# VideoPlayer

[![Build Status](https://travis-ci.org/fofix/python-videoplayer.svg?branch=master)](https://travis-ci.org/fofix/python-videoplayer)


VideoPlayer is a C-extension in Python to read OGG video files.


## Setup

### Dependencies

You'll need those packages:

* `glib`
* `libogg`
* `libtheora`
* `libswscale` (part of `ffmpeg`).


### Native modules

Build the extension:

    python setup.py build_ext --inplace --force


## Tests

To test this python package, we are using [Big Buck Bunny trailers](https://peach.blender.org/trailer-page/):

* [OGG trailer](http://download.blender.org/peach/trailer/trailer_400p.ogg) (4.3MiB)
* [IPhone trailer](http://mirror.cessen.com/blender.org/peach/trailer/trailer_iphone.m4v) (3.8MiB)

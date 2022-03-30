# VideoPlayer

[![Tests](https://github.com/fofix/python-videoplayer/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/fofix/python-videoplayer/actions/workflows/tests.yml)
[![Build status](https://ci.appveyor.com/api/projects/status/kl6wvf6yuv0b5pjt/branch/master?svg=true)](https://ci.appveyor.com/project/Linkid/python-videoplayer/branch/master)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/videoplayer.svg)](https://pypi.python.org/pypi/videoplayer)
[![PyPI version](https://img.shields.io/pypi/v/videoplayer)](https://pypi.python.org/pypi/videoplayer)


VideoPlayer is a C-extension in Python to read OGG video files.


## Setup

### Dependencies

You'll need those packages:

* `glib`
* `libogg`
* `libtheora`
* `libswscale` (part of `ffmpeg`).

You'll also need some python package:

    pip install -r requirements.txt


### Native modules

Build the extension:

    python setup.py build_ext --inplace --force


## Tests

To test this python package, we are using [Big Buck Bunny trailers](https://peach.blender.org/trailer-page/):

* [OGG trailer](http://download.blender.org/peach/trailer/trailer_400p.ogg) (4.3MiB)
* [IPhone trailer](http://mirror.cessen.com/blender.org/peach/trailer/trailer_iphone.m4v) (3.8MiB)

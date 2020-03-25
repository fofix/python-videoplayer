# VideoPlayer

[![Build Status](https://travis-ci.org/fofix/python-videoplayer.svg?branch=master)](https://travis-ci.org/fofix/python-videoplayer)


VideoPlayer is a C-extension in Python.


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

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-self-use, pointless-statement, missing-docstring, invalid-name

import os
import six

from ..api import guessit, properties

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def test_default():
    ret = guessit('Fear.and.Loathing.in.Las.Vegas.FRENCH.ENGLISH.720p.HDDVD.DTS.x264-ESiR.mkv')
    assert ret and 'title' in ret


def test_forced_unicode():
    ret = guessit(u'Fear.and.Loathing.in.Las.Vegas.FRENCH.ENGLISH.720p.HDDVD.DTS.x264-ESiR.mkv')
    assert ret and 'title' in ret and isinstance(ret['title'], six.text_type)


def test_forced_binary():
    ret = guessit(b'Fear.and.Loathing.in.Las.Vegas.FRENCH.ENGLISH.720p.HDDVD.DTS.x264-ESiR.mkv')
    assert ret and 'title' in ret and isinstance(ret['title'], six.binary_type)


def test_unicode():
    ret = guessit('[阿维达].Avida.2006.FRENCH.DVDRiP.XViD-PROD.avi')
    assert ret and 'title' in ret


def test_properties():
    props = properties()
    assert 'video_codec' in props.keys()

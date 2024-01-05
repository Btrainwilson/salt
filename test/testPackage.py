import salt
import pytest
import os
import sys


def testRotation():
    dir = os.path.dirname(os.path.realpath(__file__))
    salt.rotate_file(dir + "/index.html", dir + "/files/")


def testServer():
    dir = os.path.dirname(os.path.realpath(__file__))
    salt.run_http_server(dir, 8008)

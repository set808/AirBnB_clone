#!/usr/bin/python3
"""Tests for the console"""


import console
import unittest
import os
import json
import shutil
import io
from contextlib import redirect_stdout
from models.engine.file_storage import FileStorage

class TestConsole(unittest.TestCase):
    """Tests for the console"""

    @classmethod
    def setUp(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_all(self):
        """Test all command without args"""
        self.maxDiff = None
        shutil.copy("./tests/allfile.json", "./file.json")
        teststore = FileStorage()
        teststore.reload()
        outbuffer = io.StringIO()
        f = open("./tests/inalltest.txt", "r")
        cmdp = console.HBNBCommand(stdin=f, stdout=outbuffer)
        cmdp.use_rawinput = False
        cmdp.prompt = ""
        with redirect_stdout(outbuffer):
            cmdp.cmdloop()
        f.close()
        g = open("./tests/inallresult.txt")
        self.assertEqual(g.read(), outbuffer.getvalue())
        g.close()

    def test_allargs(self):
        """Test all command with args"""
        self.maxDiff = None
        shutil.copy("./tests/allfile.json", "./file.json")
        teststore = FileStorage()
        teststore.reload()
        outbuffer = io.StringIO()
        f = open("./tests/inallindtest.txt", "r")
        cmdp = console.HBNBCommand(stdin=f, stdout=outbuffer)
        cmdp.use_rawinput = False
        cmdp.prompt = ""
        with redirect_stdout(outbuffer):
            cmdp.cmdloop()
        f.close()
        g = open("./tests/inallindresult.txt")
        self.assertEqual(g.read(), outbuffer.getvalue())
        g.close()

    def test_show(self):
        """Test good show commands"""
        self.maxDiff = None
        shutil.copy("./tests/allfile.json", "./file.json")
        teststore = FileStorage()
        teststore.reload()
        outbuffer = io.StringIO()
        f = open("./tests/inshowtest.txt", "r")
        cmdp = console.HBNBCommand(stdin=f, stdout=outbuffer)
        cmdp.use_rawinput = False
        cmdp.prompt = ""
        with redirect_stdout(outbuffer):
            cmdp.cmdloop()
        f.close()
        g = open("./tests/inshowresult.txt")
        self.assertEqual(g.read(), outbuffer.getvalue())
        g.close()

    def test_showbad(self):
        """Test bad show commands"""
        self.maxDiff = None
        shutil.copy("./tests/allfile.json", "./file.json")
        teststore = FileStorage()
        teststore.reload()
        outbuffer = io.StringIO()
        f = open("./tests/inshowbadtest.txt", "r")
        cmdp = console.HBNBCommand(stdin=f, stdout=outbuffer)
        cmdp.use_rawinput = False
        cmdp.prompt = ""
        with redirect_stdout(outbuffer):
            cmdp.cmdloop()
        f.close()
        g = open("./tests/inshowbadresult.txt")
        self.assertEqual(g.read(), outbuffer.getvalue())
        g.close()

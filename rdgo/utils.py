#!/usr/bin/env python
#
# Copyright (C) 2015 Colin Walters <walters@verbum.org>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import sys
import subprocess
import os

from gi.repository import GLib, Gio, GSystem

def fatal(msg):
    print >>sys.stderr, msg
    sys.exit(1)

def log(msg):
    "Print to standard output and flush it"
    sys.stdout.write(msg)
    sys.stdout.write('\n')
    sys.stdout.flush()

def run_sync(args, **kwargs):
    """Wraps subprocess.check_call(), logging the command line too."""
    log("Running: %s" % (subprocess.list2cmdline(args), ))
    subprocess.check_call(args, **kwargs)

def rmrf(path):
    GSystem.shutil_rm_rf(Gio.File.new_for_path(path), None)

def ensuredir(path, with_parents=False):
    GSystem.file_ensure_directory(Gio.File.new_for_path(path), with_parents, None)

def ensure_clean_dir(path):
    rmrf(path)
    ensuredir(path)

#!/usr/bin/env python

import os
import sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, "vendor")

sys.path.append(vendor_dir)

import utilities

SCRIPT_NAMES = {"confpack-runtime", "confpack", "confpack-runtime.py"}


def main(argv):
  if argv[0] in SCRIPT_NAMES:
    argv.pop(0)

  if len(argv) == 0:
    argv.append("help") # lol

  class_name = "{}Main".format(argv.pop(0).capitalize())
  if class_name in dir(utilities):
    p = getattr(utilities, class_name, None)()
  else:
    p = None
    raise NotImplementedError

  return p(argv) or 0


if __name__ == "__main__":
  sys.exit(main(sys.argv[:]))

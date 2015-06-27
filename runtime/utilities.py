import argparse
import sys

import jinja2


class TemplateMain(object):
  def __init__(self):
    self.argparser = argparse.ArgumentParser(description="Processes a template file and replaces it all values filled out.")
    self.argparser.add_argument("path", help="The path to the template file. This file will be replaced as the jinja2 template gets executed.")
    self.argparser.add_argument("vars", nargs="*", help="key1=value1 key2=value2 to be executed in the template.")
    self.argparser.prog = self.argparser.prog + " template"

  def get_help(self):
    return self.argparser.format_help()

  def get_description(self):
    return self.argparser.description

  def __call__(self, argv):
    args = self.argparser.parse_args(argv)
    self._path = args.path
    self._vars = dict(map(lambda x: x.split("="), args.vars))
    with open(self._path, "rw") as f:
      content = f.read()
      template = jinja2.Template(content)
      content = template.render(**self._vars)
      f.write(content)

    return 0


class HelpMain(object):
  def __init__(self):
    pass

  def get_description(self):
    return "Displays this help screen. A command can be appended to this."

  def __call__(self, argv):
    if len(argv) == 0:
      utility_commands = [(k[:-4].lower(), globals()[k]) for k in globals() if k.endswith("Main")]
      print("usage: {} command".format(sys.argv[0]))
      print("")
      print("commands:")
      for name, klass in utility_commands:
        print("  {}".format(name))
        print("    {}".format(klass().get_description()))
        print("")
    else:
      p = globals()["{}Main".format(argv[0].capitalize())]()
      print(p.get_help())

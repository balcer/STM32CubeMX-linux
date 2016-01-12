"""fix files generatied by CubeMX"""
import os
from subprocess import call

def dos2unix():
    """convert Windows dos files to unix"""
    for _file in os.walk(os.getcwd()):
        for string in _file[2]:
            if string.endswith(".c") or \
               string.endswith(".h") or \
               string.endswith(".ld") or \
               string.endswith(".s") or \
               string.endswith(".launch"):
                call(["dos2unix", os.path.join(_file[0], string)])
                call(["indent", os.path.join(_file[0], string)])
                call(["rm", os.path.join(_file[0], string + "~")])
            else:
                print "skipping: %s" %string

if __name__ == "__main__":
    dos2unix()

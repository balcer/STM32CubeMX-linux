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
            else:
                print "skipping: %s" %string

def fix_indent():
    """fix c file indents"""
    for _file in os.walk(os.getcwd()):
        for string in _file[2]:
            if string.endswith(".c"):
                call(["indent", os.path.join(_file[0], string)])
                call(["rm", os.path.join(_file[0], string + "~")])

def file_cleanup():
    """move and delate files in project"""
    call(["mv", "SW4STM32/bist-122 Configuration/STM32F030F4Px_FLASH.ld", "Drivers/"])
    call(["rm", "-r", "SW4STM32"])
    call(["rm", ".mxproject"])

if __name__ == "__main__":
    dos2unix()
    fix_indent()
    file_cleanup()

"""fix files generatied by CubeMX"""
import os
import sys
from subprocess import call

def get_project_name():
    """seek for CubeMX *.ico file and return project name"""
    file_found = False
    for _file in os.listdir("."):
        if _file.endswith(".ioc"):
            file_base = os.path.splitext(_file)[0]
            file_found = True
            return file_base
    if file_found == False:
        sys.exit("No CubeMX project file")

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

def file_cleanup(project_name):
    """move and delate files in project"""
    ld_file_path = "SW4STM32/" + project_name + " Configuration/STM32F030F4Px_FLASH.ld"
    call(["mv", ld_file_path, "Drivers/"])
    call(["rm", "-r", "SW4STM32"])
    call(["rm", ".mxproject"])

def main():
    """main function"""
    project_name = get_project_name()
    dos2unix()
    fix_indent()
    file_cleanup(project_name)

if __name__ == "__main__":
    main()

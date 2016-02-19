# -*- coding: UTF-8 -*-

import sys, os, platform, errno

def usage():
    print   "\nUsage:\n" \
            "   Generate a new Juce project with Introjucer\n" \
            "\n   Clone this repository into Builds directory:\n" \
            "       $ cd projectDir/Builds/\n" \
            "       $ git clone https://github.com/wsilverio/CMakeJuce.git\n" \
            "\n   Run this python script without arguments:\n" \
            "       $ cd CMakeJuce\n" \
            "       $ python setup.py" \
            "\n" \
            "\n" \
            "Project structure:\n" \
            "   jucerProjectDir\n" \
            "   ├── Builds\n" \
            "   │   ├── CMakeJuce <-- This repo\n" \
            "   │   └── LinuxMakefile\n" \
            "   │       ├── Makefile <-- Created by Introjucer\n" \
            "   │       ├── CMakeLists.txt <-- Created by this script\n" \
            "   │       └── build\n" \
            "   │           └── ExecutableName <-- Created by Makefile (IDE)\n" \
            "   ├── CMakeLists.txt <-- Created by this script\n" \
            "   ├── YourProjectName.jucer\n" \
            "   ├── JuceLibraryCode\n" \
            "   │   └── /..Juce files../\n" \
            "   └── Source\n" \
            "       └── /..Source files../\n" \

if len(sys.argv) > 1:
    usage()
    exit()

# TODO: add support for Windows and MacOS
if platform.system() == "Linux":# or platform.system() == "Darwin" or platform.system() == "Windows":
    pass
else:
    print "Sorry. Platform system not implemented.\n"
    exit()


projectDir = "../../"
projectDirName = os.getcwd().split("/")[-3]

introjucerFile = []

for file in os.listdir(projectDir):
    if file.endswith(".jucer"):
        introjucerFile.append(file)

if len(introjucerFile) == 0:
    usage()
    print "[error] No jucer file found.\n"
    exit()
elif len(introjucerFile) > 1:
    usage()
    print "[error] Multiples jucer files exists.\n"
    exit()

print "\nFound: %s/%s" % (projectDirName, introjucerFile[0])

projectName = ""

with open(projectDir + introjucerFile[0], 'r') as introFile:
    for line in introFile:
        if "name=\"" in line:
            split = line[line.index("name=\"")+len("name=\""):]
            split = split[:split.index("\"")]
            projectName = split
            break

print "Project name:", projectName

cmakeFile = projectDir + "CMakeLists.txt"

if os.path.isfile(cmakeFile):
    os.rename(cmakeFile, cmakeFile+".old")
    print "Moved %s/CMakeLists.txt to %s/CMakeLists.txt.old" %(projectDirName, projectDirName)

with open(cmakeFile, "w+") as f:
    f.write(
        "cmake_minimum_required(VERSION 2.8)\n" \
        "project(%s)\n" \
        "\n" \
        "if(${CMAKE_SYSTEM_NAME} MATCHES \"Darwin\")\n" \
        "   add_subdirectory(Builds/MacOSX)\n" \
        "elseif(${CMAKE_SYSTEM_NAME} MATCHES \"Linux\")\n" \
        "   add_subdirectory(Builds/LinuxMakefile)\n" \
        "endif()" % projectName
    )

print "Generated %s/CMakeLists.txt" % projectDirName

cmakeFile = ""

if platform.system() == "Linux":
    cmakeFile = "../LinuxMakefile/CMakeLists.txt"
# elif platform.system() == "Darwin":
    # cmakeFile = "../MacOSX/CMakeLists.txt"
# elif platform.system() == "Windows":
    # pass
else:
    print "[error] Plataform system not implemented."
    exit()

try:
    f = open(cmakeFile, "w+")
    f.write(
        "cmake_minimum_required(VERSION 2.8)\n" \
        "include(../CMakeJuce/juce.cmake)"
    )
except IOError as e:
    if e.errno == errno.ENOENT:
        usage()
        print "[error] Have you created an export target with Introjucer?\n"
        exit()
    else:
        print e
        exit()

print "Generated %s/Builds/%s\n" % (projectDirName, cmakeFile[3:])

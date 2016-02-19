CMakeJuce
=========

This project is a copy of [teragonaudio/CMakeJuce][CMakeJuce].  
Contains a single CMake file which can be included by
[Juce][juce] projects in order to build them with the project files generated
by Introjucer.  


Tested with [CLion-1.2.4][clion] and [Creator-3.6.0][qt] on Ubuntu-15.10.


Project setup
-------------

First, generate a new Juce project with Introjucer.  
 Then add this project's
repository to your Juce project as a submodule under the `Builds` folder.  
```
cd jucerProjectDir/Builds
git clone https://github.com/wsilverio/CMakeJuce.git
```

Execute `setup.py` script:

```
python setup.py
```

An example project structure might look something like this:

```
  jucerProjectDir  
  ├── Builds  
  │   ├── CMakeJuce <-- This repo  
  │   └── LinuxMakefile  
  │       ├── Makefile <-- Created by Introjucer  
  │       ├── CMakeLists.txt <-- Created by this script  
  │       └── build  
  │           └── ExecutableName <-- Created by Makefile (IDE)
  ├── CMakeLists.txt <-- Created by this script  
  ├── YourProjectName.jucer  
  ├── JuceLibraryCode  
  │   └── /..Juce files../  
  └── Source  
    └── /..Source files../  
```

Point your CMakeList's IDE to `jucerProjectDir/CMakeLists.txt` and your executable to `jucerProjectDir/LinuxMakefile/build/ExecutableName`.  

Video example  
------------  

<center>[![Youtube- Garagem Hacker: Arduino Dojo Shield](http://img.youtube.com/vi/ABC123/0.jpg)](http://www.youtube.com/watch?v=ABC123)</center>

[juce]: http://www.juce.com
[CMakeJuce]: https://github.com/teragonaudio/CMakeJuce/
[clion]: https://www.jetbrains.com/clion/
[qt]: https://netbeans.org/features/cpp/

#!/bin/bash

Xvfb :99 &

/Katalon_Studio_Linux_64-5.7.1/katalon -noSplash -runMode=console -projectPath="$(pwd)/versusfindertest/versusfindertest.prj" -retry=1 -testSuitePath="Test Suites/Halt_test" -executionProfile="default"  -browserType="Chrome (headless)" -Djava.awt.headless
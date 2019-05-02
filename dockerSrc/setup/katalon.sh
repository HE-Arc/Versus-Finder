#!/usr/bin/env bash

set -xe

echo "Install Katalon"

directory=5.7.1
version=5.7.1
package=Katalon_Studio_Linux_64-$version.tar.gz
unzipped_directory=Katalon_Studio_Linux_64-$version

wget -O $package http://download.katalon.com/$directory/$package
mkdir /katalon
tar -xvzf $package -C /katalon
ls
rm $package

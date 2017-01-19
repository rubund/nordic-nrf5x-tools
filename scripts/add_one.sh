#!/bin/bash

NAME=$1

pushd debian
cp ../templates/template.install ${NAME}.install
cp ../templates/template.links ${NAME}.links
cp ../templates/template.postinst ${NAME}.postinst
cp ../templates/template.postrm ${NAME}.postrm
git add ${NAME}.*

TYPE="softdevices/s132"
SUBTYPE="s132"
VERSION="5.0.0-1.alpha"
NAME="softdevice-s132-5"
MAJORVERSION="5"

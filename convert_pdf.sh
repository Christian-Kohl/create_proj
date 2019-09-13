#!/bin/bash

#Comments
sudo mv /etc/ImageMagick-6/policy.xml /etc/ImageMagick-6/policy.xmlout
convert $@
sudo mv /etc/ImageMagick-6/policy.xmlout /etc/ImageMagick-6/policy.xml

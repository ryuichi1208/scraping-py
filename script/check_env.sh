#!/bin/bash

echo "##### Python Version #####"
python -V

echo "##### pip version #####"
pip -V | awk '{print $1 " "$2}'

echo "##### installed package #####"
pip list

echo "##### Update package #####"
pip list -o

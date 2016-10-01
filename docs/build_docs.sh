#!/bin/bash

sphinx-apidoc -o ./source/ ../qtmud
make html

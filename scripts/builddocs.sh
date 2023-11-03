#!/bin/bash
set -xe

sudo apt-get update
sudo apt-get -y install git rsync python3-sphinx

# Markdown support.
pip install myst-parser
# Use Read the docs theme.
pip install sphinx_rtd_theme
# bibtex support.
pip install sphinxcontrib-bibtex

pwd ls -lah
export SOURCE_DATE_EPOCH=$(git log -1 --pretty=%ct)


#######################
# BUILD DOCUMENTATION #
#######################

make clean
make html


#######################
# Update Github Pages #
#######################

# git config --global user.name "${GITHUB_ACTOR}"
# git config --global user.email "${GITHUB_ACTOR}@users.noreply.github.com"

# mkdir -p "docs/"
# rsync -av --delete "_build/html/"* "docs/"

# git add docs/

# msg="Updating Documentation for commit ${GITHUB_SHA} made on `date -d"@${SOURCE_DATE_EPOCH}" --iso-8601=seconds` from ${GITHUB_REF} by ${GITHUB_ACTOR}"
# git commit -m "${msg}"

# git push https://token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git main

# # exit cleanly
# exit 0


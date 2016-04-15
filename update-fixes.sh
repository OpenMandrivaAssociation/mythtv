#!/bin/bash

PACKAGE=mythtv
VERSION=0.28
REPO=https://github.com/MythTV/mythtv.git
FIXES=fixes/0.28

echo "Updating Fixes Source"
if [ ! -d clone ]; then
  git clone $REPO clone
  pushd clone
  git checkout -t origin/$FIXES
  popd
else
  pushd clone
  git remote update
  git checkout $FIXES
  git pull
  popd
fi

export GIT_DIR=clone/.git

GITVERSION=$(grep "^%define gitversion " ../SPECS/$PACKAGE.spec | cut -d' ' -f3)
NEW_GITVERSION=$(git describe --abbrev=4 --match='v[0-9]*' HEAD)

if [ "$NEW_GITVERSION" == "$GITVERSION" ]; then
    echo "No newer fixes available."
    exit
fi

echo "Current Git version: $GITVERSION"
echo "New Git version:     $NEW_GITVERSION"


FIXESDATE=$(grep "^%define fixesdate " ../SPECS/$PACKAGE.spec | cut -d' ' -f3)
NEW_FIXESDATE=$(date +%Y%m%d)

echo "Generating Fixes Patch ($NEW_GITVERSION)"
if [ -f fixes-$GITVERSION.patch ]; then
    svn mv fixes-$GITVERSION.patch fixes-$NEW_GITVERSION.patch
fi
git diff v$VERSION..$FIXES >fixes-$NEW_GITVERSION.patch

echo "Updating Spec"
sed -i "s/%define fixesdate $FIXESDATE/%define fixesdate $NEW_FIXESDATE/;s/%define gitversion $GITVERSION/%define gitversion $NEW_GITVERSION/;s/%define rel .*/%define rel 1/" ../SPECS/$PACKAGE.spec

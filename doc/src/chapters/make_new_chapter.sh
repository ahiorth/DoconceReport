#!/bin/bash -x
# Use a common ../make.sh file or do customized build here.
function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

main_dir=$1
set echo off
if [ ! -d $main_dir ]; then
system mkdir $main_dir
system cd $main_dir
system mkdir "src-${main_dir}"
system mkdir "fig-${main_dir}"
else
    echo "Directory ${main_dir} exists!"
fi


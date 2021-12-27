#!/bin/bash -x
# Compile a chapter as a stand-alone HTML document.
# See make.sh for variables.
#
# Run from subdirectory as
#
# bash -x ../make_html.sh main_chaptername --encoding=utf-8
set -x

mainname=$1
shift
args="$@"

CHAPTER=document
BOOK=document
APPENDIX=document

#LANG=Python
# mainname: main_chaptername
# nickname: chaptername
nickname=`echo $mainname | sed 's/main_//g'`

function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

rm -fr tmp_*

# Spell checking: done in make.sh

preprocess -DFORMAT=html ../newcommands.p.tex > newcommands_keep.tex

opt="CHAPTER=$CHAPTER BOOK=$BOOK APPENDIX=$APPENDIX"
opt="LANG=$LANG"

style=bootswatch_readable
html=${nickname}-readable
system doconce format html $mainname $opt --html_style=$style --html_output=$html --html_code_style=inherit $args
system doconce split_html $html.html --nav_button=text


# Publish
dest=../../../pub/report
if [ ! -d $dest ]; then
exit 0  # drop publishig
fi
dest=$dest/$nickname
if [ ! -d $dest ]; then
  mkdir $dest
  mkdir $dest/pdf
  mkdir $dest/html
fi
cp -r ${nickname}-*.html ._${nickname}-*.html $dest/html


# We need fig, mov in html publishing dir
rsync="rsync -rtDvz -u -e ssh -b --delete --force "
dirs="fig-$nickname mov-$nickname"
for dir in $dirs; do
  if [ -d $dir ]; then
    $rsync $dir $dest/html
  fi
done




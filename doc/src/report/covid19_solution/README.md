# Structure of this folder
Open an Ubuntu terminal and do
```
Terminal> ./make.sh
```
If you are not allowed to run the file, you might have to first make it executable, by doing
```
Terminal> chmod u+x ./make.sh
```
If you have installed all the necessary packages, the output files should be placed in the `pub` directory. If you run into problems with references, first just remove the following line in the `.do.txt` file (located at the end)
```
BIBFILE: papers.pub
```
References needs to be imported using `publish` and they should be imported from a `.bib` file. Doing
```
Terminal> publish import ref.bib
``` 
# A larger project like a thesis
This folder is based on the structure presented in the [doconce book](https://github.com/hplgit/setup4book-doconce), and once you have run the make scripts in this folder, you should check out the comprehensive doconce book repository. 

In a thesis project you do not want to have all files for each of the chapter in one directory, rather you would like to have all chapters in a separate folder. Then you can work with one chapter at a time, compile it and view the result. From time to time you will compile and run the whole thesis. 

Open an Ubuntu terminal and do
```
Terminal> python
```
This will start up python in the terminal window, next we need to make a [soft-link](https://linuxhint.com/create_symbolic_link_ubuntu) to all the chapters

```
>>> python import scripts as s
>>> s.make_links()
```
If this worked you would have created in this folder a link to all the figure and source directories in the chapter folders. Whenever you make a new chapter you need to run the python script (or to create the soft links manually). 

Next, you should be able to do
```
Terminal> ./make.sh
```
To create a pdf version of your thesis and/or
```
Terminal> ./make_html.sh
```
to create a html version. 

The output files should be placed in the `pub` directory. If you run into problems with references, first just remove the following line in the `.do.txt` file (located at the end)
```
BIBFILE: ../chapters/papers.pub
```


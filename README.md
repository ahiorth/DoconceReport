# Doconce on Windows platform
If you are a teacher or a student that use jupyter notebooks to communicate your work, [Doconce](https://github.com/doconce/doconce) is a must. It also works great for generating pdf reports and larger projects like books. One of the challenge when including code in your work is that it is hard to keep the pieces code you choose to include in your thesis/report up to date. This problem is solved if you use [Doconce](https://github.com/doconce/doconce). In [Doconce](https://github.com/doconce/doconce) you link the relevant part of your code in the thesis *directly* to your source file.

To work efficient with doconce it is good to have a certain structure and workflow. The [workflow](https://github.com/hplgit/setup4book-doconce) presented here is very similar to the one originally published by Hans Petter Langtangen, the creator of Doconce. In my experience the original workflow does not work out of the box, and one needs to do some manual adjustment, but to be fair there is nothing original in presented in this repository. The sole purpose here is to lower the bar for people that wants to use doconce on Windows. (People using macOS and Linux can just follow the instructions on the [doconce home page](https://github.com/doconce/doconce)).

# Windows and Ubuntu workflows
Much have happened to the Windows platform over the last years, and a particular attractive feature is the ability to work seamlessly with Ubuntu on a Windows machine. Windows is, in my mind, superior when it comes to graphical usability. However, the basic philosophy embedded in Windows of using a graphical user interface for every task is inefficient. Using the command shell in Ubuntu one can tailor worflows and get a lot done in a short amount of time. 

## Requirements
In order to get doconce to work properly on a Windows platform one should install Windows Subsystem for Linux (WSL). It is possible to install doconce using conda on  Windows, and if you are lucky part of the installation will work. However, even if it was possible to run the full installation of doconce on Windows, you would not (in my experience) be able to work efficiently. To be able to use the best of two worlds, Linux and Windows, is a great advantage which can be used in many other cases as well.  The key idea I would like to promote is to use Linux for all terminal work and Windows for all graphical work, like text editing and viewing of pdf, notebooks and html. 

### Install WSL (Ubuntu)
Follow the instructions [here](https://ubuntu.com/tutorials/ubuntu-on-windows#1-overview). 

### Install Conda 
The best way to install doconce is to do it via conda. Follow the instructions [here](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart) to install Anaconda.

### Install LaTeX
Next, we need to install LaTeX, open an Ubuntu terminal and do
```
Terminal> sudo apt-get install texlive-full
```
You will have to provide the password you made when installing Ubuntu.

### Install Doconce
Finally, we can install doconce from [here](https://github.com/doconce/doconce), or simply open an Ubuntu terminal from the windows start menu and do
```
Terminal> conda config --add channels conda-forge
Terminal> conda install doconce
```

### Install git (optional)
To install git on Ubuntu you will need a credential helper to access your repositories by doing e.g. `git pull` from an Ubuntu terminal. I would recommend that you first install [git on your Windows system](https://git-scm.com/download/win), after git is installed on Windows you should do a restart. Next, you can install git on Ubuntu following [these instruction](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git). 


# Accessing your Windows files from Ubuntu
Before we proceed there are some important things to note
* **never** access your Linux files **from** Windows. The other way around is ok, you can open, create, delete and edit windows files from Linux.

When you open a terminal window in Ubuntu you will be put in a (hidden) folder which is not easily found from Windows. What you should do is to navigate from your Linux folder to your home folder on Windows. The home folder on Windows is usually located at *`C:\Users\<your_user_name>`*. To navigate to this folder you should do
```
Terminal> cd /mnt/c/Users/<your_user_name>
```
(After a while you might get tired of writing the full path, and then you can create a [soft-link](https://linuxhint.com/create_symbolic_link_ubuntu/).)
Next, we would like to create a folder where we keep all our repositories, e.g. `git_repo`
```
Terminal> mkdir git_repo
```
If you now open a Windows file explorer you see that a folder in your home directory have been created with the name `git_repo`. Move into this folder from the Ubuntu terminal
```
Terminal> cd git_repo
```
and clone this repository (or simply download the repository as a zip file and unpack it here)
```
Terminal> git clone github.com/ahiorth/DoconceReport.git 
```

# What's next
In the [doc](https://github.com/ahiorth/DoconceReport/tree/master/doc) folder in this repository you wil find a `README.md` file that contains the necessary information on how to create different formats from the source. 

The simplest, minimal, example with just is the doconce file in the chapter directory. Run the `make.sh` in [chapter one directory](https://github.com/ahiorth/DoconceReport/tree/master/doc/src/chapters/ch1). You should also be able to run the doconce commands directly, without using the `make.sh` scripts, e.g. to create html
```
Terminal> doconce format html main_ch1 
```
Jupyter notebook
```
Terminal> doconce format ipynb main_ch1 
```
For `pdf` from LaTeX
```
Terminal> doconce format pdflatex main_ch1 --latex_code_style=pyg
Terminal> pdflatex main_ch1.tex
```
 see [here](http://hplgit.github.io/teamods/writing_reports/index_with_doconce_commands.html) for more information on formats. 
 
 Note that you can tell doconce to replace text in the LaTeX file before you compile the final document to pdf, making it very simple to change e.g. colours in boxes, or to replace environments.  







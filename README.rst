Elephant
=========

**elephant** is a frontend to the duplicity backup tool written in python

Install
=======

**Install from pip**
::

$ pip install elephant

**Install from github**
::

$ git clone https://github.com/bougie/elephant

**Configuration**
::

# cp /etc/elephant/config.sample.py /etc/elephant/config.py

And fill variables with right value.

How-to
------

**launch a backup**
::

$ elephant backup

**get a list of saved files**
::

$ elephant list

**get a list of saved files for a given date**
::

$ elephant list --time 2014-01-01

**do a restore in the /tmp/fubar directory**
::

$ elephant restore -d /tmp/fubar

**restore the file toto ine the current directory**
::

$ elephant restore -f toto


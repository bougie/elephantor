Elephantor
===========

**elephantor** is a frontend to the duplicity backup tool written in python

Install
=======

**Install from pip**
::

$ pip install elephantor

**Install from github**
::

$ git clone https://github.com/bougie/elephantor

**Configuration**
::

# cp /etc/elephantor/config.sample.py /etc/elephantor/config.py

And fill variables with right value.

How-to
------

**launch a backup**
::

$ elephator backup

**get a list of saved files**
::

$ elephator list

**get a list of saved files for a given date**
::

$ elephator list --time 2014-01-01

**do a restore in the /tmp/fubar directory**
::

$ elephator restore -d /tmp/fubar

**restore the file toto ine the current directory**
::

$ elephator restore -f toto


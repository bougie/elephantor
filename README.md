# Elephant

**elephant** is a frontend to the duplicity backup tool

## Examples

* Launch a backup
```
# ./elephant backup
```
* Get a list of saved files
```
# ./elephant list
```
* Get a list of saved files for a given date
```
# ./elephant list --time 2014-01-01
```
* Do a restore in the /tmp/fubar directory
```
# ./elephant restore -d /tmp/fubar
```
* Restore the file toto ine the current directory
```
# ./elephant restore -f toto
```

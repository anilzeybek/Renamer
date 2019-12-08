# Renamer

Sort and rename files in specified directory with custom header and with numbers after the header.

## Getting Started

```console
foo@bar:~$ python3 renamer.py .
DONE!
```

Or if you want with header:
```console
foo@bar:~$ python3 renamer.py -n "CUSTOM_HEADER"
DONE!
```

If you want to skip caution part:
```console
foo@bar:~$ python3 renamer.py -y
DONE!
```

By default this program will rename only files with extensions:
* .txt
* .png
* .jpg

However if you want your own extension list, you cant give it by:
```console
foo@bar:~$ python3 renamer.py -e "xml yml json"
DONE!
```


### Prerequisites

Python with version 3 is enough!
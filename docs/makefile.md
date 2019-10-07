# Quick bot, No pain / `Makefile`


## Usage

After adapting the Makefile to your bot, simply run `make install`.  
Run `make` for help.

### Overridable values:

```none
## Define those
## ...as environment variables
$ export BOTENV=customenv
$ make install

## ...or as make arguments
$ make install BOTENV=customenv
```

***`VAR`=`default`: Description***

- `BOTENV`=`botenv`: Name of the venv to create/use.

- `PY3DOT`=`7`: Defines the python3 executable to use. *Will be changed in future versions (Issue #1).*
    > `PY3DOT=6` --> `python3.6`

- `PIP_OUTPUT`=`q`: PIP verbosity option.
    > `q` - Silent  
    > `v` - Verbose *(more v's for more verbose)*  
    > ~~*unset* - Normal PIP output~~ *Unavailable for now (Issue #2).*


## Changelog

```none
## [1.0.0] - 2019-10-06
### Added
- Initial release
```

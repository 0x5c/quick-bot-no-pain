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

- `PYTHON_BIN`=`python3.7`: Defines the python executable to use.  
    > A full path may be given.

- `PIP_OUTPUT`=`-q`: PIP verbosity option.
    > `-q` - Silent  
    > `-v` - Verbose *(more v's for more verbose)*  
    > *unset* - Normal PIP output


## Changelog

```none
## [1.1.0] - 2019-10-31
### Added
- New environment variable to specify the python binary to use.
### Changed
- Changed `PIP_OUTPUT`; Added the ability to unsilence pip.
- Changed some comments.
- Fixed indentation [cosmetic].
### Removed
- No more "python minor version" environment variable.
## [1.0.0] - 2019-10-06
### Added
- Initial release
```

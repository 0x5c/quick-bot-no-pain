# Quick bot, No pain / `run.sh`

> **Note:** This wrapper assumes that the bot is  
> a) in the same directory  
> and  
> b) a file named `main.py`
>
> Modify it to fit your needs.

## Usage


```none
$ run.sh [--pass-errors] [--no-botenv] [-- [bot arguments]]
```

### Command line arguments

- `--pass-errors` : ­ ­ Exits on error from the bot, instead of restarting it.  
    *Exits with the error code from the bot.*

- `--no-botenv` : ­ ­ Allows usage of an arbitrary python executable, as specified in `PYTHON_BIN`.

- `--` : ­ ­ Stops argument parsing. Any further argument will be passed to the bot.
    > **Note** This is required to be able to pass arguments to the bot.

### Environment variables

***`VAR`=`default`: Description***

- `BOTENV`=`botenv`: The name of the venv to use.

- `PYTHON_BIN`=`python3.7`: Defines the python executable to use.  
    > A full path may be given.


## Changelog

```md
## [1.2.0] - 2019-11-04
### Added
- Ability to use arbitrary python executable.
- Environment variable to specify the executable.

## [1.1.0] - 2019-11-04
### Added
- Argument passing
### Changed
- No longer requires `bash`

## [1.0.0] - 2019-10-06
### Added
- Initial release
```

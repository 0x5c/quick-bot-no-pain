# Quick bot, No pain / `run.sh`


## Usage

> **Note:** This wrapper assumes that the bot is  
> a) in the same directory  
> and  
> b) a file named `main.py`
>
> Modify it to fit your needs.

```none
$ run.sh [--pass-errors]
```

### Command line arguments

- `--pass-errors`: Exits on error from the bot, instead of restarting it.  
    *Exits with the error code from the bot.*

### Environment variables

***`VAR`=`default`: Description***

- `BOTENV`=`botenv`: The name of the venv to use.


## Changelog

```none
## [1.0.0] - 2019-10-06
### Added
- Initial release
```

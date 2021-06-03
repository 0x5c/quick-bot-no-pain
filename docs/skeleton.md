# Quick bot, No pain / **Skeleton files**


## License

All of the skeleton files listed in this file are released under the terms of the [*Unlicense*](https://unlicense.org/).  
[Full text of the Unlicense](#unlicense)


## Included files

- `requirements.txt`: standard file for passing package dependencies to pip.

- `templates/template_*`: templates of settings and token files, ready for the Makefile.  
    Put your default settings in `options` for quick setup via the Makefile.
    > In the bot, load those by importing them. ie: `from data import options`

- `.gitignore`: git ignore file, pre-configured for a basic bot.


## Changelog

```md
## [Unreleased]
### Added
- Comments in template files.
### Changed
- Entirety of `data/` ignored.
- Catch-all to ignore environments.

## [2.0.0] - 2019-11-24
### Changed
- Modified to reflect the move of options/keys to "/data".

## [1.0.0] - 2019-10-06
### Added
- Initial release
```


## Unlicense

```none
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
```

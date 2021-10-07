# {{ bot.name }}

*{{ bot.description }}*


## Features

Your project's features here.


## Running the bot

Requires Python {{ bot.target_ver }} or newer.

Prep the environment. For more information on extra options, see the [quick-bot-no-pain Makefile documentation](https://github.com/0x5c/quick-bot-no-pain/blob/master/docs/makefile.md).

```sh
$ make install
```

Run. For more information on options, see the [quick-bot-no-pain run.sh documentation](https://github.com/0x5c/quick-bot-no-pain/blob/master/docs/run.sh.md).

```sh
$ run.sh
```


{% if docker %}
## Run with Docker

See [README-DOCKER.md](README-DOCKER.md)


{% endif %}
## License

Copyright (c) {{ copyright.year }} {{ copyright.holder }}
{% if copyright.licence %}

This project is released under the {{ copyright.licence }}.  
See [`LICENSE`](LICENSE) for the full license text.
{% endif %}

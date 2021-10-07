#!/usr/bin/env python3
"""
{{ bot.name }}
{{ short_desc }}
---
Copyright (C) {{ copyright.year }} {{ copyright.holder }}

{% if copyright.licence.spdx %}
SPDX-License-Identifier: {{ copyright.licence.spdx }}
{% endif %}
{% if copyright.licence.name %}
{{ copyright.licence.name }}
{% endif %}
"""


import discord
from discord.ext import commands

import data.keys as keys
import data.options as opt


# --- Settings ---

#* You might want to cleanup these comments once/if you do something with those variables.

exit_code = 1  # The default exit code. 
#! Change it in any function/command that should clealy exit the bot or cause a restart.
#! Refer to the end of this file for the proper values for `run.sh`.

debug_mode = False  # Controls the error messages in case the bot exits from an exception.
#* This variable controls the error handling at the end of the file.


# --- Bot setup ---

# Defining the intents
intents = discord.Intents.default()

member_cache = discord.MemberCacheFlags.from_intents(intents)

bot = commands.Bot(
    command_prefix=opt.prefix,
    case_insensitive=True,
    intents=intents,
    member_cache_flags=member_cache)


# --- Commands ---


# --- Events ---

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user} - {bot.user.id}")
    print("------")


# --- Run ---

try:
    bot.run(keys.discord_token)

except discord.LoginFailure as ex:
    # Miscellaneous authentications errors: borked token and co
    if debug_mode:
        raise
    raise SystemExit("Error: Failed to authenticate: {}".format(ex))

except discord.ConnectionClosed as ex:
    # When the connection to the gateway (websocket) is closed
    if debug_mode:
        raise
    raise SystemExit("Error: Discord gateway connection closed: [Code {}] {}".format(ex.code, ex.reason))

except ConnectionResetError as ex:
    # More generic connection reset error
    if debug_mode:
        raise
    raise SystemExit("ConnectionResetError: {}".format(ex))


# --- Exit ---
# Codes for the wrapper shell script:
# 0 - Clean exit, don't restart
# 1 - Error exit, [restarting is up to the shell script]
# 42 - Clean exit, do restart

raise SystemExit(exit_code)

#!/usr/bin/env python3
"""
Copyright (c) 2021 0x5c, classabbyamp
Released under the MIT License
"""


import re
import subprocess
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

import jinja2
from jinja2 import Template

from rich.console import Console
from rich.prompt import Prompt, Confirm


jinja_env = jinja2.Environment(
    trim_blocks=True,
    lstrip_blocks=True,
    loader=jinja2.FileSystemLoader(Path("./quickbot")),
)


copyright_header_template = Template(
    '''
    """
    {{ filename }}
    ---
    Copyright (C) {{ copyright.year }} {{ copyright.holder }}

    {% if copyright.spdx %}
    SPDX-License-Identifier: {{ copyright.spdx }}
    {% elif copyright.licence %}
    {{ copyright.licence }}
    {% endif %}
    """
    '''
)


con = Console()
err_con = Console(stderr=True, style="red")


@dataclass
class BotInfo:
    name: Optional[str] = None
    description: Optional[str] = None
    target_ver: Optional[str] = None


@dataclass
class CopyrightInfo:
    year: Optional[str] = None
    holder: Optional[str] = None
    licence: Optional[str] = None
    spdx: Optional[str] = None


@dataclass
class DockerInfo:
    prebuilt: bool
    registry: Optional[str] = None
    user: Optional[str] = None
    image: Optional[str] = None


@dataclass
class GitInfo:
    namespace: Optional[str] = None
    repo: Optional[str] = None


def get_git_details() -> GitInfo:
    try:
        completed = subprocess.run(["git", "remote", "get-url", "origin"], check=True, timeout=1, capture_output=True)
    except (OSError, subprocess.TimeoutExpired, subprocess.SubprocessError):
        return (None, None)
    origin_url = completed.stdout.decode().strip().lower()
    github_urls = ("http://github.com/", "https://github.com/", "ssh://git@github.com/", "git@github.com:")
    if not origin_url.startswith(github_urls) and origin_url.endswith(".git"):
        return (None, None)
    pair = origin_url.removeprefix(github_urls[0]) \
                     .removeprefix(github_urls[1]) \
                     .removeprefix(github_urls[2]) \
                     .removeprefix(github_urls[3]) \
                     .removesuffix(".git")
    print(f"{pair=}", type(pair))
    return GitInfo(*pair.split("/"))


def get_docker_details(git: GitInfo) -> DockerInfo:
    prebuilt = Confirm.ask("Generate documentation about prebuilt images?", console=con)
    if prebuilt:
        registry = Prompt.ask("What registry do you want to use?", default="ghcr.io", console=con)
        user = Prompt.ask("What user/namespace will the package be listed under?", default=git.namespace, console=con)
    else:
        registry = None
        user = None
    image = Prompt.ask("What will the package be called?", default=git.repo, console=con)

    return DockerInfo(
        prebuilt=prebuilt,
        registry=registry,
        user=user,
        image=image,
    )


def fill_template(name: str, **vars) -> str:
    try:
        template = jinja_env.get_template(name)
        return template.render(**vars)
    except jinja2.exceptions.TemplateError as e:
        err_con.print(e)
        raise SystemExit(1)


if __name__ == "__main__":
    git_info = get_git_details()
    docker_info = get_docker_details(git_info)

    templates = {
        "docker/README-DOCKER.md": {"docker": docker_info, "bot": "qrm2"},
        "github_workflows/docker.yml": {"docker": docker_info, "git": git_info},
    }

    for t, v in templates.items():
        print(fill_template(t, **v))

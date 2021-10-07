# A minimal Dockerfile for painless discord bots.
# v2.0.0
# Copyright (c) 2021 classabbyamp, 0x5c
# Released under the terms of the MIT license.
# Part of:
# https://github.com/0x5c/quick-bot-no-pain


FROM voidlinux/voidlinux

COPY . /app
WORKDIR /app

ENV PYTHON_BIN python3

RUN \
    echo "**** update packages ****" && \
    xbps-install -Suy && \
    echo "**** install system packages ****" && \
    # NOTE: if you have buildtime dependencies,
    # add your packages between the quotes in the following line
    export build_deps='' && \
    # NOTE: if you have runtime dependencies,
    # add your packages between the quotes in the following line
    export runtime_deps='' && \
    export runtime_pkgs='${runtime_deps} python3-pip python3' && \
    xbps-install -y $build_deps $runtime_pkgs && \
    echo "**** install pip packages ****" && \
    pip3 install -U pip setuptools wheel && \
    pip3 install -r requirements.txt && \
    echo "**** clean up ****" && \
    xbps-remove -ROy $build_deps && \
    rm -rf \
        /root/.cache \
        /tmp/* \
        /var/cache/xbps/*

# settable user and group ID, with the default being 1000:1000
ARG UID
ENV UID=${UID:-1000}
ARG GID
ENV GID=${GID:-1000}
USER $UID:$GID

CMD ["/bin/sh", "run.sh", "--pass-errors", "--no-botenv"]

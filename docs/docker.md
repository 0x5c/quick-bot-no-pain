# Quick bot, No pain / **Docker files**

Minimal dockerfile and instructions for using it, [almost] ready to ship.


## Included files

| File               | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `Dockerfile`       | Minimal dockerfile for running your bot, uses `run.sh`. |
| `README-DOCKER.md` | Template for instructions to run your bot through docker. |
| `.dockerignore`    | Docker ignore file.                                       |


## Usage

### `Dockerfile`

The dockerfile, as-is, should be ready to use for a bot with no additional dependencies. Modify it to fit the needs of your bot.

Usage of the dockerfile itself is documented in `README-DOCKER.md`.

> Publishing a prebuilt image on the Docker Hub is extensively documented elsewhere, and is outside the scope of these instructions. However, the required files are present in this repository.

### `README-DOCKER.md`

The instructions are provided as a fairly complete template. Remove or uncomment the commented blocks, and replace `{{bot}}`, `{{user}}`, and `{{image}}` with the appropriate values.

### `.dockerignore`

The dockerignore file is to be expanded with any new file/directory that should not be included in the image.

> The dockerignore file serves as a way to excludes files and directories from the image. While commonly omitted from projects, it is best practice and helps lowering the building time and image size.


## Changelog

```md
## [1.0.0] - 2019-12-23
### Added
- Dokerfile
- Docker instructions
- dockerignore file
```

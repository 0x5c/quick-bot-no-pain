# TODO

- Ignore files
- All docs
- Finishing the bootstrap script
- Help in run.sh

## Templating
- `docker/`
  - .dockerignore ✅
    - no template
  - Dockerfile ✅
    - no template
  - README-DOCKER.md ✅
    - bot, docker
- `docs/`
  - docker.md
  - makefile.md
  - run.sh.md
  - skeleton.md
  - workflows.md
- `github_workflows/`
  - docker.yml ✅
    - NO TEMPLATE, but only copy if using ghcr
  - linting.yml
    - template hard, but by default runs lint on py3.9. change to `{{ bot.target_ver }}`?
  - release.yml ✅
    - no template
- `makefile/`
  - Makefile
- `run_script/`
  - run.sh
- `skeleton_files/`
  - .gitignore
  - dev-requirements.txt
  - main.py
  - README.md ✅
    - bot, copyright, docker
  - requirements.txt
- `templates/data/`
  - keys.py
  - options.py


### Need
- Copyright
  - Year
  - Holder
  - Licence
    - Name
    - ?SPDX
- Bot (move all current refs to bot.name)
  - Short description
  - Name
  - Authors? (same as copyright?)
  - target python ver

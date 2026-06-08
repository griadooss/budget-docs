# Virtualenv note

The Python virtualenv (`.venv/`, ~141 MB) was **removed on 2026-06-08** during a
`~/Workdir` cleanup to reclaim disk space. It holds no project source - only
installed packages - so it is safe to delete and regenerate at any time.

This is an [MkDocs](https://www.mkdocs.org/) project (see `mkdocs.yml`).

## Recreate the environment

Run these commands (indented lines below are the commands to type):

    cd ~/Workdir/budget-docs
    python -m venv .venv
    source .venv/bin/activate
    pip install mkdocs

(Install any theme/plugins listed in mkdocs.yml too - this project uses
mkdocs-material.)

Then serve the docs locally with:

    mkdocs serve

The live preview is then available at http://127.0.0.1:8000

Note: `.venv/` is git-ignored (see `.gitignore`) and should never be committed.

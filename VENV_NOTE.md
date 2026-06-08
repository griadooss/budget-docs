# Virtualenv note

The Python virtualenv (`.venv/`, ~141 MB) was **removed on 2026-06-08** during a
`~/Workdir` cleanup to reclaim disk space. It holds no project source — only
installed packages — so it is safe to delete and regenerate at any time.

This is an [MkDocs](https://www.mkdocs.org/) project (see `mkdocs.yml`).

## Recreate the environment

```bash
cd ~/Workdir/budget-docs
python -m venv .venv
source .venv/bin/activate
pip install mkdocs            # plus any theme/plugins listed in mkdocs.yml
```

Then serve the docs locally:

```bash
mkdocs serve     # live preview at http://127.0.0.1:8000
```

`.venv/` is git-ignored (see `.gitignore`) and should never be committed.

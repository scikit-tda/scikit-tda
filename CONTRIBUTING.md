# Contributing

Thank you for your interest in contributing to a scikit-tda library! Here are some
guidelines to help you orient yourself as you submit your PR. 

## Workflow
Most contributions start from Issues, but you may also open a pull request (PR) directly. Here’s a quick summary:
- **Found a bug or want a feature?** Open an Issue and describe the problem or request in detail.
- **Ready to contribute code?** Open a PR with your changes and include a detailed description of what you did.
- **Discussion:** We’ll work with you to clarify bugs, documentation mistakes, or feature requests.
- **Review:** PRs are reviewed by maintainers. Please respond to feedback promptly.

## Installation

Whether installing for an end-user or a developer, we strongly recommend the use of [python virtualenvs](https://docs.python.org/3/library/venv.html), [conda environments](https://www.anaconda.com/docs/getting-started/working-with-conda/environments), or [uv venvs](https://docs.astral.sh/uv/pip/environments/). Any of these will help keep your python version and the versions of this package's dependencies isolated from those of other projects.

Once you have your environment settled, run

```
pip install -e .
```

from the directory of the package to install an editable version of the package. This will allow you to make changes to the source code and see their effect without having to constantly re-install the package. Read more about this [here](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).


### Developer installation

If you are contributing, you might want more than just the base installation. The above command can be modified to install dependencies helpful during development. For example

```
pip install -e ".[docs, testing, examples]"
```
would install the core project dependencies as well as those listed in the `docs`, `testing`, and `examples` tables in `pyproject.toml`. All optional dependencies are listed as tables under `[project.optional-dependencies]` in the project's `pyproject.toml` file.

## Changelogs and Versioning

We attempt (or are in the process of) maintaining changelogs for each project in scikit-tda. 
As the code evolves, this file should be updated with information about new features added, 
bug fixes, and deprecations. Changelogs will be formatted according to the 
[Keep a changelog](https://keepachangelog.com/en/1.0.0/) with entries indexed on date and version number. 

Version numbers are stored in either `src/<package_name>/_version.py` or 
`<package_name>/_version.py` within each package. We 
follow [semantic versioning](https://semver.org/) for all packages and releases.

## Linting

We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting code. Install Ruff
in your environment with `pip install ruff`.

Linting refers to a static analysis of the codebase to check for efficient and compliant Python code. 
The default rules are documented in each project's `pyproject.toml` file. Linting can be 
performed from the command line with `ruff check`. Certain errors can be automatically 
fixed by ruff with `ruff check --fix`. 

Formatting refers to adjusting the physical appearance of the code by adding new lines, commas,
etc. without modifying the intent or logic. Ruff can automatically format a specific file with
`ruff format <file.py>` or everything in a directory with `ruff format <path>/<to>/<dir>`. The
current directory can be formatted with `ruff format .` or more simply `ruff format`.

## Code Style
- Follow [PEP8](https://peps.python.org/pep-0008/) guidelines.
- Use [Numpy style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html) for all functions and classes.
- Add type hints where possible.

## Documentation

We use sphinx to build the docs. Documentation for each repository is stored in `docs/`. 
Individual pages 
of documentation are stored as jupyter notebooks with `docs/` or a subdirectory. 
The docs should build on each push to a PR and can be viewed in the PR by clicking on 
the job which appears as a comment on the PR. 

If you add features or change APIs, please update the documentation and add or update relevant tests.

## Testing

We use `pytest` to verify (or attempt to) correctness. A good PR should also include unit tests which 
come as close as possible to covering the added lines of code. Tests are stored in the `test/` directory
and can be run by executing `pytest` from the command line within the directory. 

## Continuous Integration (CI)

All PRs are checked for lint, tests, and documentation builds via CI. Please ensure your code passes all checks before requesting review.

## Contact & Help

For questions, open an Issue or make a post in a Discussions section. We're always looking for new
contributions and we are happy to help in any way we can. Thanks again!
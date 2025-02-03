# How to use this template

Prerequisites: `uv` instalado

## Setup
1. After creating your repository from the template.
2. With uv installed, start a new project in the root of the repository:`uv init <project_name>`. This will create a `pyproject.toml` file and a `src/<project_name>` folder. This folder contains a file `__init__.py` which makes it a python module that will be installed in the scope of the project's virtual environment.

## Adding dependencies
The recommended way to add dependencies to the `uv` project is via the `uv add <package>` command. If the dependency is not on the current library, but only on the development environment, such as `pytest` or `jupyterlab`, simply include the `--dev` flag after `add`: `uv add --dev pytest`
See the `uv` documentation for more information.

## Leveraging pre-commit for Code Quality Assurance
`pre-commit` is a powerful tool used to manage and maintain pre-commit hooks. These hooks are automated checks that run before each commit, ensuring that your code adheres to defined standards and helping to prevent common issues. Integrating pre-commit into your workflow can significantly enhance the code quality and consistency of your project. Prior to installing pre-commit, make sure that your repository is a github repo.

`uv add --dev pre-commit`

### Configure Pre-Commit Hooks

Create a [`.pre-commit-config.yaml`](../.pre-commit-config.yaml) file at the root of your repository. In this file,
specify the hooks you want to use. For example:

```yaml
repos:
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.9.4
    hooks:
      - id: ruff
        args:
          - --fix
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.950
    hooks:
      - id: mypy
        additional_dependencies:
          - "types-pytz"

  - repo: https://github.com/kynan/nbstripout
    rev: 0.8.1
    hooks:
      - id: nbstripout
        files: ".ipynb"

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
        exclude: ./tests/
      - id: end-of-file-fixer
        exclude: ./tests/
      - id: check-yaml
      - id: check-toml

ci:
  autofix_commit_msg: 🎨 [pre-commit.ci] Auto format from pre-commit.com hooks
  autoupdate_commit_msg: ⬆ [pre-commit.ci] pre-commit autoupdate
```

### Install hooks

Install to set up the git hook scripts. This command installs the pre-commit script into your `.git/hooks/pre-commit`.

```bash
pre-commit install
```

### Running pre-commit for check-ups

```bash
pre-commit run --all-files
```


### How Pre-Commit Enhances Your Workflow

- **Automated Code Quality Checks:** Before each commit, pre-commit runs the configured hooks, automatically checking your code for formatting errors, trailing whitespaces, syntax errors in YAML files, and more.
- **Consistency Across the Team:** By including the `.pre-commit-config.yaml` file in your repository, you ensure that every contributor adheres to the same coding standards, enhancing consistency and reducing code review time.
- **Customisation and Extensible:** pre-commit supports a wide range of hooks for various languages and frameworks. You can customize it to suit the specific needs of your project, including setting up hooks for Python formatting (like flake8, black, isort) and more.

Integrating pre-commit into your Python project setup brings a structured approach to code quality.
It automates the enforcement of coding standards, leading to cleaner, more maintainable, and error-free code.
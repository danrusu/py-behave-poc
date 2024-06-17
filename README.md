# py-behave-poc

Python - Behave POC

### Create Virtual Environment

```bash
python -m venv venv
source venv/scripts/activate
#deactivate
```

- from VSCode

```text
CTRL + ALT + P => Python: Select Interpreter => (venv)
```

### Install dependencies

```bash
pip install pipenv
pipenv install
```

### [Behave config](./behave.ini)

### Run Behave tests

```bash
behave src/features
```

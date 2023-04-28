# upy-error

![GitHub Org's stars](https://img.shields.io/github/stars/UpyExplorer?label=LinuxProfile&style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/upy-error)
![PyPI](https://img.shields.io/pypi/v/upy-error)
![GitHub last commit](https://img.shields.io/github/last-commit/UpyExplorer/upy-error)

---

- **Documentation**: [https://github.com/UpyExplorer/upy-error](https://github.com/UpyExplorer/upy-error)
- **Source Code**: [https://github.com/UpyExplorer/upy-error](https://github.com/UpyExplorer/upy-error)

---

## How to install?

```python
pip install upy-error

```
## How to use?

```python
# Import the package
from upy_error import format_exception
```

### Exception example with (log)

```python
try:
    print(x)
except Exception as error:
    # Using the function to process the error with the 'logging' package.
    format_exception(error=error, log=True)
```

**Output:**

```shell
==========================================
2022-07-23 00:13:37,577 ERROR 
UpyError: 
  File "test_upy_error.py", line 4, in <module>
    print(x)
NameError: name 'x' is not defined
==========================================
```

### Exception example with (print)

```python
try:
    1 / 0
except Exception as error:
    # Using the function to return the error in string format.
    print(format_exception(error=error))
```

**Output:**
```shell
UpyError: 
  File "test_upy_error.py", line 11, in <module>
    1 / 0
ZeroDivisionError: division by zero
```

## Commit Style

- ⚙️ FEATURE
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 PyPI
- ❤️️ TEST
- ⬆️ CI/CD
- ⚠️ SECURITY

## License

Distributed under the MIT License. See `LICENSE` for more information.

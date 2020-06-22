Python MaskProcessor
====================
[![Python Version](https://img.shields.io/pypi/pyversions/maskprocessor)](https://pypi.org/project/maskprocessor)
[![Version](https://img.shields.io/pypi/v/maskprocessor)](https://pypi.org/project/maskprocessor)
[![License](https://img.shields.io/pypi/l/maskprocessor)](LICENSE)

Python maskprocessor implementation which inspired by [hashcat maskprocessor](https://github.com/hashcat/maskprocessor)


Installation
------------
```sh
pip install maskprocessor
```

Usage
-----

Print help
```sh
maskprocessor --help  # or -h
```

Via command line
```sh
$ maskprocessor '?d'
0
1
2
3
4
5
6
7
8
9
```

Import as python module

```python
>>> from maskprocessor import maskprocessor as maskproc
>>> g = maskproc('?l')
>>> print(next(g))
a
>>> print(next(g))
b
```


License
-------
[MIT License](LICENSE)

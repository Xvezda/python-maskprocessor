PY2 = python
PY = $(PY2)
PY3 = python3
TWINE = twine
PACKAGE_NAME = maskprocessor
VERSION_FILE = $(PACKAGE_NAME)/_version.py
PACKAGE_VERSION = $(shell \
	sed -E "s/__version__ = [\"']([^\"']+)[\"']/\1/" $(VERSION_FILE))
DIST_DIR = dist
DIST_FILES = $(wildcard $(DIST_DIR)/$(PACKAGE_NAME)-$(PACKAGE_VERSION)*)


all: py2dist py3dist

dist:
	$(PY) setup.py sdist bdist_wheel

py2dist:
	$(PY2) setup.py sdist bdist_wheel

py3dist:
	$(PY3) setup.py sdist bdist_wheel

check:
	$(TWINE) check $(DIST_DIR)/$(PACKAGE_NAME)-$(PACKAGE_VERSION)*

publish: all check
	$(TWINE) upload $(DIST_FILES)

test:
	echo $(DIST_FILES)

clean:
	$(PY) setup.py clean

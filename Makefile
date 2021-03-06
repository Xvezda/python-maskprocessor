PY2 = python
PY = $(PY2)
PY3 = python3
TWINE = twine
SED = sed -n -E
PACKAGE_NAME = maskprocessor
VERSION_FILE = $(PACKAGE_NAME)/__version__.py
PACKAGE_VERSION = $(shell \
	$(SED) "s/__version__ = [\"']([^\"']+)[\"']/\1/p" $(VERSION_FILE))
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

pkg_version:
	@echo $(PACKAGE_VERSION)

test:
	# echo $(DIST_FILES)
	$(PY) -m $(PACKAGE_NAME) '?l'
	# $(PY) -m $(PACKAGE_NAME) --custom-charset1='?l?d' '?1'
	$(PY) -m $(PACKAGE_NAME) -1='?l?d' '?1'
	$(PY) -m $(PACKAGE_NAME) 'password?d'
	$(PY) -m $(PACKAGE_NAME) -1='?dabcdef' -2='?l?u' '?1?2'
	$(PY) -m $(PACKAGE_NAME) -1='efghijklmnop' '?1?1?1'

clean:
	$(PY) setup.py clean

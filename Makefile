clean::
	find . -iname '*.pyc' | xargs rm -f
	rm -rf RPMS SRPMS SOURCES BUILDROOT BUILD

prepare:
	mkdir -p RPMS SRPMS SOURCES
	tar --exclude=".svn" --exclude="*.sw?" --exclude="*.pyc" -czf SOURCES/python-json-logger.tar.gz src/

rpmbuild: clean prepare
	rpmbuild -ba --define "%_topdir $$(pwd)" SPECS/python-json-logger.spec

rpm: clean prepare
	mbt

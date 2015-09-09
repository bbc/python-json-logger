%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif


Name: python-json-logger
Version: 0.1.3
Release: 3%{?dist}
Group: Development/Tools
Summary: JSON formatter for python's logging module
License: https://github.com/bbc/python-json-logger/blob/master/LICENSE
Source: python-json-logger.tar.gz
Requires: python
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch


%description
JSON formatter for python's logging module


%prep
%setup -q -n src


%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{python_sitelib}/
cp -r pythonjsonlogger/ $RPM_BUILD_ROOT%{python_sitelib}/


%clean
rm -rf $RPM_BUILD_ROOT


%files

%defattr(644, root, root, 755)
%{python_sitelib}/pythonjsonlogger/

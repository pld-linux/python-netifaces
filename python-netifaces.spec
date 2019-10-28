#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	netifaces
Summary:	Python library to retrieve information about network interfaces
Name:		python-%{module}
Version:	0.10.5
Release:	3
License:	MIT
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/n/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	5b4d1f1310ed279e6df27ef3a9b71519
URL:		https://alastairs-place.net/projects/netifaces/
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a cross platform API for getting address
information from network interfaces.

%package -n python3-%{module}
Summary:	Python library to retrieve information about network interfaces
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
This package provides a cross platform API for getting address
information from network interfaces.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%{?with_tests:%{__python} setup.py test}
%endif

%if %{with python3}
%py3_build
%{?with_tests:%{__python3} setup.py test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{py_sitedir}/netifaces.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/netifaces-*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitedir}/netifaces*.so
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%endif

#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	netifaces
Summary:	Python library to retrieve information about network interfaces
Name:		python-%{module}
Version:	0.8
Release:	3
License:	MIT
Group:		Development/Languages/Python
Source0:	http://alastairs-place.net/projects/netifaces/%{module}-%{version}.tar.gz
# Source0-md5:	e57e5983f4c286fac5f8068fbfc5c873
URL:		http://alastairs-place.net/projects/netifaces/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a cross platform API for getting address
information from network interfaces.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/netifaces.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/netifaces-*.egg-info
%endif

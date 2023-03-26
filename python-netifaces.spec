#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	netifaces
Summary:	Python library to retrieve information about network interfaces
Summary(pl.UTF-8):	Biblioteka Pythona do pobierania informacji o interfejsach sieciowych
Name:		python-%{module}
Version:	0.11.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/netifaces/
Source0:	https://files.pythonhosted.org/packages/source/n/netifaces/%{module}-%{version}.tar.gz
# Source0-md5:	3146dcb3297dd018ae5eb9a52b440419
URL:		https://pypi.org/project/netifaces/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	rpm-pythonprov
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a cross platform API for getting address
information from network interfaces.

%description -l pl.UTF-8
Ten pakiet zapewnia wieloplatformowe API do pobierania informacji o
adresach z interfejsów sieciowych.

%package -n python3-%{module}
Summary:	Python library to retrieve information about network interfaces
Summary(pl.UTF-8):	Biblioteka Pythona do pobierania informacji o interfejsach sieciowych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
This package provides a cross platform API for getting address
information from network interfaces.

%description -n python3-%{module} -l pl.UTF-8
Ten pakiet zapewnia wieloplatformowe API do pobierania informacji o
adresach z interfejsów sieciowych.

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
%doc LICENSE README.rst
%attr(755,root,root) %{py_sitedir}/netifaces.so
%{py_sitedir}/netifaces-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{py3_sitedir}/netifaces.cpython-*.so
%{py3_sitedir}/netifaces-%{version}-py*.egg-info
%endif

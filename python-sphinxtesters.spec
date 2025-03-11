#
# Conditional build:
%bcond_without	tests	# unit tests [py3 tests fail with sphinx3.x+docutils0.18 combo]
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Utilities for testing Sphinx extensions
Summary(pl.UTF-8):	Narzędzia do testowania rozszerzeń Sphinksa
Name:		python-sphinxtesters
Version:	0.2.3
Release:	7
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxtesters/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxtesters/sphinxtesters-%{version}.tar.gz
# Source0-md5:	3df3720ba757d3d8270fed5aff622852
Patch0:		%{name}-noconf.patch
URL:		https://pypi.org/project/sphinxtesters/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.4
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.4
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-Sphinx >= 1.4
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for testing Sphinx extensions.

%description -l pl.UTF-8
Narzędzia do testowania rozszerzeń Sphinksa.

%package -n python3-sphinxtesters
Summary:	Utilities for testing Sphinx extensions
Summary(pl.UTF-8):	Narzędzia do testowania rozszerzeń Sphinksa
Group:		Libraries/Python
Requires:	python3-Sphinx >= 1.4
Requires:	python3-modules >= 1:3.3

%description -n python3-sphinxtesters
Utilities for testing Sphinx extensions.

%description -n python3-sphinxtesters -l pl.UTF-8
Narzędzia do testowania rozszerzeń Sphinksa.

%prep
%setup -q -n sphinxtesters-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest sphinxtesters/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest sphinxtesters/tests
%endif
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
%{py_sitescriptdir}/sphinxtesters
%{py_sitescriptdir}/sphinxtesters-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinxtesters
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinxtesters
%{py3_sitescriptdir}/sphinxtesters-%{version}-py*.egg-info
%endif

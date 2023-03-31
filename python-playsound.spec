%define debug_package %{nil}
%global pypi_name playsound

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        2
Group:          Development/Python
Summary:        Pure Python, cross platform, single function module with no dependencies for playing sounds.
License:        MIT
URL:            https://github.com/TaylorSMarks/playsound
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

Requires: python
Requires: gstreamer1.0-plugins-base

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
Pure Python, cross platform, single function module with no dependencies for playing sounds.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/playsound-*-py*.*.egg-info
%{python_sitelib}/playsound.py

%define name %{shortname}-python
%define rel 1
%define git 0

%define libname %mklibname %name
#define develname %mklibname -d %name

%if  %{git}
%define srcname %{name}-%{git}.tar.xz
%define distname %{name}
%define release 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}.tar.bz2
%define distname %{name}-%{version}
%define release %{rel}
%endif

Name: %{shortname}-python
Version: 0.9.5.92
Release: %release
Summary: Python bindings for libcompizconfig
Group: System/X11
URL: http://www.compiz.org/
Source: http://releases.compiz-fusion.org/%{version}/%{srcname}
License: GPL

BuildRequires: compiz-devel >= %{version}
BuildRequires: libcompizconfig-devel >= %{version}
BuildRequires:  python-cython
BuildRequires:  python-devel

%description
Python bindings for libcompizconfig

#----------------------------------------------------------------------------

%package -n %{libname}
Summary: Library files for %{name}
Group: System/X11
Provides: %{name} = %{version}-%{release}
Obsoletes: beryl-settings-bindings
Obsoletes: %mklibname beryl-settings-bindings

%description -n %{libname}
Python Bindings for Beryl Settings

#----------------------------------------------------------------------------

#package -n %{develname}
#ummary: Development files from %{name}
#roup: Development/Other
#equires: %{libname} = %{version}-%{release}
#rovides: %{name}-devel = %{version}-%{release}
#bsoletes: %mklibname -d beryl-settings-bindings

#description -n %{develname}
#evelopment files relating to the Python Bindings for Beryl Settings

#----------------------------------------------------------------------------

%prep
%setup -qn %{distname}

%build
%if %{git}
  # This is a GIT snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif

# cython'ing fails w/o conversion
sed -i 's|__new__|__cinit__|g' src/compizconfig.pyx
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install -O2 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

#----------------------------------------------------------------------------

%files -n %{libname}
%{py_platsitedir}/%{shortname}.so

#files -n %{develname}
#{py_platsitedir}/%{shortname}.a
#{_libdir}/pkgconfig/%{name}.pc


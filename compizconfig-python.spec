%define shortname compizconfig
%define name compizconfig-python
%define version 0.7.8
%define rel 1
%define git 0

%define libname %mklibname %name
%define libname_devel %mklibname -d %name

%if  %{git}
%define srcname %{name}-%{git}.tar.lzma
%define distname %{name}
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}.tar.bz2
%define distname %{name}-%{version}
%define release %mkrel %{rel}
%endif

Name: %name
Version: %version
Release: %release
Summary: Python bindings for libcompizconfig
Group: System/X11
URL: http://www.compiz-fusion.org/
Source: http://releases.compiz-fusion.org/%{version}/%{srcname}
License: GPL
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: compiz-devel
BuildRequires: libcompizconfig-devel
BuildRequires: pygtk2.0-devel
BuildRequires: python-pyrex

%description
Python bindings for libcompizconfig

#----------------------------------------------------------------------------

%package -n %{libname}
Summary: Library files for %{name}
Group: System/X11
Provides: %{name} = %{version}-%{release}
Obsoletes: beryl-settings-bindings
Obsoletes: %mklibname beryl-settings-bindings

%description -n %libname
Python Bindings for Beryl Settings

#----------------------------------------------------------------------------

%package -n %{libname_devel}
Summary: Development files from %{name}
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
Requires: libcompizconfig-devel
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d beryl-settings-bindings

%description -n %{libname_devel}
Development files relating to the Python Bindings for Beryl Settings

#----------------------------------------------------------------------------

%prep
%setup -q -n %{distname}

%build
%if %{git}
  # This is a GIT snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name *.la -exec rm -f {} \;

%clean
rm -rf %buildroot

#----------------------------------------------------------------------------

%files -n %{libname}
%{py_platsitedir}/%{shortname}.so

%files -n %{libname_devel}
%{py_platsitedir}/%{shortname}.a
%{_libdir}/pkgconfig/%{name}.pc


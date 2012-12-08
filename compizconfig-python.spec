%define shortname compizconfig
%define name compizconfig-python
%define version 0.8.4
%define rel 3
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
BuildRequires: compiz-devel >= %{version}
BuildRequires: libcompizconfig-devel >= %{version}
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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-3mdv2011.0
+ Revision: 663396
- mass rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-2mdv2011.0
+ Revision: 522401
- rebuilt for 2010.1

* Thu Oct 15 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.4-1mdv2010.0
+ Revision: 457728
- New version: 0.8.4
- Harden buildrequires versions

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 0.8.2-1mdv2010.0
+ Revision: 370665
- New version 0.8.2

* Sun Feb 08 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.0-0.20090208.1mdv2009.1
+ Revision: 338486
- 0.8 pre-release snapshot

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.7.8-1mdv2009.1
+ Revision: 319154
- rebuild with python 2.6
- 0.7.8 final

* Fri Sep 12 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.8-0.20080912.1mdv2009.0
+ Revision: 284291
- New snapshot

* Sun Jul 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.7-0.20080713.1mdv2009.0
+ Revision: 234341
- New snapshot
- New version: 0.7.6

* Fri May 23 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.5-0.20080522.1mdv2009.0
+ Revision: 210157
- Update to git snapshot

* Tue Apr 08 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.4-1mdv2009.0
+ Revision: 192369
- New version 0.7.4

* Fri Mar 07 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.2-1mdv2008.1
+ Revision: 181121
- New version 0.7.2

* Mon Feb 18 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.99-0.20080218.1mdv2008.1
+ Revision: 172296
- Update to git master for new compiz

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 20 2007 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 100723
- New upstream release: 0.6.0

* Fri Oct 19 2007 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-0.20071018.1mdv2008.1
+ Revision: 100097
- Update snapshot from 0.6.0 branch for compiz 0.6.2

* Mon Aug 13 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 62612
- Official Release: 0.5.3

* Sun Aug 12 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070811.1mdv2008.0
+ Revision: 62120
- Update snapshot

* Wed Aug 01 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070801.1mdv2008.0
+ Revision: 57836
- Updated snapshot

* Sat Jul 14 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070712.2mdv2008.0
+ Revision: 52116
- Update snapshot

* Sun Jul 08 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070707.2mdv2008.0
+ Revision: 49637
- Rebuild against new libcompizconfig

* Sun Jul 08 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070707.1mdv2008.0
+ Revision: 49632
- New Snapshot 20070707
- Obsolete Beryl Settings Bindings
- Import compizconfig-python


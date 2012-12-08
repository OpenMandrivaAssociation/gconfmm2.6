%define version 2.28.2
%define release %mkrel 3

%define major	1
%define api_version 2.6

%define glibmm_version	2.6.4
%define gtkmm_version	2.4.0
%define gconf_version	2.4.0

%define pkgname gconfmm
%define libname		%mklibname %pkgname %api_version %{major}
%define develname	%mklibname -d %pkgname %api_version

Name:	 	%{pkgname}%{api_version}
Summary: 	A C++ interface for GConf library
Version: 	%version
Release: 	%release
#gw lib is LGPL, tool is GPL
License: 	LGPLv2+ and GPLv2+
Group:   	System/Libraries
Source:  	ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
Patch0:		gconfmm-2.12.0-64bit-fixes.patch
URL:     	http://gtkmm.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libGConf2-devel >= %{gconf_version}
BuildRequires:	dbus-glib-devel
BuildRequires:	glibmm2.4-devel >= %{glibmm_version}
BuildRequires:	gtkmm2.4-devel >= %{gtkmm_version}
BuildRequires:	gnome-common
BuildRequires:	doxygen

%description
This package provides a C++ interface for GConf, a configuration data
storage mechanism to ship with GNOME.  It is a subpackage of the
gnomemm project, which provides a C++ interface for GNOME libraries.


%package	-n %{libname}
Summary:	%{summary}
Group:		%{group}

%description -n %{libname}
This package provides a C++ interface for GConf, a configuration data
storage mechanism to ship with GNOME.  It is a subpackage of the
gnomemm project, which provides a C++ interface for GNOME libraries.


%package	-n %develname
Summary:	Headers and development files of GConf 2 C++ wrapper
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libgconfmm%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes: %mklibname -d %pkgname %api_version 1

%description -n %develname
This package contains the headers and various development files needed,
when compiling or developing programs which want GConf 2 C++ wrapper.

%package	doc
Summary:	Documentation of %{pkgname} library
Group:		Books/Other

%description doc
This package provides API documentation of %{pkgname} library.


%prep
%setup -q -n %pkgname-%version
%patch0 -p1 -b .64bit-fixes

%build
NOCONFIGURE=yes gnome-autogen.sh
%configure2_5x --enable-static
%make 

%install
%makeinstall_std

%files -n %{libname}
%defattr(-, root, root)
%doc COPYING.LIB
%{_libdir}/libgconfmm-%{api_version}.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%doc %_datadir/doc/gconfmm-%api_version
%doc %_datadir/devhelp/books/gconfmm-%api_version
%{_includedir}/*
%{_libdir}/%{pkgname}-%{api_version}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
%{_libdir}/*.so

%files doc
%defattr(-, root, root)
%doc docs/reference/html




%changelog
* Wed May 04 2011 Funda Wang <fwang@mandriva.org> 2.28.2-2mdv2011.0
+ Revision: 665772
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sun Jul 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.2-1mdv2011.0
+ Revision: 550777
- new version
- fix documentation build

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-2mdv2010.1
+ Revision: 521479
- rebuilt for 2010.1

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446589
- update to new version 2.28.0

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.24.0-2mdv2010.0
+ Revision: 424554
- rebuild

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286535
- new version

* Wed Sep 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.1-1mdv2009.0
+ Revision: 283474
- fix build deps
- new version
- update license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.22.0-2mdv2009.0
+ Revision: 221041
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183000
- new version

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.20.0-2mdv2008.1
+ Revision: 150095
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 85537
- new version
- new devel name
- bump deps

* Mon Sep 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 84160
- new version
- new devel name
- drop useless provides


* Sat Mar 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 140341
- Import gconfmm2.6

* Sat Mar 10 2007 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
- unpack patch
- new version

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Sat Jun 17 2006 Götz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- drop patch 1
- New release 2.14.2

* Thu Jun 08 2006 Götz Waschk <waschk@mandriva.org> 2.14.1-1mdv2007.0
- patch to fix the build
- New release 2.14.1

* Tue Apr 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- New release 2.14.0
- use mkrel

* Sun Oct 09 2005 Götz Waschk <waschk@mandriva.org> 2.12.0-1mdk
- rediff the patch
- New release 2.12.0

* Wed Aug 24 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.10.0-2mdk
- 64-bit fixes

* Thu Mar 10 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.10.0-1mdk
- New release 2.10.0

* Tue Nov 30 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.8.1-1mdk
- New release 2.8.1

* Wed Nov 10 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.0-1mdk
- reenable libtoolize
- New release 2.8.0

* Fri Jun 18 2004 Abel Cheung <deaddog@deaddog.org> 2.6.1-2mdk
- Rebuild with new gcc

* Sat May 15 2004 Abel Cheung <deaddog@deaddog.org> 2.6.1-1mdk
- New version

* Thu Apr 29 2004 Abel Cheung <deaddog@deaddog.org> 2.6.0-1mdk
- New major release


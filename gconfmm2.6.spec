%define major	1
%define api_version 2.6

%define glibmm_version	2.6.4
%define gtkmm_version	2.4.0
%define gconf_version	2.4.0

%define	pkgname	gconfmm
%define	libname	%mklibname %{pkgname} %{api_version} %{major}
%define	devname	%mklibname -d %{pkgname} %{api_version}

Name:	 	%{pkgname}%{api_version}
Summary: 	A C++ interface for GConf library
Version:	2.28.3
Release: 	2
#gw lib is LGPL, tool is GPL
License: 	LGPLv2+ and GPLv2+
Group:   	System/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz
Patch0:		gconfmm-2.12.0-64bit-fixes.patch
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	gnome-common
BuildRequires:	doxygen

%description
This package provides a C++ interface for GConf, a configuration data
storage mechanism to ship with GNOME.  It is a subpackage of the
gnomemm project, which provides a C++ interface for GNOME libraries.


%package -n	%{libname}
Summary:	%{summary}
Group:		%{group}

%description -n	%{libname}
This package provides a C++ interface for GConf, a configuration data
storage mechanism to ship with GNOME.  It is a subpackage of the
gnomemm project, which provides a C++ interface for GNOME libraries.


%package -n	%{devname}
Summary:	Headers and development files of GConf 2 C++ wrapper
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libgconfmm%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%mklibname -d %pkgname %api_version 1

%description -n	%{devname}
This package contains the headers and various development files needed,
when compiling or developing programs which want GConf 2 C++ wrapper.

%package	doc
Summary:	Documentation of %{pkgname} library
Group:		Books/Other

%description doc
This package provides API documentation of %{pkgname} library.


%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .64bit-fixes~

%build
NOCONFIGURE=yes gnome-autogen.sh
%configure2_5x --enable-static
%make 

%install
%makeinstall_std

%files -n %{libname}
%doc COPYING.LIB
%{_libdir}/libgconfmm-%{api_version}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%doc %{_datadi}r/doc/gconfmm-%api_version
%doc %{_datadir}/devhelp/books/gconfmm-%api_version
%{_includedir}/*
%{_libdir}/%{pkgname}-%{api_version}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.*a
%{_libdir}/*.so

%files doc
%doc docs/reference/html

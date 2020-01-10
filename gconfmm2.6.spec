%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	pkgname	gconfmm
%define api	2.6
%define major	1
%define	libname	%mklibname %{pkgname} %{api} %{major}
%define	devname	%mklibname -d %{pkgname} %{api}

Name:	 	%{pkgname}%{api}
Summary:	A C++ interface for GConf library
Version:	2.28.3
Release:	14
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
Url:		http://gtkmm.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{url_ver}/%{pkgname}-%{version}.tar.xz
Patch0:		gconfmm-2.12.0-64bit-fixes.patch

BuildRequires:	doxygen
BuildRequires:	gnome-common
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gtkmm-2.4)

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
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-doc < 2.28.3-3

%description -n	%{devname}
This package contains the headers and various development files needed,
when compiling or developing programs which want GConf 2 C++ wrapper.

%prep
%setup -qn %{pkgname}-%{version}
%autopatch -p1
NOCONFIGURE=yes gnome-autogen.sh

%build
%configure2_5x \
	--disable-static
%make 

%install
%makeinstall_std

%files -n %{libname}
%doc COPYING.LIB
%{_libdir}/libgconfmm-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%doc %{_datadir}/doc/gconfmm-%{api}
%doc %{_datadir}/devhelp/books/gconfmm-%{api}
%doc docs/reference/html
%{_includedir}/*
%{_libdir}/%{pkgname}-%{api}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

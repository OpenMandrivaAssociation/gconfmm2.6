%define version 2.24.0
%define release %mkrel 2

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
%configure2_5x --enable-static
%make 

### Build doc
pushd docs/reference
  perl -pi -e 's/^(HAVE_DOT.*=) YES/$1 NO/' Doxyfile
  make all
popd

%install
rm -rf %{buildroot}
%makeinstall_std
find %buildroot -name \*.la|xargs chmod 644

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc COPYING.LIB
%{_libdir}/libgconfmm-%{api_version}.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/%{pkgname}-%{api_version}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so

%files doc
%defattr(-, root, root)
%doc docs/reference/html



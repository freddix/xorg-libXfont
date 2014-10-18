Summary:	X font library used by the X server
Name:		xorg-libXfont
Version:	1.5.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfont-%{version}.tar.bz2
# Source0-md5:	664629bfa7cdf8b984155019fd395dcb
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libfontenc-devel
BuildRequires:	xorg-xtrans-devel
BuildRequires:	xorg-proto >= 7.7
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X font library used by the X server.

%package devel
Summary:	Header files for libXfont library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X font library used by the X server.

This package contains the header files needed to develop programs that
use libXfont.

%prep
%setup -qn libXfont-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXfont.so.?
%attr(755,root,root) %{_libdir}/libXfont.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXfont.so
%{_includedir}/X11/fonts/*.h
%{_pkgconfigdir}/xfont.pc


Summary:	Map widget for Clutter
Summary(pl.UTF-8):	Widget mapy dla Cluttera
Name:		libchamplain
Version:	0.8.2
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libchamplain/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	6018dbd6a52906c1ff73ba9cf2c60c81
URL:		http://projects.gnome.org/libchamplain/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	clutter-devel >= 1.2.0
BuildRequires:	clutter-gtk-devel >= 0.10.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	glibc-misc
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 0.6.3
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	libsoup-gnome-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	memphis-devel >= 0.2.1
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	sqlite3-devel >= 3.0
BuildRequires:	xorg-proto-glproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libchamplain is a C library aimed to provide a ClutterActor to display
rasterized maps.

%description -l pl.UTF-8
Libchamplain jest biblioteką C, której celem jest dostarczenie
interfejcu ClutterActor do wyświetlania rastrowych map.

%package devel
Summary:	Header files for the libchamplain library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libchamplain
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	clutter-devel >= 1.0.0
Requires:	clutter-gtk-devel >= 0.10.0
Requires:	glib2-devel >= 1:2.16.0
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	memphis-devel >= 0.2.1
Requires:	sqlite3-devel >= 3.0

%description devel
Header files for the libchamplain library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libchamplain.

%package apidocs
Summary:	libchamplain API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libchamplain
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libchamplain API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libchamplain

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--disable-silent-rules \
	--enable-gtk \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libchamplain-0.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchamplain-0.8.so.1
%attr(755,root,root) %{_libdir}/libchamplain-gtk-0.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchamplain-gtk-0.8.so.1
%{_libdir}/girepository-1.0/Champlain-0.8.typelib
%{_libdir}/girepository-1.0/GtkChamplain-0.8.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libchamplain-0.8.so
%attr(755,root,root) %{_libdir}/libchamplain-gtk-0.8.so
%{_libdir}/libchamplain-0.8.la
%{_libdir}/libchamplain-gtk-0.8.la
%{_includedir}/libchamplain-0.8
%{_includedir}/libchamplain-gtk-0.8
%{_pkgconfigdir}/champlain-0.8.pc
%{_pkgconfigdir}/champlain-gtk-0.8.pc
%{_pkgconfigdir}/champlain-memphis-0.8.pc
%{_datadir}/gir-1.0/Champlain-0.8.gir
%{_datadir}/gir-1.0/GtkChamplain-0.8.gir
%{_datadir}/vala/vapi/*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libchamplain
%{_gtkdocdir}/libchamplain-gtk

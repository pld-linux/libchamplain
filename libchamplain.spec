#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	vala		# do not build Vala API
#
Summary:	Map widget for Clutter
Summary(pl.UTF-8):	Widget mapy dla Cluttera
Name:		libchamplain
Version:	0.12.3
Release:	3
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libchamplain/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	f0d63225c2efa8b367ebf205fa40862a
URL:		http://projects.gnome.org/libchamplain/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	clutter-devel >= 1.2.0
BuildRequires:	clutter-gtk-devel >= 0.90.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	glibc-misc
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 0.6.3
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	libsoup-gnome-devel >= 2.26.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	memphis-devel >= 0.2.1
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3.0
%{?with_vala:BuildRequires:	vala >= 0.11.0}
Requires:	cairo >= 1.4.0
Requires:	glib2 >= 1:2.16.0
Requires:	memphis >= 0.2.1
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
Requires:	clutter-devel >= 1.2.0
Requires:	clutter-gtk-devel >= 0.90.0
Requires:	glib2-devel >= 1:2.16.0
Requires:	gtk+3-devel >= 3.0.0
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
Dokumentacja API biblioteki libchamplain.

%package -n vala-libchamplain
Summary:	libchamplain API for Vala language
Summary(pl.UTF-8):	API libchamplain dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 0.11.0

%description -n vala-libchamplain
libchamplain API for Vala language.

%description -n vala-libchamplain -l pl.UTF-8
API libchamplain dla języka Vala.

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
	--disable-silent-rules \
	--disable-static \
	--enable-gtk \
	%{__enable_disable apidocs gtk-doc} \
	%{__enable_disable vala vala} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libchamplain-0.12.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchamplain-0.12.so.0
%attr(755,root,root) %{_libdir}/libchamplain-gtk-0.12.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchamplain-gtk-0.12.so.0
%{_libdir}/girepository-1.0/Champlain-0.12.typelib
%{_libdir}/girepository-1.0/GtkChamplain-0.12.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libchamplain-0.12.so
%attr(755,root,root) %{_libdir}/libchamplain-gtk-0.12.so
%{_includedir}/libchamplain-0.12
%{_includedir}/libchamplain-gtk-0.12
%{_pkgconfigdir}/champlain-0.12.pc
%{_pkgconfigdir}/champlain-gtk-0.12.pc
%{_pkgconfigdir}/champlain-memphis-0.12.pc
%{_datadir}/gir-1.0/Champlain-0.12.gir
%{_datadir}/gir-1.0/GtkChamplain-0.12.gir

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libchamplain
%{_gtkdocdir}/libchamplain-gtk
%endif

%if %{with vala}
%files -n vala-libchamplain
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/champlain-0.12.vapi
%{_datadir}/vala/vapi/champlain-gtk-0.12.vapi
%endif

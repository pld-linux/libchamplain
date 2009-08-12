Summary:	Map widget for Clutter
Name:		libchamplain
Version:	0.3.90
Release:	1
License:	LGPL v2
Group:		Development/Libraries
Source0:	http://download.gnome.org/sources/libchamplain/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	7a09721b41cba2947bdc9ab4216e34a9
URL:		http://projects.gnome.org/libchamplain/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.4
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 0.10
BuildRequires:	gir-repository-devel
BuildRequires:	glib2-devel >= 2.16
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+2-devel >= 2.10
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libsoup-gnome-devel >= 2.26
BuildRequires:	python-devel
BuildRequires:	sqlite3-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libchamplain is a C library aimed to provide a ClutterActor to display
rasterized maps.

%package devel
Summary:	Header files for the champlain library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the champlain library.

%package apidocs
Summary:	libchamplain API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libchamplain API documentation.

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
	--enable-gtk \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_gtkdocdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libchamplain-0.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchamplain-0.3.so.3
%attr(755,root,root) %{_libdir}/libchamplain-gtk-0.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchamplain-gtk-0.3.so.3
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libchamplain-0.3.so
%attr(755,root,root) %{_libdir}/libchamplain-gtk-0.3.so
%{_libdir}/libchamplain-0.3.la
%{_libdir}/libchamplain-gtk-0.3.la
%{_includedir}/libchamplain-0.3
%{_includedir}/libchamplain-gtk-0.3
%{_pkgconfigdir}/champlain-0.3.pc
%{_pkgconfigdir}/champlain-gtk-0.3.pc
%{_datadir}/gir-1.0/*.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libchamplain
%{_gtkdocdir}/libchamplain-gtk

Summary:	Map widget for Clutter
Name:		libchamplain
Version:	0.3.3
Release:	1
License:	LGPL v2
Group:		Development/Libraries
Source0:	http://download.gnome.org/sources/libchamplain/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	af2cf557bfe5fb5cc6ce6f16e6cf7358
Patch0:		%{name}-makefile.patch
URL:		http://projects.gnome.org/libchamplain/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.4
BuildRequires:	clutter-cairo-devel >= 0.8
BuildRequires:	clutter-devel >= 0.8.4
BuildRequires:	clutter-gtk-devel >= 0.8
BuildRequires:	glib2-devel >= 2.16
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
%patch0 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
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
%attr(755,root,root) %ghost %{_libdir}/libchamplain-0.3.so.1
%attr(755,root,root) %{_libdir}/libchamplain-gtk-0.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchamplain-gtk-0.3.so.1

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

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libchamplain
%{_gtkdocdir}/libchamplain-gtk

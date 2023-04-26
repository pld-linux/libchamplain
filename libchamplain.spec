#
# Conditional build:
%bcond_without	apidocs		# API docs
%bcond_without	libsoup3	# libsoup 2.x instead of libsoup3
%bcond_without	memphis		# local rendering using libmemphis
%bcond_without	vala		# Vala API

Summary:	Map widget for Clutter
Summary(pl.UTF-8):	Widget mapy dla Cluttera
Name:		libchamplain
Version:	0.12.21
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/libchamplain/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	2b17ba53d88840f73f22ead3a905f475
Patch0:		%{name}-gtkdocdir.patch
URL:		https://wiki.gnome.org/Projects/libchamplain
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	clutter-devel >= 1.24
BuildRequires:	clutter-gtk-devel >= 1.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.68
BuildRequires:	glibc-misc
BuildRequires:	gobject-introspection-devel >= 0.6.3
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.15
%if %{with libsoup3}
BuildRequires:	libsoup3-devel >= 3.0
%else
BuildRequires:	libsoup-devel >= 2.42
%endif
%{?with_memphis:BuildRequires:	memphis-devel >= 0.2.1}
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sqlite3-devel >= 3.0
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 0.15.1}
BuildRequires:	xz
Requires:	cairo >= 1.4.0
Requires:	clutter >= 1.24
Requires:	clutter-gtk >= 1.0
Requires:	glib2 >= 1:2.68
%if %{with libsoup3}
Requires:	libsoup3 >= 3.0
%else
Requires:	libsoup >= 2.42
%endif
%{?with_memphis:Requires:	memphis >= 0.2.1}
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
Requires:	clutter-devel >= 1.24
Requires:	clutter-gtk-devel >= 1.0
Requires:	glib2-devel >= 1:2.68
Requires:	gtk+3-devel >= 3.0.0
%if %{with libsoup3}
Requires:	libsoup3-devel >= 3.0
%else
Requires:	libsoup-devel >= 2.42
%endif
%{?with_memphis:Requires:	memphis-devel >= 0.2.1}
Requires:	sqlite3-devel >= 3.0

%description devel
Header files for the libchamplain library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libchamplain.

%package static
Summary:	Static libchamplain libraries
Summary(pl.UTF-8):	Statyczne biblioteki libchamplain
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static libchamplain libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libchamplain.

%package apidocs
Summary:	libchamplain API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libchamplain
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
libchamplain API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libchamplain.

%package -n vala-libchamplain
Summary:	libchamplain API for Vala language
Summary(pl.UTF-8):	API libchamplain dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 0.15.1
BuildArch:	noarch

%description -n vala-libchamplain
libchamplain API for Vala language.

%description -n vala-libchamplain -l pl.UTF-8
API libchamplain dla języka Vala.

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	%{?with_apidocs:-Dgtk_doc=true} \
	-Dlibsoup3=%{__true_false libsoup3} \
	%{?with_memphis:-Dmemphis=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
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
%dir %{_includedir}/champlain-0.12
%{_includedir}/champlain-0.12/champlain
%{_includedir}/champlain-0.12/champlain-gtk
%{_pkgconfigdir}/champlain-0.12.pc
%{_pkgconfigdir}/champlain-gtk-0.12.pc
%{_datadir}/gir-1.0/Champlain-0.12.gir
%{_datadir}/gir-1.0/GtkChamplain-0.12.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libchamplain-0.12.a
%{_libdir}/libchamplain-gtk-0.12.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/champlain-0.12
%endif

%if %{with vala}
%files -n vala-libchamplain
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/champlain-0.12.deps
%{_datadir}/vala/vapi/champlain-0.12.vapi
%{_datadir}/vala/vapi/champlain-gtk-0.12.deps
%{_datadir}/vala/vapi/champlain-gtk-0.12.vapi
%endif

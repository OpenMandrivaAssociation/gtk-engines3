%define pkgname gtk-engines
%define pkgversion 3
%define lib_name %mklibname %{pkgname}%{pkgversion}

%define _requires_exceptions pkgconfig\(.*\)

%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-3.0); then pkg-config --variable=gtk_binary_version gtk+-3.0; else echo 0; fi)

Name:			%{pkgname}%{pkgversion}
Summary:		Default GTK+ 3.0 theme engines
Version:		2.90.2.1
Release:		%mkrel 1
License:		GPLv2+ and LGPLv2+
Group:			System/Libraries
BuildRequires:		gtk+3-devel
BuildRequires:		intltool
Source0:		http://ftp.gnome.org/pub/GNOME/sources/gtk-engines/%{pkgname}-%{version}.tar.bz2
Url:			ftp://ftp.gnome.org/pub/GNOME/sources/gtk-engines/

BuildRoot:		%{_tmppath}/%{name}-%{version}-buildroot
Requires:		%{lib_name} >= %{version}

%description
These are the graphical engines for the various GTK+ toolkit themes.
Included themes are:

  - Crux
  - HC
  - Industrial
  - Mist
  - Redmond
  - Glide
  - Thinice

#--------------------------------------------------------------------

%package -n %{lib_name}
Summary:	Library files for %{name}
Group:		System/Libraries
Requires:	gtk+3.0 >= 2.9.0
Provides:	%lib_name = %version

%description -n %{lib_name}
Library files for %{name}


%prep
%setup -q -n %{pkgname}-%{version}

%build

%configure2_5x --enable-animation
%make LIBS=-lm

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std


#remove empty files
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/%{gtkbinaryver}/engines/*.la
#gw needed at build time only
rm -rf %buildroot%_datadir/locale

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}


#--------------------------------------------------------------------

%files
%defattr(-,root,root)
%doc COPYING README
%{_datadir}/themes/*
%_datadir/gtk-engines/

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/gtk-3.0/%{gtkbinaryver}/engines/libclearlooks.so
%{_libdir}/gtk-3.0/%{gtkbinaryver}/engines/libcrux-engine.so
%{_libdir}/gtk-3.0/%{gtkbinaryver}/engines/libglide.so
%{_libdir}/gtk-3.0/%{gtkbinaryver}/engines/libhcengine.so
%{_libdir}/gtk-3.0/%{gtkbinaryver}/engines/libindustrial.so
%{_libdir}/gtk-3.0/%{gtkbinaryver}/engines/libmist.so
%{_libdir}/gtk-3.0/%{gtkbinaryver}/engines/libredmond95.so
%{_libdir}/gtk-3.0/%{gtkbinaryver}/engines/libthinice.so
%{_libdir}/pkgconfig/*

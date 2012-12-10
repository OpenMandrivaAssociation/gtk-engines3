%define pkgname gtk-engines
%define pkgversion 3
%define lib_name %mklibname %{pkgname}%{pkgversion}

%define _requires_exceptions pkgconfig\(.*\)

%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-3.0); then pkg-config --variable=gtk_binary_version gtk+-3.0; else echo 0; fi)

Name:			%{pkgname}%{pkgversion}
Summary:		Default GTK+ 3.0 theme engines
Version:		2.91.1
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

%configure2_5x
#--enable-animation
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


%changelog
* Tue Aug 02 2011 Götz Waschk <waschk@mandriva.org> 2.91.1-1mdv2012.0
+ Revision: 692724
- update to new version 2.91.1

* Thu Jul 01 2010 Götz Waschk <waschk@mandriva.org> 2.90.3.1-1mdv2011.0
+ Revision: 549725
- rename spec file

* Tue Apr 27 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.20.1-2mdv2010.1
+ Revision: 539614
- rebuild so that shared libraries are properly stripped again

* Sat Apr 17 2010 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2010.1
+ Revision: 535891
- update to new version 2.20.1

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2010.1
+ Revision: 528952
- update to new version 2.20.0

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 2.19.0-1mdv2010.1
+ Revision: 489955
- update to new version 2.19.0

* Fri Jan 01 2010 Götz Waschk <waschk@mandriva.org> 2.18.5-1mdv2010.1
+ Revision: 484676
- update to new version 2.18.5

* Thu Sep 24 2009 Götz Waschk <waschk@mandriva.org> 2.18.4-1mdv2010.0
+ Revision: 448383
- update to new version 2.18.4

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.18.3-1mdv2010.0
+ Revision: 446956
- build with system lua
- update to new version 2.18.3

* Mon May 18 2009 Götz Waschk <waschk@mandriva.org> 2.18.2-1mdv2010.0
+ Revision: 377376
- update to new version 2.18.2

* Sat May 16 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.18.1-2mdv2010.0
+ Revision: 376406
- split gtk-xfce-engine to a standalone package

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 2.18.1-1mdv2009.1
+ Revision: 366933
- update to new version 2.18.1

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2009.1
+ Revision: 356195
- update to new version 2.18.0

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 2.17.4-1mdv2009.1
+ Revision: 347591
- update to new version 2.17.4

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 2.17.3-2mdv2009.1
+ Revision: 345647
- Update Xfce engine

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 2.17.3-1mdv2009.1
+ Revision: 341296
- fix build
- update to new version 2.17.3

* Sun Dec 07 2008 Götz Waschk <waschk@mandriva.org> 2.17.2-1mdv2009.1
+ Revision: 311646
- update to new version 2.17.2

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 2.17.1-1mdv2009.1
+ Revision: 309079
- update to new version 2.17.1

* Tue Nov 04 2008 Götz Waschk <waschk@mandriva.org> 2.17.0-1mdv2009.1
+ Revision: 299719
- update to new version 2.17.0

* Tue Oct 21 2008 Götz Waschk <waschk@mandriva.org> 2.16.1-1mdv2009.1
+ Revision: 295911
- update to new version 2.16.1

* Fri Oct 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.16.0-2mdv2009.1
+ Revision: 294766
- update gtk-xfce-engine to the latest version 2.5.91 (Xfce4.6 beta1)

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2009.0
+ Revision: 286919
- new version

* Tue Sep 02 2008 Götz Waschk <waschk@mandriva.org> 2.15.4-1mdv2009.0
+ Revision: 278812
- new version

* Tue Aug 19 2008 Götz Waschk <waschk@mandriva.org> 2.15.3-1mdv2009.0
+ Revision: 273590
- new version

* Tue Aug 05 2008 Götz Waschk <waschk@mandriva.org> 2.15.2-1mdv2009.0
+ Revision: 263725
- new version
- update file list, the smooth engine is gone

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 2.15.1-1mdv2009.0
+ Revision: 231029
- fix installation
- new version

* Tue Jul 01 2008 Götz Waschk <waschk@mandriva.org> 2.14.3-1mdv2009.0
+ Revision: 230455
- new version
- update license

* Tue May 27 2008 Götz Waschk <waschk@mandriva.org> 2.14.2-1mdv2009.0
+ Revision: 211689
- more build fixes
- fix buildrequires
- new version
- fix flat theme build

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 2.14.1-1mdv2009.0
+ Revision: 192478
- new version

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdv2008.1
+ Revision: 183799
- new version

* Tue Feb 26 2008 Götz Waschk <waschk@mandriva.org> 2.13.6-1mdv2008.1
+ Revision: 175275
- new version

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 2.13.5-1mdv2008.1
+ Revision: 165699
- new version

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 2.13.4-1mdv2008.1
+ Revision: 159482
- new version

* Tue Jan 08 2008 Götz Waschk <waschk@mandriva.org> 2.13.3-3mdv2008.1
+ Revision: 146804
- fix cleanice build on x86_64
- replace wonderland by bluecurve gtk engine

* Tue Jan 08 2008 Götz Waschk <waschk@mandriva.org> 2.13.3-1mdv2008.1
+ Revision: 146370
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Götz Waschk <waschk@mandriva.org> 2.13.2-1mdv2008.1
+ Revision: 131634
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - do not package big ChangeLog

* Tue Dec 04 2007 Götz Waschk <waschk@mandriva.org> 2.13.1-1mdv2008.1
+ Revision: 115242
- new version

* Sun Nov 18 2007 Jérôme Soyer <saispo@mandriva.org> 2.13.0-2mdv2008.1
+ Revision: 110064
- Add new gtk-xfce-engine

* Wed Nov 14 2007 Götz Waschk <waschk@mandriva.org> 2.13.0-1mdv2008.1
+ Revision: 108582
- new version

* Tue Oct 16 2007 Götz Waschk <waschk@mandriva.org> 2.12.2-1mdv2008.1
+ Revision: 98886
- new version

* Fri Sep 21 2007 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-1mdv2008.0
+ Revision: 91895
- Release 2.12.1

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.12.0-1mdv2008.0
+ Revision: 89346
- new version

* Fri Aug 24 2007 Götz Waschk <waschk@mandriva.org> 2.11.7-1mdv2008.0
+ Revision: 70982
- new version

* Fri Aug 17 2007 Götz Waschk <waschk@mandriva.org> 2.11.6-1mdv2008.0
+ Revision: 64704
- new version

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 2.11.5-1mdv2008.0
+ Revision: 63078
- new version

* Tue Aug 07 2007 Frederic Crozat <fcrozat@mandriva.com> 2.11.4-2mdv2008.0
+ Revision: 59863
- Enable animation support in clearlooks engine (Mdv bug #30574)

* Tue Jul 31 2007 Götz Waschk <waschk@mandriva.org> 2.11.4-1mdv2008.0
+ Revision: 56958
- new version

* Tue Jul 10 2007 Götz Waschk <waschk@mandriva.org> 2.11.3-1mdv2008.0
+ Revision: 50853
- new version

* Tue Jun 19 2007 Götz Waschk <waschk@mandriva.org> 2.11.2-1mdv2008.0
+ Revision: 41285
- new version

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 2.11.1-3mdv2008.0
+ Revision: 36283
- rebuild with correct optflags

  + Götz Waschk <waschk@mandriva.org>
    - new version

* Tue May 29 2007 Götz Waschk <waschk@mandriva.org> 2.10.2-1mdv2008.0
+ Revision: 32363
- new version

* Wed Apr 25 2007 Jérôme Soyer <saispo@mandriva.org> 2.10.1-2mdv2008.0
+ Revision: 18148
- Update gtk-engine for the new XFCE

* Wed Apr 18 2007 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdv2008.0
+ Revision: 14415
- new version


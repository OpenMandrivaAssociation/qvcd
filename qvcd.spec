%define name	qvcd
%define version	0.21
%define release %mkrel 9


Name: 	 	%{name}
Summary: 	Tool for building and writing VCD's
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL:		http://www.steffen-sobiech.de/qvcd_1_en.htm
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	qt3-devel gettext png-devel
Requires:	vcdimager cdrdao

%description
qvcd is a graphical frontend for GNU vcdimager and cdrdao. Together with
those tools, qvcd can be used to create a VideoCD out of an MPEG file. 

%prep
%setup -q

%build
%configure2_5x --with-qt-libraries=/usr/lib/qt3/%{_lib}
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -fr $RPM_BUILD_ROOT/usr/doc

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=QVCD
Comment=Video CD Creator
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Video;AudioVideo;AudioVideoEditing
Encoding=UTF-8
EOF


#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README qvcd/docs/en/*.html
%{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.21-9mdv2010.0
+ Revision: 433122
- use %%configure2_5x
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.21-8mdv2009.0
+ Revision: 260007
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.21-7mdv2009.0
+ Revision: 247810
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.21-5mdv2008.1
+ Revision: 140743
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import qvcd


* Sat Sep 16 2006 Emmanuel Andry <eandry@mandriva.org> 0.21-5mdv2007.0
- %%mkrel
- xdg menu

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 0.21-4mdk
- lib64 fix

* Fri Jul 16 2004 Michael Scherer <misc@mandrake.org> 0.21-3mdk 
- rebuild for new gcc
- fix libtool

* Fri Apr 2 2004 Austin Acton <austin@mandrake.org> 0.21-2mdk
- libtoolize
- delib buildrequires
- stale rebuild

* Sat Mar 22 2003 Austin Acton <aacton@yorku.ca> 0.21-1mdk
- initial package

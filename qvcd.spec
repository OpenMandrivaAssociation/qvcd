%define name	qvcd
%define version	0.21
%define release %mkrel 5


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
%configure --with-qt-libraries=/usr/lib/qt3/%{_lib}
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


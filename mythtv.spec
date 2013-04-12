%define gitversion v0.26.0-138-g69cd7
%define fixesdate 20130328
%define rel 1

%if %{fixesdate}
%define release %{fixesdate}.%{rel}
%else
%define release %{rel}
%endif

%define lib_name_orig	libmyth
%define lib_major	%{version}
%define lib_name	%mklibname myth %{lib_major}
%define lib_name_devel	%mklibname myth -d

%define maenable 1

#set default build options
# disabled as overrides xv
%define build_directfb		0
%define build_dts		0
%define build_faac		0
%define build_faad		0
%define build_lame		0
%define build_x264		0
%define build_xvid		0

# Can be enabled later
%define build_crystalhd		0

%define build_plf 0

%if %{build_plf}
%define extrarelsuffix plf
%define distsuffix		plf
%define build_dts		1
%define build_faac		1
%define build_faad		1
%define build_lame		1
# build broken against current x264 as of 2010-01, re-enable when fixed
%define build_x264		1
%define build_xvid		1
%endif

#enable/disable building for certain hardware
%{?_without_directfb:		%global build_directfb 0}
%{?_without_dts:		%global build_dts 0}
%{?_without_faac:		%global build_faac 0}
%{?_without_faad:		%global build_faad 0}
%{?_without_lame:		%global build_lame 0}
%{?_without_x264:		%global build_x264 0}
%{?_without_xvid:		%global build_xvid 0}

%{?_with_directfb:		%global build_directfb 1}
%{?_with_dts:			%global build_dts 1}
%{?_with_faac:			%global build_faac 1}
%{?_with_faad:			%global build_faad 1}
%{?_with_lame:			%global build_lame 1}
%{?_with_x264:			%global build_x264 1}
%{?_with_xvid:			%global build_xvid 1}


Summary:	A personal video recorder (PVR) application
Name:		mythtv
Version:	0.26.0
Release:	%{release}%{?extrarelsuffix}
URL:		http://www.mythtv.org/
License:	GPLv2 and GPLv3
Group:		Video
Source0:	%{name}-%{version}.tar.bz2
Source1:	mythbackend.sysconfig.in
Source2:	mythbackend.service.in
Source3:	mythbackend.logrotate.in
Source4:	99MythFrontend
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
Source10:	%{name}.rpmlintrc

%if %{fixesdate}
Patch0:		fixes-%{gitversion}.patch
%endif
Patch1:		mythtv-0.26.0-gcc-c++11.patch
Patch100:	0100-lame-Allow-building-without-lame-libraries.patch
Patch101:	0101-pulse-Do-not-suspend-PA-when-using-alsa-default.patch
Patch102:	0102-Fix-dns-sd-detection.patch
Patch103:	0103-Fix-installation-of-zeromq.patch
Patch104:	0104-Support-libcec-2.x.patch

BuildRequires:	yasm
BuildRequires:	imagemagick
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dvdnav)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(jack)
BuildRequires:	lirc-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xvmc)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	python-devel
BuildRequires:	python-mysql
BuildRequires:	python-lxml
BuildRequires:	python-urlgrabber
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	perl-devel
BuildRequires:	perl(DBD::mysql)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Date::Manip)
BuildRequires:	pkgconfig(libva)
%if %{build_crystalhd}
BuildRequires:	crystalhd-devel
%endif
BuildRequires:	pkgconfig(libcec)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(avahi-compat-libdns_sd)
BuildRequires:	pkgconfig(vpx)
BuildRequires:	gdb
%if %{build_lame}
BuildRequires:	lame-devel
%endif
%if %{build_dts}
BuildRequires:	dtsdec-devel
%endif
%if %{build_x264}
BuildRequires:	x264-devel
%endif
%if %{build_xvid}
BuildRequires:	xvid-devel
%endif
%if %{build_faac}
BuildRequires:	libfaac-devel
%endif
%if %{build_faad}
BuildRequires:	libfaad2-devel
%endif
%if %{build_directfb}
BuildRequires:	pkgconfig(directfb)
%endif
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libiec61883)
BuildRequires:	pkgconfig(glu)
%if %{maenable}
BuildRequires:	multiarch-utils
%endif

%description
MythTV implements the following PVR features, and more, with a
unified graphical interface:

 - Basic 'live-tv' functionality. Pause/Fast Forward/Rewind "live" TV.
 - Video compression using RTjpeg or MPEG-4
 - Program listing retrieval using XMLTV
 - Themable, semi-transparent on-screen display
 - Electronic program guide
 - Scheduled recording of TV programs
 - Resolution of conflicts between scheduled recordings
 - Basic video editing

%if %{build_plf}
This package is in restricted because it contains software that supports
codecs that may be covered by software patents.
%endif
%if !%{build_lame}
Note that this build does not support MP3 encoding when recording
into the NuppelVideo format.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at 
revision %{gitversion}
%endif

%package -n %{lib_name}
Summary:	Library providing mythtv support
Group:		System/Libraries
Provides:	%{lib_name_orig} = %{version}-%{release} 

%description -n %{lib_name}
Common library code for MythTV and add-on modules (development)
MythTV provides a unified graphical interface for recording and viewing
television programs.

%if %{build_plf}
This package is in restricted because it contains software that supports
codecs that may be covered by software patents.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at 
revision %{gitversion}
%endif

%package -n %{lib_name_devel}
Summary:	Development files for libmyth
Group:		Development/Other
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	myth-devel = %{version}-%{release}
Obsoletes:	%{_lib}myth0.20-devel

%description -n %{lib_name_devel}
This package contains the header files and libraries for developing
add-ons for mythtv.

%if %{build_plf}
This package is in restricted because it contains software that supports
codecs that may be covered by software patents.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at 
revision %{gitversion}
%endif

%package themes-base
Summary:	Base themes for mythtv's frontend
Group:		Video
BuildArch:	noarch
Obsoletes:	mythtv-themes < 0.20-5
Conflicts:	mythtv-themes-myththemes < 0.22
Conflicts:	mythtv-plugin-controls < 0.22

%description themes-base
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains only the base themes used by mythtv-frontend and
mythtv-setup.

%package common
Summary:	Common components needed by multiple other MythTV components
Group:		Video
Conflicts:	mythtv-backend < 0.25
Conflicts:	mythtv-frontend < 0.25

%description common
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains components needed by multiple other MythTV components.

%package frontend
Summary:	Client component of mythtv (a PVR)
Group:		Video
Requires:	mythtv-themes-base = %{version}-%{release}
Requires:	mythtv-common = %{version}-%{release}
Requires:	qt4-database-plugin-mysql
Requires:	mplayer
%if %{build_plf}
Requires:	transcode
Requires:	%{mklibname dvdcss 2}
%endif
Obsoletes:	mythtv-plugin-controls < 0.25
Obsoletes:	mythtv-plugin-video < 0.25
Conflicts:	mythtv-backend < 0.25


%description frontend
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains only the client software, which provides a
front-end for playback and configuration.  It requires access to a
mythtv-backend installation, either on the same system or one
reachable via the network.

%if %{build_plf}
This package is in restricted because it contains software that supports
codecs that may be covered by software patents.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at 
revision %{gitversion}
%endif

%package backend
Summary:	Server component of mythtv (a PVR)
Group:		Video
Requires:	%{lib_name} = %{version}-%{release}
Requires:	mythtv-common = %{version}-%{release}
Requires:	qt4-database-plugin-mysql
Requires(pre,post,preun,postun):	rpm-helper
Conflicts:	mythtv-frontend < 0.25

%description backend
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains only the server software, which provides video
and audio capture and encoding services.  In order to be useful, it
requires a mythtv-frontend installation, either on the same system or
one reachable via the network.

%if %{build_plf}
This package is in restricted because it contains software that supports
codecs that may be covered by software patents.
%endif
%if !%{build_lame}
Note that this build does not support MP3 encoding when recording
into the NuppelVideo format.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at 
revision %{gitversion}
%endif

%package setup
Summary:	Setup the mythtv backend
Group:		Video
Requires:	mythtv-backend = %{version}-%{release}
Requires:	mythtv-themes-base = %{version}-%{release}
Obsoletes:	mythtvsetup < 0.19
Provides:	mythtvsetup
Requires:	qt4-database-plugin-mysql

%description setup
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains the setup software for configuring the mythtv
backend.

%if %{build_plf}
This package is in restricted because it contains software that supports
codecs that may be covered by software patents.
%endif
%if !%{build_lame}
Note that this build does not support MP3 encoding when recording
into the NuppelVideo format.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at 
revision %{gitversion}
%endif

%package doc
Summary:	MythTV documentation
Group:		Video
Obsoletes:	mythtv < 0.20-5

%description doc
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains the documentation and contributed additional
scripts for MythTV.

%package -n perl-MythTV
Summary:	Perl bindings for MythTV
Group:		Development/Perl

%description -n perl-MythTV
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains the perl bindings for MythTV.

%package -n python-mythtv
Summary:	Python bindings for MythTV
Group:		Development/Python
Requires:	python-mysql
Requires:	python-lxml

%description -n python-mythtv
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains the python bindings for MythTV.

%package -n php-mythtv
Summary:	PHP bindings for MythTV
Group:		Development/PHP
BuildArch:	noarch
Requires:	php-mysql

%description -n php-mythtv
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains the PHP bindings for MythTV.

%prep
%setup -q
%apply_patches

# (cg) Fixes might bring in some .gitignore files in patches... trash 'em.
find -name .gitignore -delete

# (cg) The installer is dumb and installs our patch backup files...
# This can be removed after 0.25
rm -f programs/scripts/database/mythconverg_restore.pl.*

# (cg) As of 0.21, only contrib scripts are affected.
find contrib -type f | xargs grep -l /usr/local | xargs perl -pi -e's|/usr/local|%{_prefix}|g'

echo "QMAKE_PROJECT_DEPTH = 0" >> mythtv.pro
echo "QMAKE_PROJECT_DEPTH = 0" >> settings.pro

cp -a %{SOURCE1} %{SOURCE2} %{SOURCE3} .
for file in mythbackend.service \
            mythbackend.sysconfig \
            mythbackend.logrotate; do
  sed -e's|@logdir@|%{_logdir}|g' \
      -e's|@rundir@|%{_var}/run|g' \
      -e's|@sysconfdir@|%{_sysconfdir}|g' \
      -e's|@sysconfigdir@|%{_sysconfdir}/sysconfig|g' \
      -e's|@initdir@|%{_initrddir}|g' \
      -e's|@bindir@|%{_bindir}|g' \
      -e's|@sbindir@|%{_sbindir}|g' \
      -e's|@subsysdir@|%{_var}/lock/subsys|g' \
      -e's|@varlibdir@|%{_localstatedir}/lib|g' \
      -e's|@varcachedir@|%{_var}/cache|g' \
      -e's|@logrotatedir@|%{_sysconfdir}/logrotate.d|g' \
  < $file.in > $file
done

# default recordings dir
perl -pi -e's|/mnt/store|%{_localstatedir}/lib/mythtv/recordings|' programs/mythtv-setup/backendsettings.cpp

# do not set hardcoded archflags
perl -pi -e's|^echo "ARCHFLAGS=|# echo "ARCHFLAGS=|' configure

# Fix the version reporting (which assumes svn checkout)
echo "SOURCE_VERSION=%{version}-%{release}" >VERSION

%build
./configure \
  --prefix=%{_prefix} \
  --libdir-name=%{_lib} \
  --enable-runtime-cpudetect \
  --enable-dvb \
  --enable-opengl-video \
  --without-bindings=perl \
  --extra-cxxflags="%{optflags}" \
  --extra-ldflags="%{ldflags}" \
  --enable-vdpau \
  --enable-vaapi \
%if %{build_crystalhd}
  --enable-crystalhd \
%endif
  --enable-libfftw3 \
  --enable-libdns-sd \
  --enable-libvpx \
%if %{build_plf}
  --enable-nonfree \
%endif
%if %{build_x264}
  --enable-libx264 \
%endif
%if %{build_xvid}
  --enable-libxvid \
%endif
%if %{build_faac}
  --enable-libfaac \
%endif
%if %{build_lame}
  --enable-libmp3lame \
%endif
  --enable-firewire

%make

# This is easier to do ourselves
pushd bindings/perl
%__perl Makefile.PL INSTALLDIRS=vendor
%make
popd

%install
INSTALL_ROOT=%{buildroot}; export INSTALL_ROOT
%makeinstall

pushd bindings/perl
%makeinstall_std
popd

%if %{maenable}
%multiarch_includes %{buildroot}%{_includedir}/mythtv/mythconfig.h
%endif

mkdir -p %{buildroot}%{_localstatedir}/lib/mythtv
mkdir -p %{buildroot}%{_localstatedir}/lib/mythtv/recordings
mkdir -p %{buildroot}%{_var}/cache/mythtv
mkdir -p %{buildroot}%{_logdir}/mythtv
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig

install -p mythbackend.service %{buildroot}%{_unitdir}/mythbackend.service
install -p mythbackend.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/mythbackend
install -p mythbackend.logrotate  %{buildroot}%{_sysconfdir}/logrotate.d

# wmsession.d for mythfrontend
mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d
install -p %{SOURCE4} %{buildroot}%{_sysconfdir}/X11/wmsession.d

# icon
install -d -m755 %{buildroot}/%{_miconsdir}
install -m755 %{SOURCE5} %{buildroot}/%{_miconsdir}/%{name}.png

install -d -m755 %{buildroot}/%{_iconsdir}
install -m755 %{SOURCE6} %{buildroot}/%{_iconsdir}/%{name}.png

install -d -m755 %{buildroot}/%{_liconsdir}
install -m755 %{SOURCE7} %{buildroot}/%{_liconsdir}/%{name}.png


# Mandriva Menu entrys
install -d -m755 %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/mandriva-mythtv-frontend.desktop
[Desktop Entry]
Name=MythTV
Comment=Record, playback and watch TV
Exec=mythfrontend
Icon=%{name}
Terminal=false
Type=Application
Categories=Qt;AudioVideo;Video;TV;Recorder;X-MandrivaLinux-Multimedia-Video;
EOF
cat <<EOF > %{buildroot}%{_datadir}/applications/mandriva-mythtv-setup.desktop
[Desktop Entry]
Name=MythTV Setup
Comment=Setup MythTV backend
Exec=mythtv-setup
Icon=%{name}
Terminal=false
Type=Application
Categories=Qt;AudioVideo;Video;TV;Recorder;X-MandrivaLinux-Multimedia-Video;
EOF

cat > README.install.urpmi <<EOF
You can import the initial database by running:
mysql -u root -p < %{_datadir}/mythtv/initialdb/mc.sql
(you can omit -p if you do not have the password set)
EOF

mkdir -p %{buildroot}%{_libdir}/mythtv/plugins

install -d -m755 %{buildroot}%{_datadir}/mythtv/initialdb
install -m644 database/* %{buildroot}%{_datadir}/mythtv/initialdb

# install a few useful contrib scripts
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -ar contrib %{buildroot}%{_datadir}/%{name}

# Remove python egg-info as it's pointless
rm -f %{buildroot}%{py_puresitedir}/MythTV-*.egg-info

# (cg) We cover the package license so no need to include it separately
rm -f %{buildroot}%{_datadir}/%{name}/fonts/tiresias_gpl3.txt

# (cg) This is needed for the %doc stuff on the subpackages for some reason...
mkdir -p %{buildroot}%{_docdir}/%{name}-backend
mkdir -p %{buildroot}%{_docdir}/%{name}-doc

# (cg) For some reason the FFmpeg stuff is included in two build roots :s
if [ -d %{buildroot}%{buildroot}%{_includedir}/%{name} ]; then
  mv %{buildroot}%{buildroot}%{_includedir}/%{name}/* %{buildroot}%{_includedir}/%{name}
  rmdir -p %{buildroot}%{buildroot}%{_includedir}/%{name} || /bin/true
fi
if [ -f %{buildroot}%{buildroot}%{_bindir}/mythffmpeg ]; then
  mv %{buildroot}%{buildroot}%{_bindir}/mythff* %{buildroot}%{_bindir}
  rmdir -p %{buildroot}%{buildroot}%{_bindir} || /bin/true
fi

# (cg) Clean up some stuff we don't want to include
rm -f %{buildroot}%{_libdir}/libmythqjson.prl \
rm -f %{buildroot}%{_includedir}/zmq*.h* \
      %{buildroot}%{_libdir}/pkgconfig/libmythzmq.pc

find %{buildroot} -name *.la -delete
find %{buildroot} -name *.a -delete

%pre backend
# Add the "mythtv" user
%_pre_useradd mythtv %{_localstatedir}/lib/mythtv /sbin/nologin
%{_bindir}/gpasswd -a mythtv audio &>/dev/null
%{_bindir}/gpasswd -a mythtv video &>/dev/null

%postun backend
%_postun_userdel mythtv

%post backend
%_post_service mythbackend

%preun backend
%_preun_service mythbackend

%files doc
%doc README UPGRADING AUTHORS COPYING FAQ
%doc keys.txt
%doc contrib
%{_datadir}/%{name}/fonts/*.txt
%{_datadir}/%{name}/contrib
%{_datadir}/%{name}/html

%files common
%{_bindir}/mythccextractor
%{_bindir}/mythcommflag
%{_bindir}/mythpreviewgen
%{_bindir}/mythtranscode
%{_bindir}/mythwikiscripts
%{_bindir}/mythmetadatalookup
%{_bindir}/mythutil
%{_bindir}/mythlogserver
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/mythconverg*.pl
%dir %{_datadir}/%{name}/locales
%{_datadir}/%{name}/locales/*
%dir %{_datadir}/%{name}/metadata
%{_datadir}/%{name}/metadata/*
%dir %{_datadir}/%{name}/hardwareprofile
%{_datadir}/%{name}/hardwareprofile/*

%files backend
%doc README.install.urpmi
%{_bindir}/mythbackend
%{_bindir}/mythfilldatabase
%{_bindir}/mythjobqueue
%{_bindir}/mythmediaserver
%{_bindir}/mythreplex
%attr(-,mythtv,mythtv) %dir %{_localstatedir}/lib/mythtv
%attr(-,mythtv,mythtv) %dir %{_localstatedir}/lib/mythtv/recordings
%attr(-,mythtv,mythtv) %dir %{_var}/cache/mythtv
%{_unitdir}/mythbackend.service
%config(noreplace) %{_sysconfdir}/sysconfig/mythbackend
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%attr(-,mythtv,mythtv) %dir %{_logdir}/mythtv
%{_datadir}/%{name}/backend-config
%dir %{_datadir}/%{name}/initialdb
%{_datadir}/%{name}/initialdb/mc.sql
%{_datadir}/mythtv/internetcontent/

%files frontend
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/99MythFrontend
%{_datadir}/mythtv/*.xml
%exclude %{_datadir}/mythtv/setup.xml
%{_bindir}/mythwelcome
%{_bindir}/mythfrontend
%{_bindir}/mythff*
%{_bindir}/mythlcdserver
%{_bindir}/mythshutdown
%{_bindir}/mythavtest
%dir %{_libdir}/mythtv
%{_libdir}/mythtv/filters
%{_libdir}/mythtv/plugins
%dir %{_datadir}/mythtv
%dir %{_datadir}/mythtv/fonts
%{_datadir}/mythtv/fonts/*.ttf
%{_datadir}/mythtv/fonts/*.otf
%{_datadir}/mythtv/i18n
%{_datadir}/applications/mandriva-mythtv-frontend.desktop

%files setup
%{_bindir}/mythtv-setup
%{_datadir}/applications/mandriva-mythtv-setup.desktop
%dir %{_datadir}/mythtv
%{_datadir}/mythtv/setup.xml

%files themes-base
%dir %{_datadir}/mythtv
%{_datadir}/mythtv/themes
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%files -n %{lib_name}
%{_libdir}/*.so.*

%files -n %{lib_name_devel}
%if %maenable
%{multiarch_includedir}/mythtv/mythconfig.h
%endif
%{_includedir}/mythtv
# FIXME: Manually multiarch mythconfig.mak
%{_libdir}/*.so
#%{_datadir}/mythtv/build/settings.pro

%files -n perl-MythTV
%{perl_vendorlib}/MythTV.pm
%{perl_vendorlib}/MythTV
%{perl_vendorlib}/IO/Socket/INET/MythTV.pm

%files -n python-mythtv
%{_bindir}/mythpython
%{py_puresitedir}/MythTV

%files -n php-mythtv
%{_datadir}/%{name}/bindings/php

%changelog
* Fri Apr 13 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.24.2-1
+ Revision: 790456
- update to 0.24.2

  + Colin Guthrie <cguthrie@mandriva.org>
    - Fix issue with mythff* files.
    - Update to latest fixes

  + Anssi Hannula <anssi@mandriva.org>
    - plf: append "plf" to Release on cooker to make plf build have higher EVR
      again with the rpm5-style mkrel now in use

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 0.24-27162.3
+ Revision: 636322
- tighten BR

* Mon Nov 15 2010 Colin Guthrie <cguthrie@mandriva.org> 0.24-27162.2mdv2011.0
+ Revision: 597804
- Fix PLF build

* Fri Nov 12 2010 Colin Guthrie <cguthrie@mandriva.org> 0.24-27162.1mdv2011.0
+ Revision: 596470
- Add some missing python build deps
- New version 0.24

* Thu Jun 17 2010 Colin Guthrie <cguthrie@mandriva.org> 0.23-25073.1mdv2010.1
+ Revision: 548207
- Update to latest fixes
- Add World Cup 2010 Vuvuzela audio filter

* Wed Jun 02 2010 Colin Guthrie <cguthrie@mandriva.org> 0.23-24821.2mdv2010.1
+ Revision: 546932
- Move mythcommflag to the backend package (mdv #59600)

* Tue May 25 2010 Colin Guthrie <cguthrie@mandriva.org> 0.23-24821.1mdv2010.1
+ Revision: 545863
- Updated to latest (post-release) -fixes

* Sun May 02 2010 Colin Guthrie <cguthrie@mandriva.org> 0.23-24334.1mdv2010.1
+ Revision: 541652
- Fix python includes
- Resurrect the nolame patch (my reading of upstream changes was bogus)
- New version: 0.23
- Update patch for enabling PA+alsa (only when PA is running + default device is used)
- Drop unneeded patches
- Fix the version reported by myth* --version
- Update to latest -fixes

* Sun Jan 17 2010 Anssi Hannula <anssi@mandriva.org> 0.22-22890.4mdv2010.1
+ Revision: 492811
- plf: disable x264 support as per Colin Guthrie's comments until fixed

* Mon Dec 21 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22890.3mdv2010.1
+ Revision: 480519
- Fix PLF configure with x264

* Tue Nov 24 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22890.2mdv2010.1
+ Revision: 469800
- Obsolete mythtv-plugin-controls (mdv#55663)
- Update to latest fixes
- Re-enable x264 support (it seems to build fine)
- enable-runtime-cpudetect

* Thu Nov 12 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22807.1mdv2010.1
+ Revision: 465509
- Update to post release -fixes.

* Wed Oct 21 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22550.0.1mdv2010.0
+ Revision: 458507
- Latest upstream fixes-branch

* Tue Oct 13 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22427.0.1mdv2010.0
+ Revision: 457193
- Latest fixes
- Fix no-lame patch

* Mon Oct 12 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22355.0.2mdv2010.0
+ Revision: 456965
- Enable vdpau and fftw3
- Fix PLF build

* Sun Oct 11 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22355.0.1mdv2010.0
+ Revision: 456638
- Latest updates and do not accidentally include patch in export tree.
- Update to latest 0.22 code (currently trunk - release due shortly)
- Update lame patch for 0.22
- Enable PulseAudio by default (upstream suspend it). Automatic Suspending still possible.
- Rejig SPEC for QT4 build, drop old stuff

* Sat May 23 2009 Colin Guthrie <cguthrie@mandriva.org> 0.21-20320.2mdv2010.0
+ Revision: 379024
- Fix db schema creation (mdv#50698)

* Tue Apr 14 2009 Colin Guthrie <cguthrie@mandriva.org> 0.21-20320.1mdv2009.1
+ Revision: 367222
- Update to latest fixes revision
- Fix the version as reported by --version to include the correct svn revision

* Sun Feb 15 2009 Colin Guthrie <cguthrie@mandriva.org> 0.21-19961.1mdv2009.1
+ Revision: 340521
- Do not require arts
- Fix format-security fallow
- New fixes snapshot (r19961)

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sat Sep 27 2008 Colin Guthrie <cguthrie@mandriva.org> 0.21-18452.1mdv2009.0
+ Revision: 288918
- Update to -fixes revision r18452

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.21-16564.2mdv2009.0
+ Revision: 218425
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
- adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

  + Anssi Hannula <anssi@mandriva.org>
    - define %%_localstatedir locally for backportability

* Sun Mar 16 2008 Anssi Hannula <anssi@mandriva.org> 0.21-16564.2mdv2008.1
+ Revision: 188149
- build with correct optflags

* Sat Mar 15 2008 Colin Guthrie <cguthrie@mandriva.org> 0.21-16564.1mdv2008.1
+ Revision: 188078
- Update to latest fixes

* Sat Mar 01 2008 Colin Guthrie <cguthrie@mandriva.org> 0.21-0.16317.1mdv2008.1
+ Revision: 177469
- Fix python-devel BR
- Install the python bindings manually
- BuildRequires python-setuptools for bindings
- Add patch for building sans LAME
- Update fixes branch
- Prefix release by 0 to indicate pre-release.
- Update to 0.21-fixes branch. 0.21 is not yet officially released but we will follow this branch until the next release anyway.

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Colin Guthrie <cguthrie@mandriva.org> 0.20.2-14486.1mdv2008.0
+ Revision: 86034
- Update fixes snapshot

  + Anssi Hannula <anssi@mandriva.org>
    - obsolete old devel name

* Thu Aug 30 2007 Colin Guthrie <cguthrie@mandriva.org> 0.20.2-14357.1mdv2008.0
+ Revision: 76260
- Update fixes snapshot
- New upstream fixes release - 0.20.2

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Tue Aug 14 2007 Colin Guthrie <cguthrie@mandriva.org> 0.20-4.14154.1mdv2008.0
+ Revision: 63324
- Fix group
- Update to 'fixes' r14154

* Thu Apr 19 2007 Anssi Hannula <anssi@mandriva.org> 0.20-4.13272.1mdv2008.0
+ Revision: 15132
- new snapshot
- Import mythtv




* Sat Mar 24 2007 Anssi Hannula <anssi@mandriva.org> 0.20-3.13107.1mdv2007.0
+ Revision: 148719
- add conditional build option for dts
- add some contrib scripts to bindir
- enable the usual options unconditionally
- add build options for faad, faac, xvid, and enable them for plf
- add perl-MythTV for perl bindings
- drop archflags guessed by configure
- drop configure lib64 hack, fixed upstream
- add build options for lame and plf
- fix descriptions
- rename mythtv to mythtv-doc, and do not explicitely require it
- fix sysconfig location
- add xdg="true" to menu entries
- drop 0.19 upgrade notice
- move initial database file to mythtv-backend package
- own some unowned directories
- new snapshot from the stable branch
- patch2: allow build without lame
- uncompress patch1
- provide myth-devel in the -devel package
- rename mythtv-themes to mythtv-themes-base
- Import mythtv



* Sat Jan 20 2007 Stefan van der Eijk <stefan@zarb.org> 0.20-3
- add release-0-20-fixes patch (12579)
- drop glXWaitVideoSyncSGI patch
- move setup.xml to the setup package
- tighter dependencies (also on %%{release}) within the package
- fix logrotate to kill -HUP the pid. This should release storage
  of deleted episodes, etc.

* Thu Jan 11 2007 Stefan van der Eijk <stefan@zarb.org> 0.20-2
- add glXWaitVideoSyncSGI patch
- add pinit info to mythbacken initscript

* Tue Sep 12 2006 Anssi Hannula <anssi@zarb.org> 0.20-1plf2007.0
- 0.20
- xdg menu

* Sun Jul 16 2006 Anssi Hannula <anssi@zarb.org> 0.19.1-0.10553.1plf2007.0
- new snapshot of the stable branch
- minor fix to README.urpmi
- backportability buildrequires fix

* Sun Jun 04 2006 Stefan van der Eijk <stefan@zarb.org> 0.19-4plf
- fix BuildRequires (new mesa naming)
- add wmsession file for mythfrontend

* Sun Apr 23 2006 Anssi Hannula <anssi@zarb.org> 0.19-3plf
- fix PLF reason

* Tue Feb 21 2006 Anssi Hannula <anssi@zarb.org> 0.19-2plf
- fix menus
- add mythtv user to audio group

* Tue Feb 21 2006 Anssi Hannula <anssi@zarb.org> 0.19-1plf
- enable dvd by default
- clean spec
- drop patch0, don't force O_STREAMING if not supported by kernel/headers
- drop patch4, patch5, fixed upstream
- fix icons
- drop patch1, unneeded
- fix requires qt3-mysql
- convert to README.urpmi
- use dts_pic (patch0)
- mythtv user created by backend only
- mythbackend runs as user mythtv, add notice to README.urpmi
- fix build with arts
- drop broken nvidia/via renaming thing, use xvmcw by default
- apply default recordings dir of /var/lib/mythtv/recordings
- add mythtv user to video group

* Sat Oct 15 2005 Anssi Hannula <anssi@zarb.org> 0.18.2-0.7467.2plf
- fix requires qt3-MySQL

* Thu Oct 13 2005 Anssi Hannula <anssi@zarb.org> 0.18.2-0.7467.1plf
- upgrade to release-0-18-fixes svn branch revision 7467

* Mon Oct 10 2005 Anssi Hannula <anssi@zarb.org> 0.18.1-20050618.6plf
- fix x86_64 build (patch5)
- use %%_post_service %%_preun_service %%_pre_useradd %%_postun_userdel

* Mon Aug 22 2005 Stefan van der Eijk <stefan@zarb.org> 0.18.1-20050618.5plf
- fix menu's
- add menu entry to setup package
- move icons of menus to themes package
- add distsuffix
- fix filelist: include files
- add %%{_logdir} define for  %%mdkversion <= 1020
- add versioned Provides to devel package

* Sun Jul 24 2005 Stefan van der Eijk <stefan@zarb.org> 0.18.1-20050618.4plf
- use mythtv-setup name consitantly
- add Requires for theme package on frontend package
- modified Source2 --> default runlevels
- use %%mkrel
- replace non-standard defines with standard defines

* Thu Jul 14 2005 Stefan van der Eijk <stefan@zarb.org> 0.18.1-20050618.3plf
- BuildRequires

* Mon Jun 20 2005 Austin Acton <austin@zarb.org> 0.18.1-20050618.2plf
- get rid of some unnecessary version dependencies
- get rid of some unnecessary requires

* Fri Jun 18 2005 Austin Acton <austin@zarb.org> 0.18.1-20050618.1plf
- bring back to PLF
- bump to CVS for gcc4 and dvb fixes
- fix library major version
- fix some rpmlint
- parallel build (hope that's okay)
- TODO: avoid having -march defined three times in gcc commands
- add build option for native dvd (but disable by default)
- don't try to build firewire by default on < 2006.0
- multiarch macros on >= 10.2
- fix icons for menu

* Fri May 21 2005 Colin Guthrie <mythtv@colin.guthr.ie> 0.18.1-2.mdk10.2.thac
- Patch has_library funcion in myth on x86_64 builds to detect libs correctly

* Fri May 20 2005 Colin Guthrie <mythtv@colin.guthr.ie> 0.18.1-1.mdk10.2.thac
- Fixes for x86_64 builds
- Bump version to 0.18.1

* Sun Apr 24 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.18-2.mdk10.2.thac
- Sync with changes from Stefan van der Eijk <stefan@eijk.nu>
- re-did the --with & --without mechanism
- re-did the BuildRequires
- used %%configure instead of editting the settings.pro file

* Sun Apr 24 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.18-1.mdk10.2.thac
- 0.18
- Fix spec to build on pclo


* Wed Feb 16 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.17-3.mdk10.1.thac
- Fix Provides lybmyth = 0.17

* Tue Feb 15 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.17-2.mdk10.1.thac
- Chenge conlicts xmltv-grabbers to obsoletes

* Sun Feb 13 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.17-1.mdk10.1.thac
- Update to 0.17
- Sync with Axel Thimm spec file
- Remove dependencies on xmltv-grabbers and mysql (Edward Rudd
  <eddie@omegaware.com>)..
- Enable opengl_vsync and xrandr for some distributions.

* Mon Oct 25 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.16-5.mdk10.1.thac
- 5.mdk10.1.thac
- Where "5" is the release of the package, "mdk" is the distro, "10.1" is the release of the distro, and "thac" is the Torbjorn Turpeinen extension.

* Fri Oct 22 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.16-4thac
- Synced with Sefan van der Eijks spec file
- Updated requiremnts for kdelibs,xmlltv and lame
- Rebuilt for Mandrake-10.1

* Mon Oct 05 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.16-3thac
- Changed requirement to qt3 >= 3.3.3

* Fri Sep 10 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.16-2thac 
- Included .png files for html help

* Fri Sep 10 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.16-1thac
- Updated to latest version
- Included dvb support in the build. 
- Changed back to thac release to be able to support nnidia and via builds.

* Wed Jun 23 2004 Stefan van der Eijk <stefan@eijk.nu> 0.15.1-2plf
- turn off building against NVIDIA by default, untill the NVIDIA
  packages are in plf
- patch0 gcc 3.4 fixes

* Wed Jun 02 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.15.1-1plf
- Updated to latest version

* Fri May 28 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.15-1plf
- Updated to latest version
- Use workaround for qmake project depth bug
  (by Robert Hardy <rhardy@webcon.ca>).
- Split off mythtvsetup and the base themes into their own sub packages.
- Make mysql.txt part of both frontend and backend.
- Added support for arts and dvb. arts has been enabled by default.
- Disable directfb in default build.

* Sat Feb 28 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.14-4plf
- Added the missing configfiles dir to %%doc

* Sat Feb 21 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.14-3plf
- Clean spec file for Mandrake menu.

* Sat Feb 21 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.14-2plf
- Readded first time myth-backend mysql setup instruction.

* Sun Feb 01 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.14-1plf
- Updated to latest version

* Tue Jan 13 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.13-5plf
- cleaned up spec file

* Fri Dec 26 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.13-4plf
- Changed to plf release

* Sun Dec 14 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.13-3thac
- Merged changes made by stefan@eijk.nu

* Sun Dec 14 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.13-2thac
- Added the tvformat patch
- Cleaned up spec file

* Sat Dec 13 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.13-1thac
- Updated to latest version

* Wed Oct 29 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.12-3thac
- Added missing dependency for libqt3-mysql in mythtv-backend

* Thu Oct 23 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.12-2thac
- Rebuilt for Mandrake 9.2

* Sun Oct 19 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.12-1thac
- Updated to latest version

* Mon Oct 06 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.11-1thac
- Changed naming
- Added imdb patch

* Mon Aug 25 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.11-2mdk
- Fix location of localstatedir from Frederic Crozat <fcrozat@mandrakesoft.com>

* Sun Aug 17 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.11-1mdk
- Updated to latest version

* Wed Jul 16 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.10-2mdk
- Added patch for latest XMLTV from Alex.Thimms red hat package

* Mon Jul 07 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.10-1mdk
- Updated to latest version
- with latest XmlTV dependency
- Added all the latest from Alex.Thimms RedHat spec.

* Sun Jun 15 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.9.1-1mdk
- Updated to latest version
- with latest XmlTV dependency

* Thu Apr 17 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.8-6mdk
- Removed the mysql dependency from frontend to backend.
  Frontend only needs qt3-mysql.

* Thu Apr 10 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.8-5mdk
- Rebuilt with lataest XmlTV dependency

* Fri Mar 28 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.8-4mdk
- Cleaned up spec file.

* Fri Mar 28 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.8-3mdk
- Added missing dependency for libqt3-mysql needed for 9.1

* Thu Mar 27 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.8-2mdk
- Recompiled for Mandrake 9.1

* Mon Mar 24 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.8-1mdk
- Recompiled for Mandrake 9.0

* Sun Mar 23 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Fixed desktop entries.

* Sat Mar 22 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Add g flag to sed.
- Don't use mythtv user yet.

* Fri Mar 21 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Add mythtv user.
- Add desktop entries.

* Wed Mar 19 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Added start/stop scripts for mythbackend.

* Tue Mar 18 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Removed unneeded 0.7 patches.

* Mon Mar 17 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Update to 0.8.
- Synced with Matt Zimmerman's debian package (package splitting).
- Split off lib, devel, frontend, backend packages.

* Thu Feb 13 2003 Paul Jara <pjara@rogers.com> 0.7-0at7
- Added a patch that prevents a segmentation fault in mythfilldatabase.

* Thu Jan 16 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 0.7-0at6
- Added dependency to qt-MySQL (Roy Stogner <roystgnr@ticam.utexas.edu>).

* Thu Dec  5 2002 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 0.7-0at4
- fixed installation paths.

* Wed Nov 13 2002 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Initial build.


%define name    mythtv
%define version 0.23
%define fixes 24334
%define rel 1

%define release	%mkrel %fixes.%rel

%define lib_name_orig	libmyth
%define lib_major	0.23
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

# --with plf
%bcond_with plf
%if %with plf
%define distsuffix		plf
%define build_dts		1
%define build_faac		1
%define build_faad		1
%define build_lame		1
# build broken against current x264 as of 2010-01, re-enable when fixed
%define build_x264		0
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
Name:		%{name}
Version:	%{version}
Release: 	%{release}
URL:		http://www.mythtv.org/
License:	GPL
Group:		Video
Source0:	%{name}-%{version}-%{fixes}.tar.bz2
Source1:	mythbackend.sysconfig.in
Source2:	mythbackend.init.in
Source3:	mythbackend.logrotate.in
Source4:	99MythFrontend
Source5:	%name-16.png
Source6:	%name-32.png
Source7:	%name-48.png
Patch0: mythtv-0.23-enable-pulseaudio-with-alsa-default.patch

BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	imagemagick
BuildRequires:	qt4-devel
BuildRequires:	libalsa-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libjack-devel
BuildRequires:	lirc-devel
BuildRequires:	X11-devel
BuildRequires:  python-devel
BuildRequires:  fftw3-devel
BuildRequires:  vdpau-devel
%if %build_lame
BuildRequires:	lame-devel
%endif
%if %build_dts
BuildRequires:	dtsdec-devel
%endif
%if %build_x264
BuildRequires:	x264-devel
%endif
%if %build_xvid
BuildRequires:	xvid-devel
%endif
%if %build_faac
BuildRequires:	libfaac-devel
%endif
%if %build_faad
BuildRequires:	libfaad2-devel
%endif
%if %{build_directfb}
BuildRequires:	libdirectfb-devel
%endif
BuildRequires:	libavc1394-devel
BuildRequires:	libiec61883-devel
BuildRequires:	mesaglu-devel
%if %maenable
BuildRequires:  multiarch-utils
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

%if %with plf
This package is in PLF because it contains software that supports
codecs that may be covered by software patents.
%endif
%if !%build_lame
Note that this build does not support MP3 encoding when recording
into the NuppelVideo format.
%endif
%if %fixes
This package is based on the MythTV "fixes" branch at revision %fixes
%endif

%package -n %{lib_name}
Summary:	Library providing mythtv support
Group:		System/Libraries
Provides:	%{lib_name_orig} = %{version}-%{release} 

%description -n %{lib_name}
Common library code for MythTV and add-on modules (development)
MythTV provides a unified graphical interface for recording and viewing
television programs.

%if %with plf
This package is in PLF because it contains software that supports
codecs that may be covered by software patents.
%endif
%if %fixes
This package is based on the MythTV "fixes" branch at revision %fixes
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

%if %with plf
This package is in PLF because it contains software that supports
codecs that may be covered by software patents.
%endif
%if %fixes
This package is based on the MythTV "fixes" branch at revision %fixes
%endif

%package themes-base
Obsoletes:	mythtv-themes < 0.20-5
Summary:	Base themes for mythtv's frontend
Group:		Video
Conflicts:	mythtv-themes-myththemes < 0.22
Conflicts:	mythtv-plugin-controls < 0.22

%description themes-base
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains only the base themes used by mythtv-frontend and
mythtv-setup.

%package frontend
Summary:	Client component of mythtv (a PVR)
Group:		Video
Requires:	mythtv-themes-base = %{version}-%{release}
Requires:	qt4-database-plugin-mysql
Obsoletes:	mythtv-plugin-controls

%description frontend
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains only the client software, which provides a
front-end for playback and configuration.  It requires access to a
mythtv-backend installation, either on the same system or one
reachable via the network.

%if %with plf
This package is in PLF because it contains software that supports
codecs that may be covered by software patents.
%endif
%if %fixes
This package is based on the MythTV "fixes" branch at revision %fixes
%endif

%package backend
Summary:	Server component of mythtv (a PVR)
Group:		Video
Requires:	%{lib_name} = %{version}-%{release}
Requires:	qt4-database-plugin-mysql

%description backend
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains only the server software, which provides video
and audio capture and encoding services.  In order to be useful, it
requires a mythtv-frontend installation, either on the same system or
one reachable via the network.

%if %with plf
This package is in PLF because it contains software that supports
codecs that may be covered by software patents.
%endif
%if !%build_lame
Note that this build does not support MP3 encoding when recording
into the NuppelVideo format.
%endif
%if %fixes
This package is based on the MythTV "fixes" branch at revision %fixes
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

%if %with plf
This package is in PLF because it contains software that supports
codecs that may be covered by software patents.
%endif
%if !%build_lame
Note that this build does not support MP3 encoding when recording
into the NuppelVideo format.
%endif
%if %fixes
This package is based on the MythTV "fixes" branch at revision %fixes
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

%description -n python-mythtv
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains the python bindings for MythTV.

%prep
%setup -q
%patch0 -p0 -b .pulse

# (cg) As of 0.21, only contrib scripts are affected.
find contrib -type f | xargs grep -l /usr/local | xargs perl -pi -e's|/usr/local|%{_prefix}|g'

echo "QMAKE_PROJECT_DEPTH = 0" >> mythtv.pro
echo "QMAKE_PROJECT_DEPTH = 0" >> settings.pro

cp -a %{SOURCE1} %{SOURCE2} %{SOURCE3} .
for file in mythbackend.init \
            mythbackend.sysconfig \
            mythbackend.logrotate; do
  sed -e's|@logdir@|%{_logdir}|g' \
      -e's|@rundir@|%{_var}/run|g' \
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
echo "SOURCE_VERSION=%version-%release" >VERSION

%build

./configure \
  --prefix=%{_prefix} \
  --libdir-name=%{_lib} \
  --enable-runtime-cpudetect \
  --enable-dvb \
  --enable-opengl-vsync --enable-opengl-video \
  --enable-xvmc --enable-xvmc-pro \
  --without-bindings=perl \
  --extra-cxxflags="%{optflags}" \
  --enable-vdpau \
  --enable-libfftw3 \
%if %with plf
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
%if %{build_faad}
  --enable-libfaad \
%endif
%if !%{build_directfb}
  --disable-directfb \
%endif
%if %{build_lame}
  --enable-libmp3lame \
%endif
  --enable-firewire

%make

# This is easier to do ourselves
pushd bindings/perl
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
popd

%install
rm -rf %{buildroot}

INSTALL_ROOT=%{buildroot}; export INSTALL_ROOT
%makeinstall

pushd bindings/perl
%makeinstall_std
popd


%if %maenable
%multiarch_includes %{buildroot}%_includedir/mythtv/mythconfig.h
%endif

mkdir -p %{buildroot}%{_localstatedir}/lib/mythtv
mkdir -p %{buildroot}%{_localstatedir}/lib/mythtv/recordings
mkdir -p %{buildroot}%{_var}/cache/mythtv
mkdir -p %{buildroot}%{_logdir}/mythtv
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig

install -p mythbackend.init %{buildroot}%{_initrddir}/mythbackend
install -p mythbackend.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/mythbackend
install -p mythbackend.logrotate  %{buildroot}%{_sysconfdir}/logrotate.d

# wmsession.d for mythfrontend
mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d
install -p %{SOURCE4} %{buildroot}%{_sysconfdir}/X11/wmsession.d

# icon
install -d -m755 %{buildroot}/%{_miconsdir}
install -m755 %{SOURCE5} %{buildroot}/%{_miconsdir}/%name.png

install -d -m755 %{buildroot}/%{_iconsdir}
install -m755 %{SOURCE6} %{buildroot}/%{_iconsdir}/%name.png

install -d -m755 %{buildroot}/%{_liconsdir}
install -m755 %{SOURCE7} %{buildroot}/%{_liconsdir}/%name.png


# Mandriva Menu entrys
install -d -m755 %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/mandriva-mythtv-frontend.desktop
[Desktop Entry]
Name=MythTV
Comment=Record, playback and watch TV
Exec=%{_bindir}/mythfrontend
Icon=%{name}
Terminal=false
Type=Application
Categories=Qt;AudioVideo;Video;TV;Recorder;X-MandrivaLinux-Multimedia-Video;
EOF
cat <<EOF > %{buildroot}%{_datadir}/applications/mandriva-mythtv-setup.desktop
[Desktop Entry]
Name=MythTV Setup
Comment=Setup MythTV backend
Exec=%{_bindir}/mythtv-setup
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

#mkdir -p %{buildroot}%{_datadir}/mythtv/build/
#install -p settings.pro %{buildroot}%{_datadir}/mythtv/build/

# install a few useful contrib scripts
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -ar contrib %{buildroot}%{_datadir}/%{name}

# Remove python egg-info as it's pointless
rm -f %{buildroot}%{py_puresitedir}/MythTV-*.egg-info

# (cg) This is needed for the %doc stuff on the subpackages for some reason...
mkdir -p %{buildroot}%{_docdir}/%{name}-backend
mkdir -p %{buildroot}%{_docdir}/%{name}-doc

%clean
rm -rf %{buildroot}

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

%post frontend
%{make_session}

%postun frontend
%{make_session}

%files doc
%defattr(-,root,root)
%doc README UPGRADING AUTHORS COPYING FAQ
%doc keys.txt
%doc docs/*.html docs/*.png docs/*.txt docs/i18n contrib
%{_datadir}/%{name}/contrib

%files backend
%defattr(-,root,root)
%doc README.install.urpmi
#%config(noreplace) %{_datadir}/mythtv/mysql.txt
%{_bindir}/mythbackend
%{_bindir}/mythfilldatabase
%{_bindir}/mythjobqueue
%{_datadir}/%{name}/mythconverg_backup.pl
%{_datadir}/%{name}/mythconverg_restore.pl
%attr(-,mythtv,mythtv) %dir %{_localstatedir}/lib/mythtv
%attr(-,mythtv,mythtv) %dir %{_localstatedir}/lib/mythtv/recordings
%attr(-,mythtv,mythtv) %dir %{_var}/cache/mythtv
%{_initrddir}/mythbackend
%config(noreplace) %{_sysconfdir}/sysconfig/mythbackend
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%attr(-,mythtv,mythtv) %dir %{_logdir}/mythtv
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/initialdb
%{_datadir}/%{name}/initialdb/mc.sql

%files frontend
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/99MythFrontend
%{_datadir}/mythtv/*.xml
%{_bindir}/mythwelcome
%{_bindir}/mythfrontend
%{_bindir}/mythcommflag
%{_bindir}/mythlcdserver
%{_bindir}/mythtranscode
%{_bindir}/mythtvosd
%{_bindir}/mythreplex
%{_bindir}/mythshutdown
%{_bindir}/mythavtest
%dir %{_libdir}/mythtv
%{_libdir}/mythtv/filters
%{_libdir}/mythtv/plugins
%dir %{_datadir}/mythtv
%{_datadir}/mythtv/*.ttf
%{_datadir}/mythtv/i18n
%{_datadir}/applications/mandriva-mythtv-frontend.desktop

%files setup
%defattr(-,root,root)
%{_bindir}/mythtv-setup
%{_datadir}/applications/mandriva-mythtv-setup.desktop
%dir %{_datadir}/mythtv
%{_datadir}/mythtv/setup.xml

%files themes-base
%defattr(-,root,root)
%dir %{_datadir}/mythtv
%{_datadir}/mythtv/themes
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_liconsdir}/%name.png

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*-%lib_major.so.*

%files -n %{lib_name_devel}
%defattr(-,root,root)
%if %maenable
%multiarch %{multiarch_includedir}/mythtv/mythconfig.h
%endif
%{_includedir}/mythtv
# FIXME: Manually multiarch mythconfig.mak
%{_libdir}/*-%lib_major.so
%{_libdir}/*.a
#%{_datadir}/mythtv/build/settings.pro

%files -n perl-MythTV
%defattr(-,root,root)
%{perl_vendorlib}/MythTV.pm
%{perl_vendorlib}/MythTV
%{perl_vendorlib}/IO/Socket/INET/MythTV.pm

%files -n python-mythtv
%defattr(-,root,root)
%dir %{py_puresitedir}/MythTV
%{py_puresitedir}/MythTV/*.py
%dir %{py_puresitedir}/MythTV/tmdb
%{py_puresitedir}/MythTV/tmdb/*.py
%dir %{py_puresitedir}/MythTV/ttvdb
%{py_puresitedir}/MythTV/ttvdb/*.py
#%{py_puresitedir}/MythTV/*.pyc

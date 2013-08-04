%define gitversion v0.26.0-138-g69cd7
%define fixesdate 20130328
%define rel 2

%if %{fixesdate}
%define release %{fixesdate}.%{rel}
%else
%define release %{rel}
%endif

%define api	0.26
%define major	0
%define avcmaj	54
%define avfmaj	2
%define avumaj	51
%define ppmaj	52
%define zmqmaj	1
%define libmyth %mklibname myth %{api} %{major}
%define libmavc %mklibname mythavcodec %{avcmaj}
%define libmavd %mklibname mythavdevice %{avcmaj}
%define libmavfi %mklibname mythavfilter %{avfmaj}
%define libmavfo %mklibname mythavformat %{avcmaj}
%define libmavu %mklibname mythavutil %{avumaj}
%define libmythbase %mklibname mythbase %{api} %{major}
%define libmythfreemheg %mklibname mythfreemheg %{api} %{major}
%define libmythhdhomerun %mklibname mythhdhomerun %{api} %{major}
%define libmythlivemedia %mklibname mythlivemedia %{api} %{major}
%define libmythmetadata %mklibname mythmetadata %{api} %{major}
%define libmnzmqt %mklibname mythnzmqt %{major}
%define libmpp %mklibname mythpostproc %{ppmaj}
%define libmythprotoserver %mklibname mythprotoserver %{api} %{major}
%define libmqjson %mklibname mythqjson %{major}
%define libmythservicecontracts %mklibname mythservicecontracts %{api} %{major}
%define libmswr %mklibname mythswresample %{major}
%define libmsws %mklibname mythswscale %{avfmaj}
%define libmythui %mklibname mythui %{api} %{major}
%define libmythupnp %mklibname mythupnp %{api} %{major}
%define libmzmq %mklibname mythzmq %{zmqmaj}
%define libname %mklibname %{name} %{api} %{major}
%define devname	%mklibname %{name} -d

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
License:	GPLv2 and GPLv3
Group:		Video
Url:		http://www.mythtv.org/
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

BuildRequires:	gdb
BuildRequires:	imagemagick
BuildRequires:	perl(Date::Manip)
BuildRequires:	perl(DBD::mysql)
BuildRequires:	perl(DBI)
BuildRequires:	python-lxml
BuildRequires:	python-mysql
BuildRequires:	python-urlgrabber
BuildRequires:	yasm
BuildRequires:	perl-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(avahi-compat-libdns_sd)
BuildRequires:	pkgconfig(dvdnav)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libcec)
BuildRequires:	pkgconfig(libiec61883)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(QtWebkit)
BuildRequires:	pkgconfig(vpx)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xvmc)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(vdpau)
%if %{build_crystalhd}
BuildRequires:	crystalhd-devel
%endif
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

%package -n %{libname}
Summary:	Library providing mythtv support
Group:		System/Libraries
Obsoletes:	%{_lib}mythtv0.26 < 0.26.0-20130328.2

%description -n %{libname}
Common library code for MythTV and add-on modules (development).

%if %{build_plf}
This package is in restricted because it contains software that supports
codecs that may be covered by software patents.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at 
revision %{gitversion}
%endif

%define mythtvlibs libmyth libmavc libmavd libmavfi libmavfo libmavu libmythbase libmythfreemheg libmythhdhomerun libmythlivemedia libmythmetadata libmnzmqt libmpp libmythprotoserver libmqjson libmythservicecontracts libmswr libmsws libmythui libmythupnp libmzmq 
%{expand:%(for lib in %{mythtvlibs}; do cat <<EOF
%%package -n %%{$lib}
Summary:	Shared library providing mythtv support
Group:		System/Libraries
Conflicts:	%{_lib}mythtv0.26 < 0.26.0-20130328.2
EOF
done)}

%{expand:%(for lib in %{mythtvlibs}; do cat <<EOF
%%description -n %%{$lib}
This package contains a shared library for %{name}.
EOF
done)}

%package -n %{devname}
Summary:	Development files for libmyth
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
%{expand:%(for lib in %{mythtvlibs}; do cat <<EOF
Requires:	%%{$lib} = %{version}-%{release}
EOF
done)}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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

%description themes-base
This package contains only the base themes used by mythtv-frontend and
mythtv-setup.

%package common
Summary:	Common components needed by multiple other MythTV components
Group:		Video

%description common
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

%description frontend
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
Requires:	%{libname} = %{version}-%{release}
Requires:	mythtv-common = %{version}-%{release}
Requires:	qt4-database-plugin-mysql
Requires(pre,post,preun,postun):	rpm-helper

%description backend
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
Requires:	qt4-database-plugin-mysql
Provides:	mythtvsetup

%description setup
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

%description doc
This package contains the documentation and contributed additional
scripts for MythTV.

%package -n perl-MythTV
Summary:	Perl bindings for MythTV
Group:		Development/Perl

%description -n perl-MythTV
This package contains the perl bindings for MythTV.

%package -n python-mythtv
Summary:	Python bindings for MythTV
Group:		Development/Python
Requires:	python-mysql
Requires:	python-lxml

%description -n python-mythtv
This package contains the python bindings for MythTV.

%package -n php-mythtv
Summary:	PHP bindings for MythTV
Group:		Development/PHP
BuildArch:	noarch
Requires:	php-mysql

%description -n php-mythtv
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

%files -n %{libmyth}
%{_libdir}/libmyth-%{api}.so.%{major}*

%files -n %{libmavc}
%{_libdir}/libmythavcodec.so.%{avcmaj}*

%files -n %{libmavd}
%{_libdir}/libmythavdevice.so.%{avcmaj}*

%files -n %{libmavfi}
%{_libdir}/libmythavfilter.so.%{avfmaj}*

%files -n %{libmavfo}
%{_libdir}/libmythavformat.so.%{avcmaj}*

%files -n %{libmavu}
%{_libdir}/libmythavutil.so.%{avumaj}*

%files -n %{libmythbase}
%{_libdir}/libmythbase-%{api}.so.%{major}*

%files -n %{libmythfreemheg}
%{_libdir}/libmythfreemheg-%{api}.so.%{major}*

%files -n %{libmythhdhomerun}
%{_libdir}/libmythhdhomerun-%{api}.so.%{major}*

%files -n %{libmythlivemedia}
%{_libdir}/libmythlivemedia-%{api}.so.%{major}*

%files -n %{libmythmetadata}
%{_libdir}/libmythmetadata-%{api}.so.%{major}*

%files -n %{libmnzmqt}
%{_libdir}/libmythnzmqt.so.%{major}*

%files -n %{libmpp}
%{_libdir}/libmythpostproc.so.%{ppmaj}*

%files -n %{libmythprotoserver}
%{_libdir}/libmythprotoserver-%{api}.so.%{major}*

%files -n %{libmqjson}
%{_libdir}/libmythqjson.so.%{major}*

%files -n %{libmythservicecontracts}
%{_libdir}/libmythservicecontracts-%{api}.so.%{major}*

%files -n %{libmswr}
%{_libdir}/libmythswresample.so.%{major}*

%files -n %{libmsws}
%{_libdir}/libmythswscale.so.%{avfmaj}*

%files -n %{libname}
%{_libdir}/libmythtv-%{api}.so.%{major}*

%files -n %{libmythui}
%{_libdir}/libmythui-%{api}.so.%{major}*

%files -n %{libmythupnp}
%{_libdir}/libmythupnp-%{api}.so.%{major}*

%files -n %{libmzmq}
%{_libdir}/libmythzmq.so.%{zmqmaj}*

%files -n %{devname}
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


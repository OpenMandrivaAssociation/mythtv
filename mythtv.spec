%if "%{distepoch}" < "2015.0"
%define	__python2	%{_bindir}/python2
%define	py2_puresitedir	%{py_puresitedir}
%endif

%define api	0.27
%define major	0
%define avcmaj	54
%define avfmaj	3
%define avumaj	52
%define ppmaj	52
%define swscmaj 2
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
%define libmythmetadata %mklibname mythmetadata %{api} %{major}
%define libmnzmqt %mklibname mythnzmqt %{major}
%define libmpp %mklibname mythpostproc %{ppmaj}
%define libmythprotoserver %mklibname mythprotoserver %{api} %{major}
%define libmqjson %mklibname mythqjson %{major}
%define libmythservicecontracts %mklibname mythservicecontracts %{api} %{major}
%define libmswr %mklibname mythswresample %{major}
%define libmsws %mklibname mythswscale %{swscmaj}
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
%define build_fdk_aac		0
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
%define build_fdk_aac		1
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
%{?_without_fdk_aac:               %global build_fdk_aac 0}
%{?_without_lame:		%global build_lame 0}
%{?_without_x264:		%global build_x264 0}
%{?_without_xvid:		%global build_xvid 0}

%{?_with_directfb:		%global build_directfb 1}
%{?_with_dts:			%global build_dts 1}
%{?_with_faac:			%global build_faac 1}
%{?_with_faad:			%global build_faad 1}
%{?_with_fdk_aac:               %global build_fdk_aac 1}
%{?_with_lame:			%global build_lame 1}
%{?_with_x264:			%global build_x264 1}
%{?_with_xvid:			%global build_xvid 1}

%if "%{disttag}" == "mdk"
%define build_directfb		1
%define build_dts		1
%define build_faac		1
%define build_faad		1
%define build_fdk_aac		1
%define build_lame		1
%define build_x264		1
%define build_xvid		1
# Can be enabled later
%define build_crystalhd		1
%endif

Summary:	A personal video recorder (PVR) application
Name:		mythtv
Version:	0.27.4
%define	gitrev	v0.27.4-4-gb305e
%define	fixesdate 20141022
Release:	%{?fixesdate:%{fixesdate}.}2%{?extrarelsuffix}
License:	GPLv2 and GPLv3
Group:		Video
Url:		http://www.mythtv.org/
Source0:	v%{version}.tar.gz
Source1:	mythbackend.sysconfig.in
Source2:	mythbackend.service.in
Source3:	mythbackend.logrotate.in
Source4:	99MythFrontend
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
Source10:	%{name}.rpmlintrc

%if %{fixesdate}
Patch0:		fixes-%{gitrev}.patch
%endif
Patch100:	0100-lame-Allow-building-without-lame-libraries.patch
Patch101:	0101-lame-Allow-building-plugins-without-lame-libraries.patch
Patch102:	0102-pulse-Do-not-suspend-PA-when-using-alsa-default.patch
Patch103:	0103-Fix-dns-sd-detection.patch
Patch104:	0104-Support-libcec-2.x.patch
Patch105:	0105-Use-system-build-flags.patch
Patch106:	0106-Fix-zeromq-libdir-path-on-some-systems.patch
Patch107:	0107-add-missing-qt5-include.patch

Patch200:	mythtv-0.27.4-ffmpeg-dlopen-restricted-codecs.patch
Patch201:	0001-this-patch-is-most-likely-broken-but-at-least-it-mak.patch
Patch203:	0001-fix-to-use-mythtv-s-own-header.patch

BuildRequires:	gdb
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	imagemagick
BuildRequires:	flite-devel
BuildRequires:	perl(Date::Manip)
BuildRequires:	perl(DBD::mysql)
BuildRequires:	perl(DBI)
BuildRequires:	pythonegg(lxml)
BuildRequires:	python-mysql
BuildRequires:	python-urlgrabber
BuildRequires:	pythonegg(oauth)
BuildRequires:	yasm
BuildRequires:	perl-devel
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(avahi-compat-libdns_sd)
BuildRequires:	pkgconfig(dvdnav)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libbluray)
BuildRequires:	pkgconfig(libcec)
BuildRequires:	pkgconfig(libiec61883)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(QtWebKit)
BuildRequires:	pkgconfig(vpx)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xvmc)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:  gsm-devel
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(schroedinger-1.0)
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(speex)
BuildRequires:  libnut-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(celt)
BuildRequires:  openjpeg-devel
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(libilbc)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:	dc1394-devel
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
%if %{build_fdk_aac}
BuildRequires:	pkgconfig(fdk-aac)
%endif
%if %{build_directfb}
BuildRequires:	pkgconfig(directfb)
%endif
%if %{maenable}
BuildRequires:	multiarch-utils
%endif

BuildRequires:  libvisual-devel
BuildRequires:  fftw-devel
BuildRequires:  pkgconfig(sdl)
BuildRequires:  libdvdread-devel
BuildRequires:  pkgconfig(libexif)
BuildRequires:  id3tag-devel
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(flac)
BuildRequires:  cdaudio-devel
BuildRequires:  cdda-devel
BuildRequires:  tiff-devel
BuildRequires:  mysql-devel
BuildRequires:  taglib-devel
BuildRequires:  perl-XML-XPath
BuildRequires:  perl-Image-Size
BuildRequires:  perl-Date-Manip
BuildRequires:  perl-DateTime-Format-ISO8601
BuildRequires:  perl-SOAP-Lite
BuildRequires:  perl-XML-Simple
BuildRequires:	perl-JSON
BuildRequires:  perl(Class::Factory::Util)

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
revision %{gitrev}
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
revision %{gitrev}
%endif

%define mythtvlibs libmyth libmavc libmavd libmavfi libmavfo libmavu libmythbase libmythfreemheg libmythhdhomerun libmythmetadata libmnzmqt libmpp libmythprotoserver libmqjson libmythservicecontracts libmswr libmsws libmythui libmythupnp libmzmq 
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
revision %{gitrev}
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
revision %{gitrev}
%endif

%package backend
Summary:	Server component of mythtv (a PVR)
Group:		Video
Requires:	%{libname} = %{version}-%{release}
Requires:	mythtv-common = %{version}-%{release}
Requires:	qt4-database-plugin-mysql
Requires(pre,postun):	rpm-helper

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
revision %{gitrev}
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
revision %{gitrev}
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
Requires:	python2-lxml

%description -n python-mythtv
This package contains the python bindings for MythTV.

%package -n php-mythtv
Summary:	PHP bindings for MythTV
Group:		Development/PHP
BuildArch:	noarch
Requires:	php-mysql

%description -n php-mythtv
This package contains the PHP bindings for MythTV.

%package plugin-browser
Summary:        Full web browser for MythTV
URL:            http://www.mythtv.org/
Group:          Video
Obsoletes:      mythbrowser < 0.20a-7
Requires:       mythtv-frontend >= %{version}

%description plugin-browser
MythBrowser is a full web browser for MythTV.

%package plugin-gallery
Summary:        Gallery/slideshow module for MythTV
Group:          Video
Requires:       mythtv-frontend >= %{version}
Obsoletes:      mythgallery < 0.20a-7

%description plugin-gallery
A gallery/slideshow module for MythTV.

%package plugin-game
Summary:        Game frontend for MythTV
Group:          Video
Requires:       mythtv-frontend >= %{version}
Obsoletes:      mythgame < 0.20a-7

%description plugin-game
A game frontend for MythTV.

%package plugin-music
Summary:        The music player add-on module for MythTV
Group:          Video
#Requires:       cdparanoia
Requires:       mythtv-frontend >= %{version}
Obsoletes:      mythmusic < 0.20a-7

%description plugin-music
The music player add-on module for MythTV.

%if %{build_plf}
This package is in the tainted section because it contains software that supports
codecs that may be covered by software patents.
%endif

%package plugin-netvision
Summary:        NetVision for MythTV
Group:          Video
Requires:       mythtv-frontend >= %{version}
Requires:	pythonegg(oauth)

%description plugin-netvision
NetVision for MythTV. View popular media website content.

%package plugin-news
Summary:        RSS News feed plugin for MythTV
Group:          Video
Requires:       mythtv-frontend >= %{version}
Obsoletes:      mythnews < 0.20a-7

%description plugin-news
An RSS News feed plugin for MythTV.

%package plugin-weather
Summary:        MythTV module that displays a weather forecast
Group:          Video
Requires:       mythtv-frontend >= %{version}
Obsoletes:      mythweather < 0.20a-7

%description plugin-weather
A MythTV module that displays a weather forcast.

%package plugin-zoneminder
Summary:        Security camera plugin for MythTV
Group:          Video
Requires:       mythtv-frontend >= %{version}

%description plugin-zoneminder
A security camera plugin for MythTV.

%package plugin-archive
Summary:        Creates DVDs from your recorded shows
Group:          Video
Requires:       dvd+rw-tools
Requires:       dvdauthor
Requires:       ffmpeg
Requires:       mjpegtools
Requires:       python-imaging
Requires:       mythtv-frontend >= %{version}
%if %{build_plf}
Requires:       transcode
%endif
Requires:       cdrkit-genisoimage
Obsoletes:      mytharchive < 0.20a-7

%description plugin-archive
MythArchive is a plugin for MythTV that lets you create DVDs
from your recorded shows, MythVideo files and any video files
available on your system. It can also archive recordings in a
proprietary format that archives not only the file but also all the
associated metadata like title, description and cut list information
which will mean you can create backups of myth recordings which can
later be restored or it will also allow you to move recordings
between myth systems without losing any of the metadata. It is a
complete rewrite of the old MythBurn bash scripts, now using python,
and the mythfrontend UI plugin.

%prep
%setup -q
%apply_patches

# (cg) Fixes might bring in some .gitignore files in patches... trash 'em.
find -name .gitignore -delete

# (cg) The installer is dumb and installs our patch backup files...
# This can be removed after 0.25
rm -f programs/scripts/database/mythconverg_restore.pl.*

pushd mythtv

# (cg) As of 0.21, only contrib scripts are affected.
find contrib -type f | xargs grep -l /usr/local | xargs perl -pi -e's|/usr/local|%{_prefix}|g'

echo "QMAKE_PROJECT_DEPTH = 0" >> mythtv.pro
echo "QMAKE_PROJECT_DEPTH = 0" >> settings.pro

sed -i 's/-fno-exceptions//' settings.pro

cp -a %{SOURCE1} %{SOURCE2} %{SOURCE3} .
for file in mythbackend.service \
            mythbackend.sysconfig \
            mythbackend.logrotate; do
  sed -e's|@logdir@|%{_logdir}|g' \
      -e's|@rundir@|%{_varrun}|g' \
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
pushd mythtv
%global debugcflags -gdwarf-4 -Wstrict-aliasing=2
./configure	--cc=clang \
		--cxx=clang++ \
		--logfile=config.log \
		--prefix=%{_prefix} \
		--libdir-name=%{_lib} \
		--python=%{__python2} \
		--enable-runtime-cpudetect \
		--enable-dvb \
		--enable-opengl-video \
		--with-bindings=perl,php,python \
		--extra-cxxflags="%{optflags} -fPIC -Ofast" \
		--extra-ldflags="%{ldflags}" \
		--enable-sdl \
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
		--enable-dvb \
		--enable-opengl-video \
		--with-bindings=perl,php,python \
		--perl-config-opts=INSTALLDIRS=vendor \
		--enable-libass \
		--enable-v4l2 \
		--enable-firewire \
                --disable-libfdk-aac \
%if %{build_fdk_aac}
                --enable-libfdk-aac-dlopen \
%endif
		--disable-libopencore-amrnb \
%if %{build_plf}
		--enable-libopencore-amrnb-dlopen \
%endif
		--disable-libopencore-amrwb \
%if %{build_plf}
		--enable-libopencore-amrwb-dlopen \
%endif
		--disable-libfaac \
%if %{build_faac}
		--enable-libfaac-dlopen \
%endif
		--disable-libx264 \
%if %{build_x264}
		--enable-libx264-dlopen \
%endif
		--disable-libxvid \
%if %{build_xvid}
		--enable-libxvid-dlopen \
%endif
		--disable-libmp3lame \
%if %{build_lame}
		--enable-libmp3lame-dlopen \
%endif
		--enable-postproc \
		--enable-pthreads \
		--enable-libtheora \
		--enable-libdc1394 \
		--enable-libschroedinger \
		--enable-librtmp \
		--enable-libspeex \
		--enable-libfreetype \
		--enable-libnut \
		--enable-libgsm \
		--enable-libcelt \
		--enable-libopenjpeg \
		--enable-libmodplug \
		--enable-libv4l2 \
		--enable-openal \
		--enable-libsoxr \
		--enable-libtwolame \
		--enable-libopus \
		--enable-libilbc \
		--enable-libiec61883 \
		--enable-libbluray \
		--enable-fontconfig \
		--enable-libflite \
		--disable-decoder=aac \
		--disable-encoder=aac
%make
popd

# Install temporarily to compile plugins
mkdir -p temp
temp=$PWD/temp
make -C mythtv install INSTALL_ROOT=$temp DESTDIR=$temp
export LD_LIBRARY_PATH=$temp%{_libdir}:$LD_LIBRARY_PATH

pushd mythplugins

# Fix things up so they can find our "temp" install location for mythtv libs
echo "QMAKE_PROJECT_DEPTH = 0" >> settings.pro
find . -name \*.pro \
  -exec sed -i -e "s,INCLUDEPATH += .\+/include/mythtv,INCLUDEPATH += $temp%{_includedir}/mythtv," {} \; \
  -exec sed -i -e "s,DEPLIBS = \$\${LIBDIR},DEPLIBS = $temp%{_libdir}," {} \; \
  -exec sed -i -e "s,\$\${PREFIX}/include/mythtv,$temp%{_includedir}/mythtv," {} \;
echo "INCLUDEPATH -= \$\${PREFIX}/include" >> settings.pro
echo "INCLUDEPATH -= \$\${SYSROOT}/\$\${PREFIX}/include" >> settings.pro
echo "INCLUDEPATH -= %{_includedir}" >> settings.pro
echo "INCLUDEPATH += $temp%{_includedir}" >> settings.pro
echo "INCLUDEPATH += %{_includedir}" >> settings.pro
echo "LIBS *= -L$temp%{_libdir}" >> settings.pro
echo "QMAKE_LIBDIR += $temp%{_libdir}" >> targetdep.pro

./configure	--prefix=${temp}%{_prefix} \
		--libdir=%{_libdir} \
		--libdir-name=%{_lib} \
		--logfile=config.log \
		--python=%{__python2} \
		--enable-all \
		--enable-new-exif \
		--disable-mp3lame \
		--enable-mp3lame-dlopen

%make

popd


%install
INSTALL_ROOT=%{buildroot}; export INSTALL_ROOT

%makeinstall_std -C mythtv

%makeinstall_std -C mythtv/bindings/perl

%if %{maenable}
%multiarch_includes %{buildroot}%{_includedir}/mythtv/mythconfig.h
%endif

mkdir -p %{buildroot}%{_localstatedir}/lib/mythtv/recordings
mkdir -p %{buildroot}%{_var}/cache/mythtv
mkdir -p %{buildroot}%{_logdir}/mythtv

install -p -m644 mythtv/mythbackend.service -D %{buildroot}%{_unitdir}/mythbackend.service
install -p -m644 mythtv/mythbackend.sysconfig -D %{buildroot}%{_sysconfdir}/sysconfig/mythbackend
install -p -m644 mythtv/mythbackend.logrotate -D %{buildroot}%{_sysconfdir}/logrotate.d/mythbackend.logrotate

# wmsession.d for mythfrontend
install -p -m644 %{SOURCE4} -D %{buildroot}%{_sysconfdir}/X11/wmsession.d/99MythFrontend

# icon
install -p -m755 %{SOURCE5} -D %{buildroot}%{_miconsdir}/%{name}.png
install -p -m755 %{SOURCE6} -D %{buildroot}%{_iconsdir}/%{name}.png
install -p -m755 %{SOURCE7} -D %{buildroot}%{_liconsdir}/%{name}.png

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

cat > mythtv/README.install.urpmi <<EOF
You can import the initial database by running:
mysql -u root -p < %{_datadir}/mythtv/initialdb/mc.sql
(you can omit -p if you do not have the password set)
EOF

mkdir -p %{buildroot}%{_libdir}/mythtv/plugins

install -d -m755 %{buildroot}%{_datadir}/mythtv/initialdb
install -m644 mythtv/database/* %{buildroot}%{_datadir}/mythtv/initialdb

# install a few useful contrib scripts
cp -a mythtv/contrib %{buildroot}%{_datadir}/mythtv

%makeinstall_std -C mythplugins

#mythgallery
mkdir -p %{buildroot}%{_localstatedir}/lib/pictures
#mythmusic
mkdir -p %{buildroot}%{_localstatedir}/lib/mythmusic

mkdir -p %{buildroot}{%_docdir}/mythtv-plugin-{browser,gallery,game,music,netvision,news,weather,video,zoneminder}

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

rm -f %{buildroot}%{_datadir}/mythtv/contrib/development/tsc-calibrate/tsc-calibrate.c
rm -f %{buildroot}%{_datadir}/mythtv/mytharchive/themes/burnthemestrings.h

find %{buildroot} -name *.a -delete

#cb fix odd install location
mkdir -p %{buildroot}%{perl_vendorlib}
mv %{buildroot}%{buildroot}%{perl_vendorlib}/* %{buildroot}%{perl_vendorlib}

%pre backend
# Add the "mythtv" user
%_pre_useradd mythtv %{_localstatedir}/lib/mythtv /sbin/nologin
%{_bindir}/gpasswd -a mythtv audio &>/dev/null
%{_bindir}/gpasswd -a mythtv input &>/dev/null
%{_bindir}/gpasswd -a mythtv tty &>/dev/null
%{_bindir}/gpasswd -a mythtv video &>/dev/null

%postun backend
%_postun_userdel mythtv

%files doc
%doc mythtv/README mythtv/UPGRADING mythtv/AUTHORS mythtv/COPYING mythtv/FAQ
%doc mythtv/keys.txt
%doc mythtv/contrib
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
%{_datadir}/mythtv/CDS_scpd.xml
%{_datadir}/mythtv/CMGR_scpd.xml
%{_datadir}/mythtv/MFEXML_scpd.xml
%{_datadir}/mythtv/MSRR_scpd.xml
%{_datadir}/mythtv/MXML_scpd.xml
%{_datadir}/mythtv/devicemaster.xml
%{_datadir}/mythtv/deviceslave.xml
%{_datadir}/%{name}/mythconverg*.pl
%dir %{_datadir}/%{name}/locales
%{_datadir}/%{name}/locales/*
%dir %{_datadir}/%{name}/metadata
%{_datadir}/%{name}/metadata/Movie
%{_datadir}/%{name}/metadata/Television
%dir %{_datadir}/%{name}/hardwareprofile
%{_datadir}/%{name}/hardwareprofile/*

%files backend
%doc mythtv/README.install.urpmi
%{_bindir}/mythbackend
%{_bindir}/mythhdhomerun_config
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
%exclude %{_datadir}/mythtv/setup.xml
%{_bindir}/mythwelcome
%{_bindir}/mythfrontend
%{_bindir}/mythff*
%{_bindir}/mythlcdserver
%{_bindir}/mythshutdown
%{_bindir}/mythscreenwizard
%{_bindir}/mythavtest
%dir %{_libdir}/mythtv
%{_libdir}/mythtv/filters
%dir %{_libdir}/mythtv/plugins
%dir %{_datadir}/mythtv
%dir %{_datadir}/mythtv/fonts
%{_datadir}/mythtv/fonts/*.ttf
%{_datadir}/mythtv/fonts/*.otf
%dir %{_datadir}/mythtv/i18n
%{_datadir}/mythtv/i18n/mythfrontend*
%{_datadir}/applications/mandriva-mythtv-frontend.desktop

%files setup
%{_bindir}/mythtv-setup
%{_datadir}/applications/mandriva-mythtv-setup.desktop
%dir %{_datadir}/mythtv
%{_datadir}/mythtv/setup.xml

%files themes-base
%dir %{_datadir}/mythtv
%dir %{_datadir}/mythtv/themes
%{_datadir}/mythtv/themes/mythuitheme.dtd
%{_datadir}/mythtv/themes/classic
%{_datadir}/mythtv/themes/defaultmenu
%{_datadir}/mythtv/themes/DVR
%{_datadir}/mythtv/themes/mediacentermenu
%{_datadir}/mythtv/themes/MythCenter
%{_datadir}/mythtv/themes/MythCenter-wide
%{_datadir}/mythtv/themes/Slave
%{_datadir}/mythtv/themes/Terra
%dir %{_datadir}/mythtv/themes/default-wide
%dir %{_datadir}/mythtv/themes/default-wide/shared
%dir %{_datadir}/mythtv/themes/default
%dir %{_datadir}/mythtv/themes/default/shared

%{_datadir}/mythtv/themes/default-wide/appear-ui.xml
%{_datadir}/mythtv/themes/default-wide/bar.png
%{_datadir}/mythtv/themes/default-wide/base.xml
%{_datadir}/mythtv/themes/default-wide/button_wide_background.png
%{_datadir}/mythtv/themes/default-wide/button_wide_pushed_background.png
%{_datadir}/mythtv/themes/default-wide/button_wide_selected_background.png
%{_datadir}/mythtv/themes/default-wide/config-ui.xml
%{_datadir}/mythtv/themes/default-wide/controls-ui.xml
%{_datadir}/mythtv/themes/default-wide/cr-lines.png
%{_datadir}/mythtv/themes/default-wide/cr-selectbar.png
%{_datadir}/mythtv/themes/default-wide/def-ro-lines.png
%{_datadir}/mythtv/themes/default-wide/filler.png
%{_datadir}/mythtv/themes/default-wide/md_progress_background.png
%{_datadir}/mythtv/themes/default-wide/mv_browse_background.png
%{_datadir}/mythtv/themes/default-wide/mv_browse_nocover_large.png
%{_datadir}/mythtv/themes/default-wide/mv_browse_selector.png
%{_datadir}/mythtv/themes/default-wide/mv_itemdetail_popup.png
%{_datadir}/mythtv/themes/default-wide/mv_results_popup.png
%{_datadir}/mythtv/themes/default-wide/osd.xml
%{_datadir}/mythtv/themes/default-wide/pd-background.png
%{_datadir}/mythtv/themes/default-wide/pf-background.png
%{_datadir}/mythtv/themes/default-wide/pf-lines.png
%{_datadir}/mythtv/themes/default-wide/pf-sel1.png
%{_datadir}/mythtv/themes/default-wide/pf-sel2.png
%{_datadir}/mythtv/themes/default-wide/pf-sel3.png
%{_datadir}/mythtv/themes/default-wide/pf-top.png
%{_datadir}/mythtv/themes/default-wide/preview.png
%{_datadir}/mythtv/themes/default-wide/reclist_background.png
%{_datadir}/mythtv/themes/default-wide/recordings-ui.xml
%{_datadir}/mythtv/themes/default-wide/rk-lines.png
%{_datadir}/mythtv/themes/default-wide/rk-selectbar.png
%{_datadir}/mythtv/themes/default-wide/schedule-ui.xml
%{_datadir}/mythtv/themes/default-wide/selectbar.png
%{_datadir}/mythtv/themes/default-wide/settings-ui.xml
%{_datadir}/mythtv/themes/default-wide/shared/grid_back_reg.png
%{_datadir}/mythtv/themes/default-wide/shared/grid_back_sel.png
%{_datadir}/mythtv/themes/default-wide/shared/grid_noimage.png
%{_datadir}/mythtv/themes/default-wide/solid-container.png
%{_datadir}/mythtv/themes/default-wide/solid-cr-background.png
%{_datadir}/mythtv/themes/default-wide/status-bar.png
%{_datadir}/mythtv/themes/default-wide/status-ui.xml
%{_datadir}/mythtv/themes/default-wide/text_button_off.png
%{_datadir}/mythtv/themes/default-wide/text_button_on.png
%{_datadir}/mythtv/themes/default-wide/text_button_pushed.png
%{_datadir}/mythtv/themes/default-wide/track_info_background.png
%{_datadir}/mythtv/themes/default-wide/trans-backup.png
%{_datadir}/mythtv/themes/default-wide/trans-container.png
%{_datadir}/mythtv/themes/default-wide/trans-cr-background.png
%{_datadir}/mythtv/themes/default-wide/trans-rk-background.png
%{_datadir}/mythtv/themes/default-wide/trans-sr-background.png
%{_datadir}/mythtv/themes/default-wide/video-ui.xml
%{_datadir}/mythtv/themes/default-wide/welcome-ui.xml
%{_datadir}/mythtv/themes/default/appear-ui.xml
%{_datadir}/mythtv/themes/default/autoexpire.png
%{_datadir}/mythtv/themes/default/avchd.png
%{_datadir}/mythtv/themes/default/background.png
%{_datadir}/mythtv/themes/default/backup.png
%{_datadir}/mythtv/themes/default/bar.png
%{_datadir}/mythtv/themes/default/base.xml
%{_datadir}/mythtv/themes/default/blank.png
%{_datadir}/mythtv/themes/default/blankbutton_off.png
%{_datadir}/mythtv/themes/default/blankbutton_on.png
%{_datadir}/mythtv/themes/default/blankbutton_pushed.png
%{_datadir}/mythtv/themes/default/bookmark.png
%{_datadir}/mythtv/themes/default/bottomright.png
%{_datadir}/mythtv/themes/default/busyimages
%{_datadir}/mythtv/themes/default/button_background.png
%{_datadir}/mythtv/themes/default/button_pushed_background.png
%{_datadir}/mythtv/themes/default/button_selected_background.png
%{_datadir}/mythtv/themes/default/categories.xml
%{_datadir}/mythtv/themes/default/cc.png
%{_datadir}/mythtv/themes/default/check.png
%{_datadir}/mythtv/themes/default/checkbox_background_off.png
%{_datadir}/mythtv/themes/default/checkbox_background_selected.png
%{_datadir}/mythtv/themes/default/checkbox_fullcheck.png
%{_datadir}/mythtv/themes/default/checkbox_halfcheck.png
%{_datadir}/mythtv/themes/default/checked.png
%{_datadir}/mythtv/themes/default/checked_high.png
%{_datadir}/mythtv/themes/default/commflagged.png
%{_datadir}/mythtv/themes/default/config-ui.xml
%{_datadir}/mythtv/themes/default/container.png
%{_datadir}/mythtv/themes/default/controls-ui.xml
%{_datadir}/mythtv/themes/default/cr-background.png
%{_datadir}/mythtv/themes/default/cr-lines.png
%{_datadir}/mythtv/themes/default/cr-selectbar.png
%{_datadir}/mythtv/themes/default/cursor.png
%{_datadir}/mythtv/themes/default/cutlist.png
%{_datadir}/mythtv/themes/default/damaged.png
%{_datadir}/mythtv/themes/default/dd.png
%{_datadir}/mythtv/themes/default/def-ro-lines.png
%{_datadir}/mythtv/themes/default/down_arrow.png
%{_datadir}/mythtv/themes/default/downarrow.png
%{_datadir}/mythtv/themes/default/dummy1280x720p29.97.ts
%{_datadir}/mythtv/themes/default/dummy1920x1088p29.97.ts
%{_datadir}/mythtv/themes/default/dummy640x480p29.97.ts
%{_datadir}/mythtv/themes/default/dummy720x480p29.97.ts
%{_datadir}/mythtv/themes/default/dummy720x576p25.00.ts
%{_datadir}/mythtv/themes/default/dummy768x576p50.00.ts
%{_datadir}/mythtv/themes/default/error.png
%{_datadir}/mythtv/themes/default/filler.png
%{_datadir}/mythtv/themes/default/gg-arrow-down.png
%{_datadir}/mythtv/themes/default/gg-arrow-left.png
%{_datadir}/mythtv/themes/default/gg-arrow-right.png
%{_datadir}/mythtv/themes/default/gg-arrow-up.png
%{_datadir}/mythtv/themes/default/gg-chans.png
%{_datadir}/mythtv/themes/default/gg-rs-all.png
%{_datadir}/mythtv/themes/default/gg-rs-channel.png
%{_datadir}/mythtv/themes/default/gg-rs-findone.png
%{_datadir}/mythtv/themes/default/gg-rs-override.png
%{_datadir}/mythtv/themes/default/gg-rs-single.png
%{_datadir}/mythtv/themes/default/gg-rs-timeslot.png
%{_datadir}/mythtv/themes/default/gg-rs-weekslot.png
%{_datadir}/mythtv/themes/default/gg-times.png
%{_datadir}/mythtv/themes/default/hd.png
%{_datadir}/mythtv/themes/default/hd1080.png
%{_datadir}/mythtv/themes/default/hd720.png
%{_datadir}/mythtv/themes/default/htmls
%{_datadir}/mythtv/themes/default/keyboard
%{_datadir}/mythtv/themes/default/lb-arrow.png
%{_datadir}/mythtv/themes/default/lb-check-empty.png
%{_datadir}/mythtv/themes/default/lb-check-full.png
%{_datadir}/mythtv/themes/default/lb-check-half.png
%{_datadir}/mythtv/themes/default/lb-dnarrow-reg.png
%{_datadir}/mythtv/themes/default/lb-dnarrow-sel.png
%{_datadir}/mythtv/themes/default/lb-ltarrow-reg.png
%{_datadir}/mythtv/themes/default/lb-ltarrow-sel.png
%{_datadir}/mythtv/themes/default/lb-rtarrow-reg.png
%{_datadir}/mythtv/themes/default/lb-rtarrow-sel.png
%{_datadir}/mythtv/themes/default/lb-uparrow-reg.png
%{_datadir}/mythtv/themes/default/lb-uparrow-sel.png
%{_datadir}/mythtv/themes/default/left_arrow.png
%{_datadir}/mythtv/themes/default/leftarrow.png
%{_datadir}/mythtv/themes/default/leftright_off.png
%{_datadir}/mythtv/themes/default/leftright_on.png
%{_datadir}/mythtv/themes/default/leftright_pushed.png
%{_datadir}/mythtv/themes/default/locale
%{_datadir}/mythtv/themes/default/md_progress_background.png
%{_datadir}/mythtv/themes/default/md_rip_banner.png
%{_datadir}/mythtv/themes/default/menu_cutlist.xml
%{_datadir}/mythtv/themes/default/menu_cutlist_compact.xml
%{_datadir}/mythtv/themes/default/menu_playback.xml
%{_datadir}/mythtv/themes/default/menu_playback_compact.xml
%{_datadir}/mythtv/themes/default/mono.png
%{_datadir}/mythtv/themes/default/mv_browse_background.png
%{_datadir}/mythtv/themes/default/mv_browse_selector.png
%{_datadir}/mythtv/themes/default/mv_filerequest.png
%{_datadir}/mythtv/themes/default/mv_itemdetail_popup.png
%{_datadir}/mythtv/themes/default/mv_level_high.png
%{_datadir}/mythtv/themes/default/mv_level_low.png
%{_datadir}/mythtv/themes/default/mv_level_lowest.png
%{_datadir}/mythtv/themes/default/mv_level_medium.png
%{_datadir}/mythtv/themes/default/mv_level_none.png
%{_datadir}/mythtv/themes/default/mv_results_popup.png
%{_datadir}/mythtv/themes/default/mythdialogbox-background.png
%{_datadir}/mythtv/themes/default/mythfilebrowser-background.png
%{_datadir}/mythtv/themes/default/mythprogressdialog-background.png
%{_datadir}/mythtv/themes/default/noartwork.png
%{_datadir}/mythtv/themes/default/noartwork512.png
%{_datadir}/mythtv/themes/default/notification-ui.xml
%{_datadir}/mythtv/themes/default/osd.xml
%{_datadir}/mythtv/themes/default/osd_subtitle.xml
%{_datadir}/mythtv/themes/default/pd-background.png
%{_datadir}/mythtv/themes/default/pf-background.png
%{_datadir}/mythtv/themes/default/pf-lines.png
%{_datadir}/mythtv/themes/default/pf-sel1.png
%{_datadir}/mythtv/themes/default/pf-sel2.png
%{_datadir}/mythtv/themes/default/pf-sel3.png
%{_datadir}/mythtv/themes/default/pf-top.png
%{_datadir}/mythtv/themes/default/pf-topbackground.png
%{_datadir}/mythtv/themes/default/playlist_yes.png
%{_datadir}/mythtv/themes/default/preview.png
%{_datadir}/mythtv/themes/default/processing.png
%{_datadir}/mythtv/themes/default/progressbar_background.png
%{_datadir}/mythtv/themes/default/progressbar_fill.png
%{_datadir}/mythtv/themes/default/progressbar_fill2.png
%{_datadir}/mythtv/themes/default/reclist_background.png
%{_datadir}/mythtv/themes/default/recordings-ui.xml
%{_datadir}/mythtv/themes/default/right_arrow.png
%{_datadir}/mythtv/themes/default/rightarrow.png
%{_datadir}/mythtv/themes/default/rk-background.png
%{_datadir}/mythtv/themes/default/rk-lines.png
%{_datadir}/mythtv/themes/default/rk-selectbar.png
%{_datadir}/mythtv/themes/default/schedule-ui.xml
%{_datadir}/mythtv/themes/default/schedule_conflict.png
%{_datadir}/mythtv/themes/default/schedule_disabled.png
%{_datadir}/mythtv/themes/default/schedule_other.png
%{_datadir}/mythtv/themes/default/schedule_record.png
%{_datadir}/mythtv/themes/default/schedule_recording.png
%{_datadir}/mythtv/themes/default/selectbar.png
%{_datadir}/mythtv/themes/default/settings-ui.xml
%{_datadir}/mythtv/themes/default/shared/0_stars.png
%{_datadir}/mythtv/themes/default/shared/10_stars.png
%{_datadir}/mythtv/themes/default/shared/1_stars.png
%{_datadir}/mythtv/themes/default/shared/2_stars.png
%{_datadir}/mythtv/themes/default/shared/3_stars.png
%{_datadir}/mythtv/themes/default/shared/4_stars.png
%{_datadir}/mythtv/themes/default/shared/5_stars.png
%{_datadir}/mythtv/themes/default/shared/6_stars.png
%{_datadir}/mythtv/themes/default/shared/7_stars.png
%{_datadir}/mythtv/themes/default/shared/8_stars.png
%{_datadir}/mythtv/themes/default/shared/9_stars.png
%{_datadir}/mythtv/themes/default/shared/directory.png
%{_datadir}/mythtv/themes/default/shared/executable.png
%{_datadir}/mythtv/themes/default/shared/file.png
%{_datadir}/mythtv/themes/default/shared/grid_back_reg.png
%{_datadir}/mythtv/themes/default/shared/grid_back_sel.png
%{_datadir}/mythtv/themes/default/shared/grid_noimage.png
%{_datadir}/mythtv/themes/default/shared/secure.png
%{_datadir}/mythtv/themes/default/shared/unsecure.png
%{_datadir}/mythtv/themes/default/shared/updirectory.png
%{_datadir}/mythtv/themes/default/small_watched.png
%{_datadir}/mythtv/themes/default/solid-container.png
%{_datadir}/mythtv/themes/default/solid-cr-background.png
%{_datadir}/mythtv/themes/default/sr-background.png
%{_datadir}/mythtv/themes/default/status-bar.png
%{_datadir}/mythtv/themes/default/status-ui.xml
%{_datadir}/mythtv/themes/default/stereo.png
%{_datadir}/mythtv/themes/default/subs.png
%{_datadir}/mythtv/themes/default/subs_onscreen.png
%{_datadir}/mythtv/themes/default/surround.png
%{_datadir}/mythtv/themes/default/text_button_off.png
%{_datadir}/mythtv/themes/default/text_button_on.png
%{_datadir}/mythtv/themes/default/text_button_pushed.png
%{_datadir}/mythtv/themes/default/topleft.png
%{_datadir}/mythtv/themes/default/trans-backup.png
%{_datadir}/mythtv/themes/default/trans-container.png
%{_datadir}/mythtv/themes/default/trans-cr-background.png
%{_datadir}/mythtv/themes/default/trans-rk-background.png
%{_datadir}/mythtv/themes/default/trans-sr-background.png
%{_datadir}/mythtv/themes/default/unchecked.png
%{_datadir}/mythtv/themes/default/unchecked_high.png
%{_datadir}/mythtv/themes/default/up_arrow.png
%{_datadir}/mythtv/themes/default/uparrow.png
%{_datadir}/mythtv/themes/default/very_wide_button_background.png
%{_datadir}/mythtv/themes/default/very_wide_button_pushed_background.png
%{_datadir}/mythtv/themes/default/very_wide_button_selected_background.png
%{_datadir}/mythtv/themes/default/video-ui.xml
%{_datadir}/mythtv/themes/default/warning.png
%{_datadir}/mythtv/themes/default/watched.png
%{_datadir}/mythtv/themes/default/welcome-ui.xml
%{_datadir}/mythtv/themes/default/wide.png
%{_datadir}/mythtv/themes/default/wide_button_background.png
%{_datadir}/mythtv/themes/default/wide_button_pushed_background.png
%{_datadir}/mythtv/themes/default/wide_button_selected_background.png

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
%{_libdir}/libmythswscale.so.%{swscmaj}*

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
%{py2_puresitedir}/MythTV
%{py2_puresitedir}/MythTV*.egg-info

%files -n php-mythtv
%{_datadir}/%{name}/bindings/php


%files plugin-browser
%doc mythplugins/mythbrowser/README mythplugins/mythbrowser/COPYING mythplugins/mythbrowser/AUTHORS
%{_libdir}/mythtv/plugins/libmythbrowser.so
%{_datadir}/mythtv/i18n/mythbrowser_*.qm
%{_datadir}/mythtv/themes/default*/browser-ui.xml
%{_datadir}/mythtv/themes/default*/mb_*.png

%files plugin-gallery
%doc mythplugins/mythgallery/README*
%{_libdir}/mythtv/plugins/libmythgallery.so
%{_datadir}/mythtv/i18n/mythgallery_*.qm
%{_datadir}/mythtv/themes/default*/gallery*
%{_localstatedir}/lib/pictures

%files plugin-game
%doc mythplugins/mythgame/romdb*
%{_libdir}/mythtv/plugins/libmythgame.so
%{_datadir}/mythtv/i18n/mythgame_*.qm
%{_datadir}/mythtv/game_settings.xml
%{_datadir}/mythtv/themes/default*/game*
%dir %{_datadir}/mythtv/metadata
%{_datadir}/mythtv/metadata/Game

%files plugin-music
%doc mythplugins/mythmusic/AUTHORS mythplugins/mythmusic/COPYING mythplugins/mythmusic/README* mythplugins/mythmusic/musicdb
%{_datadir}/mythtv/music_settings.xml
%{_datadir}/mythtv/musicmenu.xml
%{_datadir}/mythtv/mythmusic/streams.xml
%{_libdir}/mythtv/plugins/libmythmusic.so
%{_localstatedir}/lib/mythmusic
%{_datadir}/mythtv/i18n/mythmusic_*.qm
%{_datadir}/mythtv/themes/default/ff_button*.png
%{_datadir}/mythtv/themes/default*/mm_*.png
%{_datadir}/mythtv/themes/default*/mm-*.png
%{_datadir}/mythtv/themes/default/music-*.png
%{_datadir}/mythtv/themes/default*/*music*.xml
%{_datadir}/mythtv/themes/default/next_button*.png
%{_datadir}/mythtv/themes/default/pause_button*.png
%{_datadir}/mythtv/themes/default/play_button*.png
%{_datadir}/mythtv/themes/default/prev_button*.png
%{_datadir}/mythtv/themes/default/rew_button*.png
%{_datadir}/mythtv/themes/default/selectionbar.png
%{_datadir}/mythtv/themes/default/stop_button*.png
%{_datadir}/mythtv/themes/default/track_info_background.png
%{_datadir}/mythtv/themes/default/miniplayer_background.png
%{_datadir}/mythtv/themes/default/stream-ui.xml
%{_datadir}/mythtv/themes/default-wide/music-sel-bg.png
%{_datadir}/mythtv/themes/default-wide/stream-ui.xml

%files plugin-netvision
%doc mythplugins/mythnetvision/README mythplugins/mythnetvision/ChangeLog mythplugins/mythnetvision/AUTHORS
%{_bindir}/mythfillnetvision
%{_libdir}/mythtv/plugins/libmythnetvision.so
%{_datadir}/mythtv/i18n/mythnetvision_*.qm
%{_datadir}/mythtv/mythnetvision
%{_datadir}/mythtv/netvisionmenu.xml
%{_datadir}/mythtv/themes/default*/netvision*.xml

%files plugin-news
%doc mythplugins/mythnews/AUTHORS mythplugins/mythnews/COPYING mythplugins/mythnews/ChangeLog mythplugins/mythnews/README*
%{_libdir}/mythtv/plugins/libmythnews.so
%{_datadir}/mythtv/i18n/mythnews_*.qm
%{_datadir}/mythtv/mythnews
%{_datadir}/mythtv/themes/default*/news*
%{_datadir}/mythtv/themes/default/enclosures.png
%{_datadir}/mythtv/themes/default/need-download.png
%{_datadir}/mythtv/themes/default/podcast.png

%files plugin-weather
%doc mythplugins/mythweather/AUTHORS mythplugins/mythweather/COPYING mythplugins/mythweather/README*
%{_libdir}/mythtv/plugins/libmythweather.so
%{_datadir}/mythtv/i18n/mythweather_*.qm
%{_datadir}/mythtv/mythweather
%{_datadir}/mythtv/themes/default/cloudy.png
%{_datadir}/mythtv/themes/default/fair.png
%{_datadir}/mythtv/themes/default/flurries.png
%{_datadir}/mythtv/themes/default/fog.png
%{_datadir}/mythtv/themes/default/logo.png
%{_datadir}/mythtv/themes/default/lshowers.png
%{_datadir}/mythtv/themes/default/mcloudy.png
%{_datadir}/mythtv/themes/default/pcloudy.png
%{_datadir}/mythtv/themes/default/rainsnow.png
%{_datadir}/mythtv/themes/default/showers.png
%{_datadir}/mythtv/themes/default/snowshow.png
%{_datadir}/mythtv/themes/default/sunny.png
%{_datadir}/mythtv/themes/default/thunshowers.png
%{_datadir}/mythtv/themes/default/unknown.png
%{_datadir}/mythtv/themes/default*/mw*.png
%{_datadir}/mythtv/themes/default*/weather-ui.xml
%{_datadir}/mythtv/weather_settings.xml

%files plugin-zoneminder
%doc mythplugins/mythzoneminder/README mythplugins/mythzoneminder/COPYING mythplugins/mythzoneminder/AUTHORS
%{_bindir}/mythzmserver
%{_libdir}/mythtv/plugins/libmythzoneminder.so
%{_datadir}/mythtv/zonemindermenu.xml
%{_datadir}/mythtv/themes/default*/zoneminder*.xml
%{_datadir}/mythtv/themes/default*/mz_*.png
%{_datadir}/mythtv/i18n/mythzoneminder_*.qm

%files plugin-archive
%{_bindir}/mytharchivehelper
%{_libdir}/mythtv/plugins/libmytharchive.so
%{_datadir}/mythtv/archive*.xml
%{_datadir}/mythtv/mytharchive
%{_datadir}/mythtv/themes/default/ma_*.png
%{_datadir}/mythtv/themes/default/mytharchive-ui.xml
%{_datadir}/mythtv/themes/default/mythburn-ui.xml
%{_datadir}/mythtv/themes/default/mythnative-ui.xml
%{_datadir}/mythtv/themes/default-wide/mytharchive-ui.xml
%{_datadir}/mythtv/themes/default-wide/mythburn-ui.xml
%{_datadir}/mythtv/themes/default-wide/mythnative-ui.xml
%{_datadir}/mythtv/i18n/mytharchive_*.qm

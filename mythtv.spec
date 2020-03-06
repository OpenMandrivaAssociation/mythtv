# Note: When updating version, also update the update-fixes.sh script's version
# and rerun it. This will generate a new fixes patch and update the spec
# automatically.
%define gitversion v30.0-85-gab250
%define fixesdate 20200217
%define rel 1

%if %{fixesdate}
%define release %mkrel %fixesdate.%rel
%else
%define release %mkrel %rel
%endif

%define lib_name_orig   libmyth
%define lib_major       30
%define lib_name        %mklibname myth %{lib_major}
%define lib_name_devel  %mklibname myth -d

%define maenable 1

#set default build options
# disabled as overrides xv
%define build_directfb          0
%define build_dts               0
%define build_faac              0
%define build_faad              0
#lame is no longer tainted
%define build_lame              1
%define build_x264              0
%define build_x265              0
%define build_xvid              0

# --with plf
%if "%distro_section" == "tainted"
%global build_tainted 1
%else
%global build_tainted 0
%endif
%if %{build_tainted}
%define build_dts               1
%define build_faac              0
%define build_faad              1
%define build_lame              1
%define build_x264              1
%define build_x265              1
%define build_xvid              1
%endif

#enable/disable building for certain hardware
%{?_without_directfb:           %global build_directfb 0}
%{?_without_dts:                %global build_dts 0}
%{?_without_faac:               %global build_faac 0}
%{?_without_faad:               %global build_faad 0}
%{?_without_lame:               %global build_lame 0}
%{?_without_x264:               %global build_x264 0}
%{?_without_x265:               %global build_x265 0}
%{?_without_xvid:               %global build_xvid 0}

%{?_with_directfb:              %global build_directfb 1}
%{?_with_dts:                   %global build_dts 1}
%{?_with_faac:                  %global build_faac 1}
%{?_with_faad:                  %global build_faad 1}
%{?_with_lame:                  %global build_lame 1}
%{?_with_x264:                  %global build_x264 1}
%{?_with_x265:                  %global build_x265 1}
%{?_with_xvid:                  %global build_xvid 1}

# Turn off the brp-python-bytecompile automagic
%global _python_bytecompile_extra 0

# The filters in mythfrontend shouldn't really be exposed as provides.
%global _exclude_files_from_autoprov %{?_exclude_files_from_autoprov:%_exclude_files_from_autoprov|}%{_libdir}/%{name}/filters/.*\\.so$

Summary:        A personal video recorder (PVR) application
Name:           mythtv
Version:        30.0
Release:        %{release}
URL:            http://www.mythtv.org/
License:        GPLv2 + GPLv3
Group:          Video/Television
Source0:        https://github.com/MythTV/mythtv/archive/v%{version}/mythtv-%{version}.tar.gz
Source1:        mythbackend.sysconfig.in
Source2:        mythbackend.init.in
Source3:        mythbackend.logrotate.in
Source4:        mythfrontend.desktop
Source5:        %name-16.png
Source6:        %name-32.png
Source7:        %name-48.png
Source8:        mythbackend.service.in
Source9:        update-fixes.sh
Source10:       mythtv.sysconfig.in
%if %{fixesdate}
Patch001: fixes-%{gitversion}.patch
%endif
# (cg) git format-patch --start-number 100 fixes/0.27..mga-0.27
Patch102: 0102-pulse-Do-not-suspend-PA-when-using-alsa-default.patch
Patch103: 0103-Fix-dns-sd-detection.patch
#add CFLAGS and LDFLAGS to QMAKE
Patch104: mythtv-0.28.1-qmake-mgaflags.patch
#fix build with new mariadb 10.2
Patch105: mythtv-30.0-mariadb10.2.patch
#fix mythavcodec linking
Patch106: mythtv-30.0-linking.patch
#enable xnvctrl support on Mageia
Patch107: mythtv-30.0-mageia-xnvctrl.patch
#use /run instead of /var/run
Patch108: 0001-Update-socket-locations-to-use-run-instead-of-var-ru.patch
Patch109: mythtv-python3.patch
Patch110: mythtv-py3_configure.patch

BuildRequires:  gdb
BuildRequires:  imagemagick
BuildRequires:  yasm
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblircclient0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xvmc)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(python3)
#BuildRequires:  python3dist(mysqlclient)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(urlgrabber)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libcec)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  crystalhd-devel
#BuildRequires:  hdhomerun-devel
%if %build_lame
BuildRequires:  lame-devel
%endif
%if %build_dts
BuildRequires:  pkgconfig(libdts)
%endif
%if %build_x264
BuildRequires:  pkgconfig(x264)
%endif
%if %build_x265
BuildRequires:  pkgconfig(x265)
%endif
%if %build_xvid
BuildRequires:  xvid-devel
%endif
%if %build_faac
BuildRequires:  libfaac-devel
%endif
%if %build_faad
BuildRequires:  libfaad2-devel
%endif
%if %{build_directfb}
BuildRequires:  libdirectfb-devel
%endif
BuildRequires:  pkgconfig(libavc1394)
BuildRequires:  pkgconfig(libiec61883)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
%if %maenable
#BuildRequires:  multiarch-utils
%endif
#BuildRequires:  perl(Net::UPnP::QueryResponse)
#BuildRequires:  perl(Net::UPnP::ControlPoint)

# For Plugins
BuildRequires:  pkgconfig(libvisual-0.4)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libbluray)
#BuildRequires:  pkgconfig(libcdaudio)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  cdda-devel
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  mysql-devel
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(theora)
BuildRequires:  python3dist(pycurl)
BuildRequires:  python3dist(oauth)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(Date::Manip)
#BuildRequires:  perl(DateTime::Format::ISO8601)
#BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(Class::Factory::Util)

# Bluray support
#BuildRequires:  ant
#BuildRequires:  java-devel
BuildRequires:  pkgconfig(libxml-2.0)


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

%if %{build_tainted}
This package is in the "tainted" section because it contains software that supports
codecs that may be covered by software patents.
%endif
%if !%build_lame
Note that this build does not support MP3 encoding when recording
into the NuppelVideo format.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at revision %{gitversion}
%endif

%package -n %{lib_name}
Summary:        Library providing mythtv support
Group:          System/Libraries
Provides:       %{lib_name_orig} = %{version}-%{release}

%description -n %{lib_name}
Common library code for MythTV and add-on modules (development)
MythTV provides a unified graphical interface for recording and viewing
television programs.

%if %{build_tainted}
This package is in the "tainted" section because it contains software that supports
codecs that may be covered by software patents.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at revision %{gitversion}
%endif

%package -n %{lib_name_devel}
Summary:        Development files for libmyth
Group:          Development/Other
Requires:       %{lib_name} = %{version}-%{release}
Provides:       %{lib_name_orig}-devel = %{version}-%{release}
Provides:       myth-devel = %{version}-%{release}

%description -n %{lib_name_devel}
This package contains the header files and libraries for developing
add-ons for mythtv.

%if %{build_tainted}
This package is in the "tainted" section because it contains software that supports
codecs that may be covered by software patents.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at revision %{gitversion}
%endif

%package themes-base
Summary:        Base themes for mythtv's frontend
Group:          Video/Television
BuildArch:      noarch

%description themes-base
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains only the base themes used by mythtv-frontend and
mythtv-setup.

%package common
Summary:        Common components needed by multiple other MythTV components
Group:          Video/Television
Requires:       perl-DBD-mysql

%description common
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains components needed by multiple other MythTV components.

%package frontend
Summary:        Client component of mythtv (a PVR)
Group:          Video/Television
Requires:       mythtv-themes-base = %{version}-%{release}
Requires:       mythtv-common = %{version}-%{release}
Requires:       qt5-database-plugin-mysql
Requires:       mplayer
%if %{build_tainted}
Requires:       transcode
Requires:       %mklibname dvdcss 2
%endif

%description frontend
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains only the client software, which provides a
front-end for playback and configuration.  It requires access to a
mythtv-backend installation, either on the same system or one
reachable via the network.

%if %{build_tainted}
This package is in the "tainted" section because it contains software that supports
codecs that may be covered by software patents.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at revision %{gitversion}
%endif

%package backend
Summary:        Server component of mythtv (a PVR)
Group:          Video/Television
Requires:       %{lib_name} = %{version}-%{release}
Requires:       mythtv-common = %{version}-%{release}
Requires:       qt5-database-plugin-mysql
Requires(post):  rpm-helper >= 0.24.8-1
Requires(preun): rpm-helper >= 0.24.8-1
Recommends:       mysql

%description backend
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains only the server software, which provides video
and audio capture and encoding services.  In order to be useful, it
requires a mythtv-frontend installation, either on the same system or
one reachable via the network.

%if %{build_tainted}
This package is in the "tainted" section because it contains software that supports
codecs that may be covered by software patents.
%endif
%if !%build_lame
Note that this build does not support MP3 encoding when recording
into the NuppelVideo format.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at revision %{gitversion}
%endif

%package setup
Summary:        Setup the mythtv backend
Group:          Video/Television
Requires:       mythtv-backend = %{version}-%{release}
Requires:       mythtv-themes-base = %{version}-%{release}
Provides:       mythtvsetup
Requires:       qt5-database-plugin-mysql

%description setup
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains the setup software for configuring the mythtv
backend.

%if %{build_tainted}
This package is in the "tainted" section because it contains software that supports
codecs that may be covered by software patents.
%endif
%if !%build_lame
Note that this build does not support MP3 encoding when recording
into the NuppelVideo format.
%endif
%if %{fixesdate}
This package is based on the MythTV "fixes" branch at revision %{gitversion}
%endif

%package doc
Summary:        MythTV documentation
Group:          Video/Television
BuildArch:      noarch
Requires:       mythtv-common >= %{version}-%{release}

%description doc
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains the documentation and contributed additional
scripts for MythTV.

%package -n perl-MythTV
Summary:        Perl bindings for MythTV
Group:          Development/Perl

%description -n perl-MythTV
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains the perl bindings for MythTV.

%package -n python3-mythtv
Summary:        Python 3 bindings for MythTV
Group:          Development/Python
Requires:       python3dist(mysqlclient)
Requires:       python3dist(lxml)
Requires:       python3dist(pycurl)
Requires:       python3dist(oauth)

Obsoletes:      python-mythtv < 0.28.1-20170528.12
Provides:       python-mythtv = %{version}-%{release}
Obsoletes:      python2-mythtv < 30.0-20190728.2

%description -n python3-mythtv
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains the python 3 bindings for MythTV.

%package -n php-mythtv
Summary:        PHP bindings for MythTV
Group:          Development/PHP
BuildArch:      noarch
Requires:       php-mysql

%description -n php-mythtv
MythTV provides a unified graphical interface for recording and viewing
television programs.

This package contains the PHP bindings for MythTV.

%package plugin-browser
Summary:        Full web browser for MythTV
URL:            http://www.mythtv.org/
Group:          Video/Television
Requires:       mythtv-frontend >= %{version}

%description plugin-browser
MythBrowser is a full web browser for MythTV.

%package plugin-gallery
Summary:        Gallery/slideshow module for MythTV
Group:          Video/Television
Requires:       mythtv-frontend >= %{version}

%description plugin-gallery
A gallery/slideshow module for MythTV.

%package plugin-game
Summary:        Game frontend for MythTV
Group:          Video/Television
Requires:       mythtv-frontend >= %{version}

%description plugin-game
A game frontend for MythTV.

%package plugin-music
Summary:        The music player add-on module for MythTV
Group:          Video/Television
#Requires:       cdparanoia
Requires:       mythtv-frontend >= %{version}

%description plugin-music
The music player add-on module for MythTV.

%if %{build_tainted}
This package is in the tainted section because it contains software that supports
codecs that may be covered by software patents.
%endif

%package plugin-netvision
Summary:        NetVision for MythTV
Group:          Video/Television
Requires:       python3-mythtv
Requires:       mythtv-frontend >= %{version}

%description plugin-netvision
NetVision for MythTV. View popular media website content.

%package plugin-news
Summary:        RSS News feed plugin for MythTV
Group:          Video/Television
Requires:       mythtv-frontend >= %{version}

%description plugin-news
An RSS News feed plugin for MythTV.

%package plugin-weather
Summary:        MythTV module that displays a weather forecast
Group:          Video/Television
Requires:       mythtv-frontend >= %{version}

%description plugin-weather
A MythTV module that displays a weather forcast.

%package plugin-zoneminder
Summary:        Security camera plugin for MythTV
Group:          Video/Television
Requires:       mythtv-frontend >= %{version}

%description plugin-zoneminder
A security camera plugin for MythTV.

%package plugin-archive
Summary:        Creates DVDs from your recorded shows
Group:          Video/Television
Requires:       dvd+rw-tools
Requires:       dvdauthor
Requires:       ffmpeg
Requires:       mjpegtools
Requires:       python3dist(pillow)
Requires:       python3dist(mysqlclient)
Requires:       mythtv-frontend >= %{version}
%if %{build_tainted}
Requires:       transcode
%endif
Requires:       cdrkit-genisoimage

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
%autopatch -p1

# (cg) The install scripts are pretty dumb at times and include these files
# so lets trash them early
find \( -name .gitignore -o -name "*.[0-9][0-9][0-9][0-9]" \) -delete

pushd mythtv
# (cg) As of 0.21, only contrib scripts are affected.
find contrib -type f | xargs grep -l /usr/local | xargs perl -pi -e's|/usr/local|%{_prefix}|g'

echo "QMAKE_PROJECT_DEPTH = 0" >> mythtv.pro
echo "QMAKE_PROJECT_DEPTH = 0" >> settings.pro

cp -a %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE8} %{SOURCE10} .
for file in mythbackend.init \
            mythbackend.service \
            mythbackend.sysconfig \
            mythtv.sysconfig \
            mythbackend.logrotate; do
  sed -e's|@logdir@|%{_logdir}|g' \
      -e's|@rundir@|%{_rundir}|g' \
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

# Fix the version reporting (which assumes git clone)
perl -pi -e"s|SOURCE_VERSION=.*|SOURCE_VERSION='%{version}-%{release} (aka %{gitversion})'\nBRANCH='fixes/%{version}'|" version.sh
popd

# remove -Wsuggest-override compile flags it generates plenty of build log
sed -i 's| -Wsuggest-override||' mythtv/configure

#(eatdirt) added -DHAVE_PTHREAD_H to fix udfreac.c for armv5. There is a
#conditional in there using either atomic, or fall back to pthread if
#HAVE_PTHREAD_H is defined.

%build
pushd mythtv
./configure \
  --prefix=%{_prefix} \
  --libdir-name=%{_lib} \
  --enable-dvb \
  --without-bindings=perl \
  --extra-cxxflags="%{optflags} -fomit-frame-pointer -fno-devirtualize" \
  --extra-cflags="%{optflags} -fomit-frame-pointer -fno-devirtualize -DHAVE_PTHREAD_H" \
  --extra-ldflags="%{ldflags}" \
  --python=%{__python3} \
%ifarch %arm
  --disable-vdpau \
  --disable-vaapi \
  --disable-opengl-video \
%else
  --enable-vdpau \
  --enable-vaapi \
  --enable-opengl-video \
%endif
  --enable-crystalhd \
  --enable-libfftw3 \
  --enable-libdns-sd \
  --enable-libvpx \
  --enable-sdl2 \
  --enable-bdjava \
%if %{build_tainted}
  --enable-nonfree \
%endif
%if %{build_x264}
  --enable-libx264 \
%endif
%if %{build_x265}
  --enable-libx265 \
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
  --enable-firewire \
  --enable-hdhomerun \
  --qmake=%{_qt5_bindir}/qmake

%make_build

# This is easier to do ourselves
pushd bindings/perl
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build
popd
popd

# Install temporarily to compile plugins
mkdir temp
temp=$(pwd)/temp
make -C mythtv install INSTALL_ROOT=$temp
export LD_LIBRARY_PATH=$temp%{_libdir}:$LD_LIBRARY_PATH

pushd mythplugins

# Fix things up so they can find our "temp" install location for mythtv libs
echo "QMAKE_PROJECT_DEPTH = 0" >> settings.pro
find . -name \*.pro \
  -exec sed -i -e "s,INCLUDEPATH += .\+/include/mythtv,INCLUDEPATH += $temp%{_includedir}/mythtv," {} \; \
  -exec sed -i -e "s,DEPLIBS = \$\${SYSROOT}\$\${LIBDIR},DEPLIBS = $temp%{_libdir}," {} \; \
  -exec sed -i -e "s,\$\${PREFIX}/include/mythtv,$temp%{_includedir}/mythtv," {} \;
echo "INCLUDEPATH -= \$\${PREFIX}/include" >> settings.pro
echo "INCLUDEPATH -= \$\${SYSROOT}/\$\${PREFIX}/include" >> settings.pro
echo "INCLUDEPATH -= %{_includedir}" >> settings.pro
echo "INCLUDEPATH += $temp%{_includedir}" >> settings.pro
echo "LIBS *= -L$temp%{_libdir}" >> settings.pro
echo "QMAKE_LIBDIR += $temp%{_libdir}" >> targetdep.pro

# (daviddavid) FIXME:
# the MythTV Python bindings is not found in "$temp" install by the
# check_py_lib script thus disabling MythNetvision due to missing dependencies
sed -i 's|check_py_lib MythTV|#check_py_lib MythTV|' configure

./configure \
  --prefix=${temp}%{_prefix} \
  --libdir=${_libdir} \
  --libdir-name=${_lib} \
  --python=%{__python3} \
  --enable-all \
  --qmake=%{_qt5_bindir}/qmake

%make_build

popd



%install
export INSTALL_ROOT=%{buildroot}

pushd mythtv
%make_install

pushd bindings/perl
%make_install
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
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig

install -p mythbackend.init %{buildroot}%{_initrddir}/mythbackend
install -p mythbackend.service %{buildroot}%{_unitdir}/mythbackend.service
install -p mythbackend.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/mythbackend
install -p mythtv.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/mythtv
install -p mythbackend.logrotate  %{buildroot}%{_sysconfdir}/logrotate.d

# wmsession.d for mythfrontend
mkdir -p %{buildroot}%{_datadir}/xsessions
install -p %{SOURCE4} %{buildroot}%{_datadir}/xsessions

# icon
install -d -m755 %{buildroot}/%{_miconsdir}
install -m755 %{SOURCE5} %{buildroot}/%{_miconsdir}/%name.png

install -d -m755 %{buildroot}/%{_iconsdir}
install -m755 %{SOURCE6} %{buildroot}/%{_iconsdir}/%name.png

install -d -m755 %{buildroot}/%{_liconsdir}
install -m755 %{SOURCE7} %{buildroot}/%{_liconsdir}/%name.png


# Menu entries
install -d -m755 %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/%{_real_vendor}-mythtv-frontend.desktop
[Desktop Entry]
Name=MythTV
Comment=Record, playback and watch TV
Exec=mythfrontend
Icon=%{name}
Terminal=false
Type=Application
Categories=Qt;AudioVideo;Video;TV;Recorder;
EOF
cat <<EOF > %{buildroot}%{_datadir}/applications/%{_real_vendor}-mythtv-setup.desktop
[Desktop Entry]
Name=MythTV Setup
Comment=Setup MythTV backend
Exec=mythtv-setup
Icon=%{name}
Terminal=false
Type=Application
Categories=Qt;AudioVideo;Video;TV;Recorder;
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

popd

pushd mythplugins
%make_install

#mythgallery
mkdir -p %{buildroot}%{_localstatedir}/lib/pictures
#mythmusic
mkdir -p %{buildroot}%{_localstatedir}/lib/mythmusic

mkdir -p %{buildroot}{%_docdir}/mythtv-plugin-{browser,gallery,game,music,netvision,news,weather,video,zoneminder}

popd

# Remove python egg-info as it's pointless
rm -f %{buildroot}%{python3_sitelib}/MythTV-*.egg-info

# (cg) We cover the package license so no need to include it separately
rm -f %{buildroot}%{_datadir}/%{name}/fonts/tiresias_gpl3.txt

# (cg) This is needed for the %%doc stuff on the subpackages for some reason...
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

# (cg) The mythzeromq stuff is not needed in our -devel package.
rm -f %{buildroot}%{_includedir}/zmq*.h* %{buildroot}%{_libdir}/pkgconfig/libmythzmq.pc
rmdir %{buildroot}%{_libdir}/pkgconfig 2>/dev/null || :

# (cg) Clean up some other stuff we don't want to include
rm -f %{buildroot}%{_libdir}/libmythqjson.prl

# python shebangs
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/%{name}/*

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
%doc mythtv/README mythtv/UPGRADING
%doc mythtv/AUTHORS mythtv/COPYING
%doc mythtv/FAQ
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
%{_bindir}/mythfilerecorder
%{_bindir}/mythexternrecorder
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/mythconverg_backup.pl
%{_datadir}/%{name}/mythconverg_restore.pl
%dir %{_datadir}/%{name}/locales
%{_datadir}/%{name}/locales/*
%dir %{_datadir}/%{name}/metadata
%{_datadir}/%{name}/metadata/*
%dir %{_datadir}/%{name}/hardwareprofile
%{_datadir}/%{name}/hardwareprofile/*
%exclude %{_datadir}/mythtv/metadata/Game

%files backend
%doc mythtv/README.install.urpmi
%{_bindir}/mythbackend
%{_bindir}/mythfilldatabase
%{_bindir}/mythjobqueue
%{_bindir}/mythmediaserver
%{_bindir}/mythreplex
%attr(-,mythtv,mythtv) %dir %{_localstatedir}/lib/mythtv
%attr(-,mythtv,mythtv) %dir %{_localstatedir}/lib/mythtv/recordings
%attr(-,mythtv,mythtv) %dir %{_var}/cache/mythtv
%{_unitdir}/mythbackend.service
%{_initrddir}/mythbackend
%config(noreplace) %{_sysconfdir}/sysconfig/mythbackend
%config(noreplace) %{_sysconfdir}/sysconfig/mythtv
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%attr(-,mythtv,mythtv) %dir %{_logdir}/mythtv
%{_datadir}/%{name}/backend-config
%dir %{_datadir}/%{name}/initialdb
%{_datadir}/%{name}/initialdb/mc.sql
%dir %{_datadir}/mythtv/internetcontent
%{_datadir}/mythtv/internetcontent/*

%files frontend
%config(noreplace) %{_datadir}/xsessions/mythfrontend.desktop
%{_bindir}/mythwelcome
%{_bindir}/mythfrontend
%{_bindir}/mythff*
%{_bindir}/mythlcdserver
%{_bindir}/mythscreenwizard
%{_bindir}/mythshutdown
%{_bindir}/mythavtest
%dir %{_libdir}/mythtv
%{_libdir}/mythtv/filters
%dir %{_libdir}/mythtv/plugins
%dir %{_datadir}/mythtv/fonts
%{_datadir}/mythtv/fonts/*.ttf
%{_datadir}/mythtv/fonts/*.otf
%dir %{_datadir}/mythtv/i18n
%{_datadir}/mythtv/i18n/mythfrontend_*.qm
%{_datadir}/applications/%{_real_vendor}-mythtv-frontend.desktop
%{_datadir}/mythtv/CDS_scpd.xml
%{_datadir}/mythtv/CMGR_scpd.xml
%{_datadir}/mythtv/MFEXML_scpd.xml
%{_datadir}/mythtv/MSRR_scpd.xml
%{_datadir}/mythtv/MXML_scpd.xml
%{_datadir}/mythtv/devicemaster.xml
%{_datadir}/mythtv/deviceslave.xml

%files setup
%{_bindir}/mythtv-setup
%{_datadir}/applications/%{_real_vendor}-mythtv-setup.desktop
%{_datadir}/mythtv/setup.xml

%files themes-base
%dir %{_datadir}/mythtv/themes
%{_datadir}/mythtv/themes/DVR/
%{_datadir}/mythtv/themes/MythCenter/
%{_datadir}/mythtv/themes/Slave/
%{_datadir}/mythtv/themes/Terra/
%{_datadir}/mythtv/themes/classic/
%{_datadir}/mythtv/themes/default-wide/
%{_datadir}/mythtv/themes/MythCenter-wide/
%{_datadir}/mythtv/themes/default/
%{_datadir}/mythtv/themes/defaultmenu/
%{_datadir}/mythtv/themes/mediacentermenu/
%{_datadir}/mythtv/themes/mythuitheme.dtd
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_liconsdir}/%name.png

%exclude %{_datadir}/mythtv/themes/default-wide/music-sel-bg.png
%exclude %{_datadir}/mythtv/themes/default-wide/stream-ui.xml
%exclude %{_datadir}/mythtv/themes/default-wide/mytharchive-ui.xml
%exclude %{_datadir}/mythtv/themes/default-wide/mythburn-ui.xml
%exclude %{_datadir}/mythtv/themes/default-wide/mythnative-ui.xml
%exclude %{_datadir}/mythtv/themes/default/ff_button*.png
%exclude %{_datadir}/mythtv/themes/default/music-*.png
%exclude %{_datadir}/mythtv/themes/default/next_button*.png
%exclude %{_datadir}/mythtv/themes/default/pause_button*.png
%exclude %{_datadir}/mythtv/themes/default/play_button*.png
%exclude %{_datadir}/mythtv/themes/default/prev_button*.png
%exclude %{_datadir}/mythtv/themes/default/rew_button*.png
%exclude %{_datadir}/mythtv/themes/default/selectionbar.png
%exclude %{_datadir}/mythtv/themes/default/stop_button*.png
%exclude %{_datadir}/mythtv/themes/default/track_info_background.png
%exclude %{_datadir}/mythtv/themes/default/miniplayer_background.png
%exclude %{_datadir}/mythtv/themes/default/stream-ui.xml
%exclude %{_datadir}/mythtv/themes/default/enclosures.png
%exclude %{_datadir}/mythtv/themes/default/need-download.png
%exclude %{_datadir}/mythtv/themes/default/podcast.png
%exclude %{_datadir}/mythtv/themes/default/cloudy.png
%exclude %{_datadir}/mythtv/themes/default/fair.png
%exclude %{_datadir}/mythtv/themes/default/flurries.png
%exclude %{_datadir}/mythtv/themes/default/fog.png
%exclude %{_datadir}/mythtv/themes/default/logo.png
%exclude %{_datadir}/mythtv/themes/default/lshowers.png
%exclude %{_datadir}/mythtv/themes/default/mcloudy.png
%exclude %{_datadir}/mythtv/themes/default/pcloudy.png
%exclude %{_datadir}/mythtv/themes/default/rainsnow.png
%exclude %{_datadir}/mythtv/themes/default/showers.png
%exclude %{_datadir}/mythtv/themes/default/snowshow.png
%exclude %{_datadir}/mythtv/themes/default/sunny.png
%exclude %{_datadir}/mythtv/themes/default/thunshowers.png
%exclude %{_datadir}/mythtv/themes/default/unknown.png
%exclude %{_datadir}/mythtv/themes/default/ma_*.png
%exclude %{_datadir}/mythtv/themes/default/mytharchive-ui.xml
%exclude %{_datadir}/mythtv/themes/default/mythburn-ui.xml
%exclude %{_datadir}/mythtv/themes/default/mythnative-ui.xml
%exclude %{_datadir}/mythtv/themes/default*/browser-ui.xml
%exclude %{_datadir}/mythtv/themes/default*/mb_*.png
%exclude %{_datadir}/mythtv/themes/default*/gallery*
%exclude %{_datadir}/mythtv/themes/default*/game*
%exclude %{_datadir}/mythtv/themes/default*/mm_*.png
%exclude %{_datadir}/mythtv/themes/default*/mm-*.png
%exclude %{_datadir}/mythtv/themes/default*/*music*.xml
%exclude %{_datadir}/mythtv/themes/default*/netvision*.xml
%exclude %{_datadir}/mythtv/themes/default*/news*
%exclude %{_datadir}/mythtv/themes/default*/mw*.png
%exclude %{_datadir}/mythtv/themes/default*/weather-ui.xml
%exclude %{_datadir}/mythtv/themes/default*/zoneminder*.xml
%exclude %{_datadir}/mythtv/themes/default*/mz_*.png

%files -n %{lib_name}
%{_libdir}/*.so.*

%files -n %{lib_name_devel}
%if %maenable
%multiarch %{multiarch_includedir}/mythtv/mythconfig.h
%endif
%{_includedir}/mythtv
# FIXME: Manually multiarch mythconfig.mak
%{_libdir}/*.so

%files -n perl-MythTV
%{perl_vendorlib}/MythTV.pm
%{perl_vendorlib}/MythTV
%{perl_vendorlib}/IO/Socket/INET/MythTV.pm

%files -n python3-mythtv
%{_bindir}/mythpython
%dir %{python3_sitelib}/MythTV
%{python3_sitelib}/MythTV/*

%files -n php-mythtv
%dir %{_datadir}/%{name}/bindings
%{_datadir}/%{name}/bindings/php

%files plugin-browser
%doc mythplugins/mythbrowser/README
%doc mythplugins/mythbrowser/COPYING
%doc mythplugins/mythbrowser/AUTHORS
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
%{_datadir}/mythtv/metadata/Game

%files plugin-music
%doc mythplugins/mythmusic/AUTHORS
%doc mythplugins/mythmusic/COPYING
%doc mythplugins/mythmusic/README*
%doc mythplugins/mythmusic/musicdb
%{_datadir}/mythtv/music_settings.xml
%{_datadir}/mythtv/musicmenu.xml
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
%doc mythplugins/mythnetvision/README
%doc mythplugins/mythnetvision/ChangeLog
%doc mythplugins/mythnetvision/AUTHORS
%{_bindir}/mythfillnetvision
%{_libdir}/mythtv/plugins/libmythnetvision.so
%{_datadir}/mythtv/i18n/mythnetvision_*.qm
%{_datadir}/mythtv/mythnetvision
%{_datadir}/mythtv/netvisionmenu.xml
%{_datadir}/mythtv/themes/default*/netvision*.xml

%files plugin-news
%doc mythplugins/mythnews/AUTHORS
%doc mythplugins/mythnews/COPYING
%doc mythplugins/mythnews/ChangeLog
%doc mythplugins/mythnews/README*
%{_libdir}/mythtv/plugins/libmythnews.so
%{_datadir}/mythtv/i18n/mythnews_*.qm
%{_datadir}/mythtv/mythnews
%{_datadir}/mythtv/themes/default*/news*
%{_datadir}/mythtv/themes/default/enclosures.png
%{_datadir}/mythtv/themes/default/need-download.png
%{_datadir}/mythtv/themes/default/podcast.png

%files plugin-weather
%doc mythplugins/mythweather/AUTHORS
%doc mythplugins/mythweather/COPYING
%doc mythplugins/mythweather/README*
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
%doc mythplugins/mythzoneminder/README
%doc mythplugins/mythzoneminder/COPYING
%doc mythplugins/mythzoneminder/AUTHORS
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

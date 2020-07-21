#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qt5ct
Version  : 1.1
Release  : 4
URL      : https://sourceforge.net/projects/qt5ct/files/qt5ct-1.1.tar.bz2
Source0  : https://sourceforge.net/projects/qt5ct/files/qt5ct-1.1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: qt5ct-bin = %{version}-%{release}
Requires: qt5ct-data = %{version}-%{release}
Requires: qt5ct-lib = %{version}-%{release}
Requires: qt5ct-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Concurrent)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : qtbase-staticdev
BuildRequires : qttools-dev

%description
qt5ct - Qt5 Configuration Tool
This program allows users to configure Qt5 settings (theme, font, icons, etc.)
under DE/WM without Qt integration.

%package bin
Summary: bin components for the qt5ct package.
Group: Binaries
Requires: qt5ct-data = %{version}-%{release}
Requires: qt5ct-license = %{version}-%{release}

%description bin
bin components for the qt5ct package.


%package data
Summary: data components for the qt5ct package.
Group: Data

%description data
data components for the qt5ct package.


%package lib
Summary: lib components for the qt5ct package.
Group: Libraries
Requires: qt5ct-data = %{version}-%{release}
Requires: qt5ct-license = %{version}-%{release}

%description lib
lib components for the qt5ct package.


%package license
Summary: license components for the qt5ct package.
Group: Default

%description license
license components for the qt5ct package.


%prep
%setup -q -n qt5ct-1.1
cd %{_builddir}/qt5ct-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake -config ltcg -config fat-static-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1595348192
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt5ct
cp %{_builddir}/qt5ct-1.1/COPYING %{buildroot}/usr/share/package-licenses/qt5ct/bb1748d3a8313c2bba3f5d0530634f092433753b
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/qt5ct

%files data
%defattr(-,root,root,-)
/usr/share/applications/qt5ct.desktop
/usr/share/qt5ct/colors/airy.conf
/usr/share/qt5ct/colors/darker.conf
/usr/share/qt5ct/colors/dusk.conf
/usr/share/qt5ct/colors/ia_ora.conf
/usr/share/qt5ct/colors/sand.conf
/usr/share/qt5ct/colors/simple.conf
/usr/share/qt5ct/colors/waves.conf
/usr/share/qt5ct/qss/fusion-fixes.qss
/usr/share/qt5ct/qss/scrollbar-simple.qss
/usr/share/qt5ct/qss/sliders-simple.qss
/usr/share/qt5ct/qss/tooltip-simple.qss
/usr/share/qt5ct/qss/traynotification-simple.qss

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/platformthemes/libqt5ct.so
/usr/lib64/qt5/plugins/styles/libqt5ct-style.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt5ct/bb1748d3a8313c2bba3f5d0530634f092433753b

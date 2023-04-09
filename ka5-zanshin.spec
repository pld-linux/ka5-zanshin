#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.3
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		zanshin
Summary:	A Getting Things Done application
Name:		ka5-%{kaname}
Version:	22.12.3
Release:	3
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2790c831c8f42586ec66404157f3b3f5
URL:		http://www.kde.org/
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	kf5-ki18n-devel >= 5.93.0
BuildRequires:	kf5-krunner-devel >= 5.93.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.93.0
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5PrintSupport >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Getting Things Done application which aims at getting your mind like
water. Zanshin is a state of awareness, of relaxed alertness, in
Japanese martial arts. A literal translation of zanshin is "remaining
mind". ([Extract from
Wikipedia](https://en.wikipedia.org/wiki/Zanshin))

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%doc AUTHORS HACKING TODO
%attr(755,root,root) %{_bindir}/zanshin
%attr(755,root,root) %{_bindir}/zanshin-migrator
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_zanshin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/zanshin_part.so
%{_desktopdir}/org.kde.zanshin.desktop
%{_iconsdir}/hicolor/128x128/apps/zanshin.png
%{_iconsdir}/hicolor/256x256/apps/zanshin.png
%{_iconsdir}/hicolor/48x48/apps/zanshin.png
%{_iconsdir}/hicolor/64x64/apps/zanshin.png
%{_iconsdir}/hicolor/scalable/apps/zanshin.svgz
%{_datadir}/kservices5/plasma-runner-zanshin.desktop
%{_datadir}/kservices5/zanshin_part.desktop
%{_datadir}/kxmlgui5/zanshin
%{_datadir}/metainfo/org.kde.zanshin.metainfo.xml
%{_libdir}/qt5/plugins/pim5/kontact/kontact_zanshinplugin.so

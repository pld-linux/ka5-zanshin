#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		zanshin
Summary:	A Getting Things Done application
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b30b593889842982d764b9a18090783c
URL:		http://www.kde.org/
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	kf6-ki18n-devel >= 5.93.0
BuildRequires:	kf6-krunner-devel >= 5.93.0
BuildRequires:	kf6-kwindowsystem-devel >= 5.93.0
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	Qt6Core >= %{qtver}
Requires:	Qt6DBus >= %{qtver}
Requires:	Qt6PrintSupport >= %{qtver}
Requires:	Qt6Widgets >= %{qtver}
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
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
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
%attr(755,root,root) %{_libdir}/qt6/plugins/zanshin_part.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/org.kde.zanshin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kontact/kontact_zanshinplugin.so
%{_desktopdir}/org.kde.zanshin.desktop
%{_iconsdir}/hicolor/*x*/apps/zanshin.png
%{_iconsdir}/hicolor/scalable/apps/zanshin.svgz
%{_datadir}/metainfo/org.kde.zanshin.metainfo.xml

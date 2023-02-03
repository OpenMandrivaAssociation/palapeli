%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		palapeli
Version:	22.12.2
Release:	1
Epoch:		1
Summary:	Jigsaw puzzle game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/palapeli/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	cmake(KF5Archive) cmake(KF5Completion) cmake(KF5Config) cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons) cmake(KF5Crash) cmake(KF5I18n) cmake(KF5ItemViews)
BuildRequires:	cmake(KF5KIO) cmake(KF5Notifications) cmake(KF5Service) cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui) cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5Svg) cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	shared-mime-info

%description
Palapeli is a jigsaw puzzle game. Unlike other games in that genre, you are not
limited to aligning pieces on imaginary grids. The pieces are freely moveable.
Also, Palapeli features real persistency, i.e. everything you do is saved on
your disk immediately.

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/palapeli.categories
%{_sysconfdir}/xdg/palapeli-collectionrc
%{_bindir}/palapeli
%{_datadir}/applications/org.kde.palapeli.desktop
%{_libdir}/qt5/plugins/kf5/thumbcreator/palathumbcreator.so
%{_datadir}/kio/servicemenus/palapeli_servicemenu.desktop
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/palapeli
%{_iconsdir}/hicolor/*/*/*palapeli*
%{_datadir}/mime/packages/palapeli-mimetypes.xml
%{_datadir}/knotifications5/palapeli.notifyrc
%{_libdir}/qt5/plugins/palapelislicers/palapeli_goldbergslicer.so
%{_libdir}/qt5/plugins/palapelislicers/palapeli_jigsawslicer.so
%{_libdir}/qt5/plugins/palapelislicers/palapeli_rectslicer.so


#------------------------------------------------------------------------------

%define pala_major 0
%define libpala %mklibname pala %{pala_major}

%package -n %{libpala}
Summary:	Palapeli shared library
Group:		System/Libraries

%description -n %{libpala}
Palapeli shared library.

%files -n %{libpala}
%{_libdir}/libpala.so.%{pala_major}*

#------------------------------------------------------------------------------

%package devel
Summary:	Development files for Palapeli
Group:		Development/KDE and Qt
Requires:	%{libpala} = %{EVRD}
Conflicts:	kdegames4-devel < 1:4.9.80

%description devel
This package provides development files for Palapeli.

%files devel                                                                                           
%{_includedir}/Pala                                                                                    
%{_libdir}/libpala.so                                                                                  
%{_libdir}/cmake/Pala

#------------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --with-html

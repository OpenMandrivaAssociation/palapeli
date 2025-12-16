#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		palapeli
Version:	25.12.0
Release:	%{?git:0.%{git}.}1
Summary:	Jigsaw puzzle game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://www.kde.org/applications/games/palapeli/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/palapeli/-/archive/%{gitbranch}/palapeli-%{gitbranchd}.tar.bz2#/palapeli-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/palapeli-%{version}.tar.xz
%endif
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	cmake(KF6Archive) cmake(KF6Completion) cmake(KF6Config) cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons) cmake(KF6Crash) cmake(KF6I18n) cmake(KF6ItemViews)
BuildRequires:	cmake(KF6KIO) cmake(KF6Notifications) cmake(KF6Service) cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui) cmake(Qt6Core) cmake(Qt6Gui) cmake(Qt6Svg) cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	shared-mime-info

%rename plasma6-palapeli

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Palapeli is a jigsaw puzzle game. Unlike other games in that genre, you are not
limited to aligning pieces on imaginary grids. The pieces are freely moveable.
Also, Palapeli features real persistency, i.e. everything you do is saved on
your disk immediately.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/palapeli.renamecategories
%{_datadir}/qlogging-categories6/palapeli.categories
%{_sysconfdir}/xdg/palapeli-collectionrc
%{_bindir}/palapeli
%{_datadir}/applications/org.kde.palapeli.desktop
%{_libdir}/qt6/plugins/kf6/thumbcreator/palathumbcreator.so
%{_datadir}/kio/servicemenus/palapeli_servicemenu.desktop
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/palapeli
%{_iconsdir}/hicolor/*/*/*palapeli*
%{_datadir}/mime/packages/palapeli-mimetypes.xml
%{_datadir}/knotifications6/palapeli.notifyrc
%{_libdir}/qt6/plugins/palapelislicers/palapeli_goldbergslicer.so
%{_libdir}/qt6/plugins/palapelislicers/palapeli_jigsawslicer.so
%{_libdir}/qt6/plugins/palapelislicers/palapeli_rectslicer.so


#------------------------------------------------------------------------------

%define pala_major 0
%define libpala %mklibname pala

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
%rename plasma6-palapeli-devel

%description devel
This package provides development files for Palapeli.

%files devel                                                                                           
%{_includedir}/Pala                                                                                    
%{_libdir}/libpala.so                                                                                  
%{_libdir}/cmake/Pala

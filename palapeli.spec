Name:		palapeli
Version:	4.11.1
Release:	1
Epoch:		1
Summary:	Jigsaw puzzle game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/palapeli/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
Palapeli is a jigsaw puzzle game. Unlike other games in that genre, you
are not limited to aligning pieces on imaginary grids. The pieces are
freely moveable. Also, Palapeli features real persistency, i.e. everything
you do is saved on your disk immediately.

%files
%{_kde_bindir}/palapeli
%{_kde_libdir}/kde4/palapeli_jigsawslicer.so
%{_kde_libdir}/kde4/palapeli_rectslicer.so
%{_kde_libdir}/kde4/palathumbcreator.so
%{_kde_libdir}/kde4/palapeli_goldbergslicer.so
%{_kde_applicationsdir}/palapeli.desktop
%{_kde_appsdir}/palapeli
%{_kde_iconsdir}/hicolor/*/*/*palapeli*
%{_kde_services}/ServiceMenus/palapeli_servicemenu.desktop
%{_kde_services}/palapeli_goldbergslicer.desktop
%{_kde_services}/palapeli_jigsawslicer.desktop
%{_kde_services}/palapeli_rectslicer.desktop
%{_kde_services}/palathumbcreator.desktop
%{_kde_servicetypes}/libpala-slicerplugin.desktop
%{_kde_datadir}/mime/packages/palapeli-mimetypes.xml
%{_kde_configdir}/palapeli-collectionrc
%{_kde_docdir}/HTML/en/palapeli

#------------------------------------------------------------------------------

%define pala_major 0
%define libpala %mklibname pala %{pala_major}

%package -n %{libpala}
Summary:	Palapeli shared library
Group:		System/Libraries

%description -n %{libpala}
Palapeli shared library.

%files -n %{libpala}
%{_kde_libdir}/libpala.so.%{pala_major}*

#------------------------------------------------------------------------------

%package devel
Summary:	Development files for Palapeli
Group:		Development/KDE and Qt
Requires:	%{libpala} = %{EVRD}
Conflicts:	kdegames4-devel < 1:4.9.80

%description devel
This package provides development files for Palapeli.

%files devel
%{_kde_includedir}/Pala
%{_kde_includedir}/libpala
%{_kde_libdir}/libpala.so
# cmake files
%{_kde_libdir}/libpala

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

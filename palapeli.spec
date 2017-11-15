%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		palapeli
Version:	17.08.3
Release:	1
Epoch:		1
Summary:	Jigsaw puzzle game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/palapeli/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	kdelibs-devel
BuildRequires:	cmake(KDEGames)

%description
Palapeli is a jigsaw puzzle game. Unlike other games in that genre, you
are not limited to aligning pieces on imaginary grids. The pieces are
freely moveable. Also, Palapeli features real persistency, i.e. everything
you do is saved on your disk immediately.

%files -f %{name}.lang
%{_bindir}/palapeli                                                                                    
%{_libdir}/kde4/palapeli_jigsawslicer.so                                                               
%{_libdir}/kde4/palapeli_rectslicer.so                                                                 
%{_libdir}/kde4/palathumbcreator.so                                                                    
%{_libdir}/kde4/palapeli_goldbergslicer.so                                                             
%{_datadir}/applications/kde4/org.kde.palapeli.desktop                                                         
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/apps/palapeli                                                                              
%{_iconsdir}/hicolor/*/*/*palapeli*                                                                    
%{_datadir}/kde4/services/ServiceMenus/palapeli_servicemenu.desktop                                    
%{_datadir}/kde4/services/palapeli_goldbergslicer.desktop                                              
%{_datadir}/kde4/services/palapeli_jigsawslicer.desktop                                                
%{_datadir}/kde4/services/palapeli_rectslicer.desktop                                                  
%{_datadir}/kde4/services/palathumbcreator.desktop                                                     
%{_datadir}/kde4/servicetypes/libpala-slicerplugin.desktop                                             
%{_datadir}/mime/packages/palapeli-mimetypes.xml                                                       
%{_datadir}/config/palapeli-collectionrc                                                               

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
%{_includedir}/libpala                                                                                 
%{_libdir}/libpala.so                                                                                  
# cmake files                                                                                          
%{_libdir}/libpala  

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
%find_lang %{name} --with-html

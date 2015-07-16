Name:		palapeli
Version:	15.04.3
Release:	1
Epoch:		1
Summary:	Jigsaw puzzle game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/palapeli/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	kdelibs-devel
BuildRequires:	cmake(KDEGames)

%description
Palapeli is a jigsaw puzzle game. Unlike other games in that genre, you
are not limited to aligning pieces on imaginary grids. The pieces are
freely moveable. Also, Palapeli features real persistency, i.e. everything
you do is saved on your disk immediately.

%files
%{_bindir}/palapeli                                                                                    
%{_libdir}/kde4/palapeli_jigsawslicer.so                                                               
%{_libdir}/kde4/palapeli_rectslicer.so                                                                 
%{_libdir}/kde4/palathumbcreator.so                                                                    
%{_libdir}/kde4/palapeli_goldbergslicer.so                                                             
%{_datadir}/applications/kde4/palapeli.desktop                                                         
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
%doc %{_docdir}/HTML/en/palapeli   

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
%cmake_kde4
%make

%install
%makeinstall_std -C build


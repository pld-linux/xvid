
%define snap 20020728

Summary:	GPLed reimplementation of OpenDivX video codec
Summary(pl):	Reimplementacja kodeka wideo OpenDivX na licencji GPL
Name:		xvid
Version:	0.%{snap}
Release:	5
License:	GPL
Group:		Libraries
Source0:	http://www.xvid.org/snapshots/%{name}_snapshot_%{snap}.tar.gz
URL:		http://www.xvid.org/
BuildRequires:	nasm
ExclusiveArch:	%{ix86} ppc sparc sparc64 sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPLed reimplementation of OpenDivX video codec. You can play OpenDivX
and DivX4 videos with it.

%description -l pl
Reimplementacja kodeka wideo OpenDivX na licencji GPL. Za pomoc± tej
biblioteki mo¿esz odtwarzaæ pliki zapisane w standardzie OpenDivX i
DivX4.

%package devel
Summary:	Development files of XviD video codec
Summary(pl):	Pliki programistyczne dla kodeka wideo XviD
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files of XviD video codec.

%description devel -l pl
Pliki programistyczne dla kodeka wideo XviD.

%package static
Summary:	Static XviD video codec library
Summary(pl):	Statyczna biblioteka kodeka wideo XviD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static XviD video codec library.

%description static -l pl
Statyczna biblioteka kodeka wideo XviD.

%prep
%setup  -q -n %{name}_%{snap}

%build
cd xvidcore/build/generic
%{__make} -f \
%ifarch %{ix86}
    Makefile.linux \
%endif
%ifarch ppc
    Makefile.linuxppc \
%endif
%ifarch sparc sparc64 sparcv9        
    Makefile.sparc \
%endif
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall \
%ifarch %{ix86}	
	-DARCH_X86 \
%endif
%ifarch ppc
	-DARCH_PPC -DARCH_IS_BIG_ENDIAN \
%endif
%ifarch sparc sparc64 sparcv9
	-DARCH_IS_BIG_ENDIAN -DARCH_SPARC \
%endif			 
	-DLINUX -ffast-math -fstrict-aliasing %{!?debug:-funroll-loops -fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/xvid}

cd xvidcore/build/generic
install *.so $RPM_BUILD_ROOT%{_libdir}
install *.a $RPM_BUILD_ROOT%{_libdir}

cd ../../../xvidcore/src

install xvid.h divx4.h $RPM_BUILD_ROOT%{_includedir}/xvid
ln -s divx4.h $RPM_BUILD_ROOT%{_includedir}/xvid/decore.h
ln -s divx4.h $RPM_BUILD_ROOT%{_includedir}/xvid/encore2.h

cd ../..

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc xvidcore/{a,c,t}*.txt xvidcore/doc/README
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%doc xvidcore/doc/*.txt
%dir %{_includedir}/xvid
%{_includedir}/xvid/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

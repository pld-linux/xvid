
Summary:	ISO MPEG-4 compliant video codec
Summary(pl):	Implementacja kodeka wideo zgodnego ze standardem ISO MPEG-4
Name:		xvid
Version:	0.9.1
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://files.xvid.org/downloads/xvidcore-%{version}.tar.bz2
URL:		http://www.xvid.org/
BuildRequires:	nasm
ExclusiveArch:	%{ix86} ppc sparc sparc64 sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISO MPEG-4 compliant video codec. You can play OpenDivX and DivX4 videos
with it, too.

%description -l pl
Implementacja kodeka wideo zgodnego ze standardem ISO MPEG-4. Za pomoc± tej
biblioteki mo¿esz tak¿e odtwarzaæ pliki zapisane w standardzie OpenDivX
i DivX4.

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
%setup  -q -n xvidcore-%{version}

%build
cd build/generic
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cd build/generic
%{__make} install libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {a,c,t}*.txt doc/README
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt
%{_includedir}/xvid.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

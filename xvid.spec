
%define snap 20020412

Summary:	GPLed reimplementation of OpenDivX video codec
Summary(pl):	Reimplementacja kodeka wideo OpenDivX na licencji GPL
Name:		xvid
Version:	0.%{snap}
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.xvid.org/%{name}_snapshot_%{snap}.tar.gz
URL:		http://www.xvid.org/
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
%requires_eq	xvid

%description devel
Development files of XviD video codec.

%description devel -l pl
Pliki programistyczne dla kodeka wideo XviD.

%prep
%setup  -q -n %{name}_%{snap}

%build
cd xvidcore/build/generic
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cd xvidcore/build/generic
install *.so $RPM_BUILD_ROOT%{_libdir}

cd ../../../xvidcore/src

install xvid.h $RPM_BUILD_ROOT%{_includedir}

cd ../..

gzip -9nf xvidcore/{a,c,t}*.txt xvidcore/doc/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc xvidcore/*.gz vfw/bin/XviD_Options_Explained.pdf
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%doc xvidcore/doc/*.gz
%{_includedir}/*.h


%define beta beta2

Summary:	ISO MPEG-4 compliant video codec
Summary(pl):	Implementacja kodeka wideo zgodnego ze standardem ISO MPEG-4
Name:		xvid
Version:	1.0.0
Release:	0.%{beta}.1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://files.xvid.org/downloads/xvidcore-%{version}-%{beta}.tar.bz2
# Source0-md5:	b2a94f56844f4c85aebc1e66853f7567
URL:		http://www.xvid.org/
%ifarch %{ix86}
BuildRequires:	nasm >= 0.98.34
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISO MPEG-4 compliant video codec. You can play OpenDivX and DivX4 videos
with it, too.

%description -l pl
Implementacja kodeka wideo zgodnego ze standardem ISO MPEG-4. Za
pomoc� tej biblioteki mo�na tak�e odtwarza� pliki zapisane w
standardzie OpenDivX i DivX4.

%package devel
Summary:	Development files of XviD video codec
Summary(pl):	Pliki programistyczne dla kodeka wideo XviD
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Development files of XviD video codec.

%description devel -l pl
Pliki programistyczne dla kodeka wideo XviD.

%package static
Summary:	Static XviD video codec library
Summary(pl):	Statyczna biblioteka kodeka wideo XviD
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static XviD video codec library.

%description static -l pl
Statyczna biblioteka kodeka wideo XviD.

%prep
%setup  -q -n xvidcore-%{version}-%{beta}

%build
cd build/generic
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cd build/generic
%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}
ln -sf libxvidcore.so.*.* $RPM_BUILD_ROOT%{_libdir}/libxvidcore.so
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

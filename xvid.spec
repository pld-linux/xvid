Summary:	ISO MPEG-4 compliant video codec
Summary(pl):	Implementacja kodeka wideo zgodnego ze standardem ISO MPEG-4
Name:		xvid
Version:	1.0.0
%define beta	rc3
Release:	0.%{beta}.2
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://files.xvid.org/downloads/xvidcore-%{version}-%{beta}.tar.bz2
# Source0-md5:	9b4a9f216ada09c22911e50af2b3cfa3
URL:		http://www.xvid.org/
BuildRequires:	autoconf
BuildRequires:	automake
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
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development files of XviD video codec.

%description devel -l pl
Pliki programistyczne dla kodeka wideo XviD.

%package static
Summary:	Static XviD video codec library
Summary(pl):	Statyczna biblioteka kodeka wideo XviD
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static XviD video codec library.

%description static -l pl
Statyczna biblioteka kodeka wideo XviD.

%prep
%setup -q -n xvidcore-%{version}-%{beta}

%build
cd build/generic
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

%{__make} -C build/generic install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libxvidcore.so.*.* libxvidcore.so

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

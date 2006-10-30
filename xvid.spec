# TODO
# - rename to xvidcore like the rest of the world names it
Summary:	ISO MPEG-4 compliant video codec
Summary(pl):	Implementacja kodeka wideo zgodnego ze standardem ISO MPEG-4
Name:		xvid
Version:	1.1.1
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://downloads.xvid.org/downloads/xvidcore-%{version}.tar.bz2
# Source0-md5:	76046c3aebce6ae13c93b837763f1e35
Patch0:		%{name}-fix.patch
URL:		http://www.xvid.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%ifarch %{ix86}
BuildRequires:	nasm >= 0.98.34
%endif
Provides:	xvidcore = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISO MPEG-4 compliant video codec. You can play OpenDivX and DivX4 videos
with it, too.

%description -l pl
Implementacja kodeka wideo zgodnego ze standardem ISO MPEG-4. Za
pomoc± tej biblioteki mo¿na tak¿e odtwarzaæ pliki zapisane w
standardzie OpenDivX i DivX4.

%package devel
Summary:	Development files of XviD video codec
Summary(pl):	Pliki programistyczne dla kodeka wideo XviD
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xvidcore-devel = %{epoch}:%{version}-%{release}

%description devel
Development files of XviD video codec.

%description devel -l pl
Pliki programistyczne dla kodeka wideo XviD.

%package static
Summary:	Static XviD video codec library
Summary(pl):	Statyczna biblioteka kodeka wideo XviD
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	xvidcore-static = %{epoch}:%{version}-%{release}

%description static
Static XviD video codec library.

%description static -l pl
Statyczna biblioteka kodeka wideo XviD.

%prep
%setup -q -n %{name}core-%{version}
%patch0 -p1

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

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/README
%attr(755,root,root) %{_libdir}/libxvidcore.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxvidcore.so
%{_includedir}/xvid.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libxvidcore.a

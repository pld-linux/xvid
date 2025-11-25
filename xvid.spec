# TODO
# - rename to xvidcore like the rest of the world names it
Summary:	ISO MPEG-4 compliant video codec
Summary(pl.UTF-8):	Implementacja kodeka wideo zgodnego ze standardem ISO MPEG-4
Name:		xvid
Version:	1.3.7
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Libraries
# Source0Download: https://labs.xvid.com/source/
Source0:	https://downloads.xvid.com/downloads/%{name}core-%{version}.tar.bz2
# Source0-md5:	81a45b0ce8c4376e35faa788aa8199f3
Patch0:		x32.patch
URL:		https://www.xvid.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%ifarch %{ix86} %{x8664} x32
# or nasm >= 2.0
BuildRequires:	yasm >= 1
%endif
Provides:	xvidcore = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-Wl,-z,noexecstack

%description
ISO MPEG-4 compliant video codec. You can play OpenDivX and DivX4
videos with it, too.

%description -l pl.UTF-8
Implementacja kodeka wideo zgodnego ze standardem ISO MPEG-4. Za
pomocą tej biblioteki można także odtwarzać pliki zapisane w
standardzie OpenDivX i DivX4.

%package devel
Summary:	Development files of XviD video codec
Summary(pl.UTF-8):	Pliki programistyczne dla kodeka wideo XviD
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xvidcore-devel = %{epoch}:%{version}-%{release}

%description devel
Development files of XviD video codec.

%description devel -l pl.UTF-8
Pliki programistyczne dla kodeka wideo XviD.

%package static
Summary:	Static XviD video codec library
Summary(pl.UTF-8):	Statyczna biblioteka kodeka wideo XviD
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	xvidcore-static = %{epoch}:%{version}-%{release}

%description static
Static XviD video codec library.

%description static -l pl.UTF-8
Statyczna biblioteka kodeka wideo XviD.

%prep
%setup -q -n %{name}core
%patch -P0 -p1

%build
cd build/generic
sed -i -e 's#@$(AS)#$(AS)#g' Makefile
sed -i -e 's#@$(CC)#$(CC)#g' Makefile
sed -i -e 's#@cd#cd#g' Makefile
cp -f /usr/share/automake/config.sub .
export CFLAGS="%{rpmcflags} -std=gnu11"
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
/sbin/ldconfig -n .

chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/README
%attr(755,root,root) %{_libdir}/libxvidcore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libxvidcore.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxvidcore.so
%{_includedir}/xvid.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libxvidcore.a

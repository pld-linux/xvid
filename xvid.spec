
#
# todo:
# 1. descriptions and summaries
#

%define snap 20020404

Summary:	XVid
Name:		xvid
Version:	0.%{snap}
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://www.xvid.org/%{name}_snapshot_%{snap}.tar.gz
URL:		http://www.xvid.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xvid

%description -l pl
Xvid

%package devel
Summary:	Xvid devel
Group:		Libraries/Development

%description devel
aa

%description devel -l pl
aa

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

gzip -9nf xvidcore/{a,c,t}*.txt

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
%{_includedir}/*.h

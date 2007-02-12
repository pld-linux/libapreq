Summary:	Generic Apache Request Library
Summary(pl.UTF-8):   Standardowa biblioteka zapytań Apache
Summary(pt_BR.UTF-8):   Biblioteca de requisiçoes do Apache
Name:		libapreq
Version:	1.33
Release:	1
License:	Apache Group
Group:		Libraries
Source0:	http://www.apache.org/dist/httpd/libapreq/%{name}-%{version}.tar.gz
# Source0-md5:	8ac4296342e637c6faa731dcf9087685
URL:		http://httpd.apache.org/apreq/
BuildRequires:	apache1-devel >= 1.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# remember about perl-libapreq.spec when incrementing version

%description
This package contains modules for manipulating client request data via
the Apache API with C.

%description -l pl.UTF-8
Ten pakiet zawiera moduły, służące do manipulowania danymi z zapytań
klientów HTTP danymi poprzez API Apache przy użyciu C.

%description -l pt_BR.UTF-8
Este pacote contém módulos para a manipulação de requisições de
cliente através da API do Apache em C.

%package devel
Summary:	libapreq header files
Summary(pl.UTF-8):   Pliki nagłówkowe libapreq
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	apache1-devel >= 1.3

%description devel
libapreq header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libapreq.

%package static
Summary:	libapreq static library
Summary(pl.UTF-8):   Statyczna biblioteka libapreq
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libapreq library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libapreq.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-apache-includes=%{_includedir}/apache1

%{__make}

/usr/bin/pod2man --section=3 libapreq.pod > libapreq.3

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D libapreq.3 $RPM_BUILD_ROOT%{_mandir}/man3/libapreq.3

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/c/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes CREDITS README ToDo
%attr(755,root,root) %{_libdir}/libapreq.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libapreq.so
%{_libdir}/libapreq.la
%{_includedir}/libapreq
%{_mandir}/man3/libapreq.3*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libapreq.a

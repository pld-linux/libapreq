Summary:	Generic Apache Request Library
Summary(pl):	Standardowa biblioteka zapytañ Apache
Summary(pt_BR):	Biblioteca de requisiçoes do Apache
Name:		libapreq
Version:	1.1
Release:	1
License:	Apache Group
Group:		Libraries
Source0:	http://www.apache.org/dist/httpd/%{name}/%{name}-%{version}.tar.gz
URL:		http://httpd.apache.org/apreq/
BuildRequires:	apache-mod_perl >= 1.26-5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	/usr/bin/pod2man
Requires:	apache-mod_perl >= 1.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# remember about perl-libapreq.spec when incrementing version

%description
This package contains modules for manipulating client request data via
the Apache API with C.

%description -l pl
Ten pakiet zawiera modu³y, s³u¿±ce do manipulowania danymi z zapytañ
klientów HTTP danymi poprzez API Apache przy u¿yciu C.

%description -l pt_BR
Este pacote contém módulos para a manipulação de requisições de
cliente através da API do Apache em C.

%package devel
Summary:	libapreq header files
Summary(pl):	Pliki nag³ówkowe libapreq
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
libapreq header files.

%description devel -l pl
Pliki nag³ówkowe biblioteki libapreq.

%package static
Summary:	libapreq static library
Summary(pl):	Statyczna biblioteka libapreq
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libapreq library.

%description static -l pl
Statyczna wersja biblioteki libapreq.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-apache-includes=%{_includedir}/apache

%{__make}

/usr/bin/pod2man --section=3 libapreq.pod > libapreq.3

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/libapreq
%{_mandir}/man3/libapreq.3*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

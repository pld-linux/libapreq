%define pnam	libapreq
Summary:	Generic Apache Request Library
Summary(pl):	Standardowa biblioteka zapyta� Apache
Summary(pt_BR):	Biblioteca de requisi�oes do Apache
Name:		%{pnam}
Version:	1.0
Release:	1
License:	Apache Group
Group:		Libraries
Source0:	http://www.apache.org/dist/httpd/%{pdir}/%{pnam}-%{version}.tar.gz
URL:		http://httpd.apache.org/apreq/
BuildRequires:	/usr/bin/pod2man
BuildRequires:	apache-mod_perl >= 1.26-5
Requires:	apache-mod_perl >= 1.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# remember about perl-libapreq.spec when incrementing version

%description
This package contains modules for manipulating client request data via
the Apache API with C.

%description -l pl
Ten pakiet zawiera modu�y, s�u��ce do manipulowania z zapyta� klient�w
HTTP danymi poprzez API Apache przy u�yciu C.

%description -l pt_BR
Este pacote cont�m m�dulos para a manipula��o de requisi��es de
cliente atrav�s da API do Apache em C.


%prep
%setup -q -n %{pnam}-%{version}

%build
./configure \
	--prefix=%{_prefix} \
	--enable-shared=yes \
	--enable-static=no  \
	--with-apache-includes=%{_includedir}/apache
%{__make} OPTIMIZE="%{rpmcflags}"
/usr/bin/pod2man libapreq.pod > libapreq.3pm

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -D libapreq.3pm $RPM_BUILD_ROOT%{_mandir}/man3/libapreq.3pm

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/c/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr (755,root,root) %{_libdir}/*.so*
%{_libdir}/*.la
%{_includedir}/libapreq

%doc Changes CREDITS README ToDo
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/libapreq*

%include	/usr/lib/rpm/macros.perl
%define pnam	libapreq
Summary:	Generic Apache Request Library
Summary(pl):	Standardowa biblioteka zapytañ Apache
Summary(pt_BR):	Biblioteca de requisiçoes do Apache
Name:		%{pnam}
Version:	1.0
Release:	0
License:	Apache Group
Group:		Libraries
Source0:	http://www.apache.org/dist/httpd/%{pnam}-%{version}.tar.gz
URL:		http://httpd.apache.org/apreq/
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	apache-mod_perl >= 1.26-5
Requires:	apache-mod_perl >= 1.26
Provides:	perl(Apache::Request) = 1.0 perl(Apache::Cookie) = 1.0
Obsoletes:	perl-libapreq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains modules for manipulating client request data via
the Apache API with Perl and C.

%description -l pl
Ten pakiet zawiera modu³y, s³u¿±ce do manipulowania z zapytañ klientów
HTTP danymi poprzez API Apache przy u¿yciu Perla i C.

%description -l pt_BR
Este pacote contém módulos para a manipulação de requisições de
cliente através da API do Apache em Perl e C.

# Motto: whatever you'll do, this spec will suck.

%prep
%setup -q -n %{pnam}-%{version}
rm -rf %{_builddir}/%{pnam}-%{version}-c
cp -a %{_builddir}/%{pnam}-%{version} %{_builddir}/%{pnam}-%{version}-c

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

cd %{_builddir}/%{pnam}-%{version}-c
./configure \
	--prefix=%{_prefix} \
	--enable-shared=yes \
	--enable-static=no  \
	--with-apache-includes=%{_includedir}/apache
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install \
	-C %{_builddir}/%{pnam}-%{version}-c \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf %{_builddir}/%{pnam}-%{version}-c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

# perl files
%{perl_sitearch}/Apache/*.pm

%dir %{perl_sitearch}/auto/Apache/Cookie
%{perl_sitearch}/auto/Apache/Cookie/Cookie.bs
%attr(755,root,root) %{perl_sitearch}/auto/Apache/Cookie/Cookie.so

%dir %{perl_sitearch}/auto/Apache/Request
%{perl_sitearch}/auto/Apache/Request/Request.bs
%attr(755,root,root) %{perl_sitearch}/auto/Apache/Request/Request.so

%dir %{perl_sitearch}/auto/libapreq
%{perl_sitearch}/auto/libapreq/extralibs.ld
%attr(755,root,root) %{perl_sitearch}/auto/libapreq/libapreq.a

%{perl_sitearch}/auto/libapreq/include

# C files
%{_libdir}/*.so*
%{_libdir}/*.la
%{_includedir}/libapreq

# both
%doc Changes CREDITS INSTALL LICENSE README ToDo
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*

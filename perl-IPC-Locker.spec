#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	Locker
Summary:	IPC::Locker - distributed lock handler
Summary(pl.UTF-8):	IPC::Locker - obsługa rozproszonych blokad
Name:		perl-IPC-Locker
Version:	1.489
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IPC/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8c39b130aacc8387d6edd5d92b9febc
URL:		http://search.cpan.org/dist/IPC-Locker/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-perldoc
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PC::Locker will query a remote server to obtain a lock. This is useful
for distributed utilities which run on many machines, and cannot use
file locks or other such mechanisms due to NFS or lack of common file
systems.

%description -l pl.UTF-8
IPC::Locker zapyta zdalny serwer w celu otrzymania blokady. Jest
użyteczny dla rozproszonych aplikacji, działających na wielu maszynach
i nie mogących używać blokad plikowych (file locks) lub innych tego
typu mechanizmów z powodu stosowania NFS lub braku tej opcji w
popularnych systemach plików.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/IPC/*
%{_mandir}/man[13]/*

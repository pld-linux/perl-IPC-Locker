#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	IPC
%define	pnam	Locker
Summary:	IPC::Locker - Distributed lock handler
Summary(pl):	IPC::Locker - Obs�uga rozproszonych blokad
Name:		perl-IPC-Locker
Version:	1.410
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PC::Locker will query a remote server to obtain a lock.  This is useful
for distributed utilities which run on many machines, and cannot use file
locks or other such mechanisms due to NFS or lack of common file systems.

%description -l pl
IPC::Locker zapyta zdalny serwr w celu otrzymania blokady.  Jest u�yteczny
dla rozproszonych aplikacji, dzia�aj�cych na wielu maszynach i nie mog�cych
u�ywa� blokad plikowych (file locks) lub innych tego typu mechanizm�w z
powodu stosowania NFS lub braku tej opcji w popularnych systemach plik�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*
%{_mandir}/man[13]/*
%{_bindir}/*
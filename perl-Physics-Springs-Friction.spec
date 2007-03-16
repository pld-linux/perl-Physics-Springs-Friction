#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Physics
%define	pnam	Springs-Friction
Summary:	Physics::Springs::Friction - Simulate Dynamics with Springs and Friction
Summary(pl.UTF-8):	Physics::Springs::Friction - symulacja dynamiki ze sprężynami i tarciem
Name:		perl-Physics-Springs-Friction
Version:	1.01
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Physics/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9addede00f2318f7d8301495a207fcd3
URL:		http://search.cpan.org/dist/Physics-Springs-Friction/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Physics-Particles >= 1.00
BuildRequires:	perl-Physics-Springs >= 1.00
BuildRequires:	perl-Sub-Assert
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended as an add-on to the Physics::Springs (from
version 1.00) and Physics::Particles (from version 1.00) modules and
may be used to simulate particle dynamics including spring-like forces
between any two particles you specify and friction-like forces that
are applied to the movement of all particles.

The module extends the API of Physics::Springs by one method. Please
see the documentation to Physics::Springs and Physics::Particles for
more information about the API.

There are several particle properties required by
Physics::Springs::Friction in order to work: These are the x/y/z
coordinates, the vx/vy/vz velocity vector components, and a non-zero
mass 'm'.

%description -l pl.UTF-8
Ten moduł ma być dodatkiem do modułów Physics::Strings (od wersji
1.00) i Physics::Particles (od wersji 1.00) służącym do symulacji
dynamiki cząstek włącznie z siłami typu sprężynowego między dowolnymi
dwiema określonymi cząstkami oraz siłami w rodzaju tarcia wywieranego
przy ruchu wszystkich cząstek.

Ten moduł rozszerza API Physics::Springs o jedną metodę; więcej
informacji o API można znaleźć w modułach Physics::Springs i
Physics::Particles.

Jest kilka właściwości cząstek wymaganych do działania przez
Physics::Springs::Friction - są to: współrzędne x/y/z, składowe
wektora prędkości vx/vy/vz i niezerowa masa m.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Physics/Springs
%{perl_vendorlib}/Physics/Springs/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

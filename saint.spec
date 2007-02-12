Summary:	Security Administrator's Integrated Network Tool
Summary(pl.UTF-8):   Zintegrowane narzędzie sieciowe administratora bezpieczeństwa
Name:		saint
Version:	3.3.3
Release:	1
License:	Free for non-commercial use
Group:		Networking/Utilities
#Source0:	http://www.saintcorporation.com/saint/downloads/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	3e79987721595e03d2662066a63c2296
Source1:	%{name}.sh
URL:		http://www.saintcorporation.com/products/saint_engine.html
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SAINT (Security Administrator's Integrated Network Tool) is a security
assesment tool based on SATAN. Features include scanning through a
firewall, updated security checks from CERT & CIAC bulletins, 4 levels
of severity (red, yellow, brown, & green) and a feature rich HTML
interface.

%description -l pl.UTF-8
SAINT jest narzędziem wspomagającym kontrolę stanu bezpieczeństwa
wzorowanym na SATANie. Umożliwia skanowanie przez zapory ogniowe,
testy bezpieczeństwa oparte na biuletynach CERT i CIAC, podział
zagrożeń na 4 grupy oraz obsługę przez rozbudowany interfejs HTML.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name},%{_mandir}/man1,%{_sbindir}}

cp -a saint bin config html perl perllib rules scripts \
	$RPM_BUILD_ROOT%{_libdir}/%{name}

install saint.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/config
%{_libdir}/%{name}/html
%{_libdir}/%{name}/perl
%{_libdir}/%{name}/perllib
%{_libdir}/%{name}/rules
%attr(755,root,root) %{_libdir}/%{name}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/bin
%attr(755,root,root) %{_libdir}/%{name}/scripts
%attr(755,root,root) %{_sbindir}/%{name}
%{_mandir}/man1/*

Summary:	Security Administrator's Integrated Network Tool
Name:		saint
Version:	3.3.3
Release:	1
License:	Free for non-commercial use
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	http://www.wwdsi.com/saint/downloads/%{name}-%{version}.tar.gz
Source1:	%{name}.sh
URL:		http://www.wwdsi.com/saint/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SAINT (Security Administrator's Integrated Network Tool) is a security
assesment tool based on SATAN. Features include scanning through a
firewall, updated security checks from CERT & CIAC bulletins, 4 levels
of severity (red, yellow, brown, & green) and a feature rich HTML
interface.

%description -l pl
SAINT jest narzêdziem wspomagaj±cym kontrolê stanu bezpieczeñstwa
wzorowanym na SATANie. Umo¿liwia skanowanie przez zapory ogniowe,
testy bezpieczeñstwa oparte na biuletynach CERT i CIAC, podzia³
zagro¿eñ na 4 grupy oraz obs³ugê przez rozbudowany interfejs HTML.

%prep
%setup -q

%build
autoconf
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name},%{_mandir}/man1,%{_sbindir}}

cp -a {saint,bin,config,html,perl,perllib,rules,scripts} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}
	
cp saint.1 $RPM_BUILD_ROOT%{_mandir}/man1/

cp %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/%{name}/config/*
%{_libdir}/%{name}/html/*
%{_libdir}/%{name}/perl/*
%{_libdir}/%{name}/perllib/*
%{_libdir}/%{name}/rules/*
%attr(755,root,root) %{_libdir}/%{name}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/bin/*
%attr(755,root,root) %{_libdir}/%{name}/scripts/*
%attr(755,root,root) %{_sbindir}/%{name}
%{_mandir}/man1/*

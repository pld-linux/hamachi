# TODO:
# - initscripts ?
#
%define		ver 0.9.9.9
%define		subver 20
Summary:	hamachi - simple VPN
Summary(de.UTF-8):	hamachi - eine einfache VPN
Summary(pl.UTF-8):	hamachi - prosty VPN
Name:		hamachi
Version:	%{ver}_%{subver}
Release:	0.1
Epoch:		0
License:	free, not-distributable
Group:		Networking
Source0:	http://files.hamachi.cc/linux/%{name}-%{ver}-%{subver}-lnx.tar.gz
# Source0-md5:	27e4c926d0aa03de3573c0b7acf032a6
URL:		http://www.hamachi.cc/
BuildRequires:	sed >= 4.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin
%define		_noautostrip	.*hamachi

%description
With Hamachi you can organize two or more computers with an Internet
connection into their own virtual network for direct secure
communication. See README for futher information.

%description -l de.UTF-8
Mit Hamachi kann man zwei oder mehr Rechner mit Internetzugang in ein
eigenes virtueles Netzwerk verbinden um direkt und sicher zu
kommunizieren. Mehr Infos findet man in der README.

%description -l pl.UTF-8
Przy użyciu Hamachi można połączyć dwa lub więcej komputerów z łączem
do Internetu we własną wirtualną sieć w celu bezpośredniej,
bezpiecznej komunikacji. Więcej informacji znajduje się w pliku
README.

%prep
%setup -q -n %{name}-%{ver}-%{subver}-lnx

sed -i 's, [^/ ]*/hamachi , hamachi ,' Makefile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}

%{__make} install \
	HAMACHI_DST=$RPM_BUILD_ROOT%{_bindir} \
	TUNCFG_DST=$RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

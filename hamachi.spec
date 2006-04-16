# TODO:
# - initscripts ?
#
%define		ver 0.9.9.9
%define		subver 17
Summary:	hamachi - simple VPN
Summary(pl):	hamachi - prosty VPN
Name:		hamachi
Version:	%{ver}_%{subver}
Release:	0.1
Epoch:		0
License:	free, not-distributable
Group:		Networking
Source0:	http://files.hamachi.cc/linux/%{name}-%{ver}-%{subver}-lnx.tar.gz
# Source0-md5:	1638f2bf7f812e75fee51c66d1623942
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

%description -l pl
Przy u¿yciu Hamachi mo¿na po³±czyæ dwa lub wiêcej komputerów z ³±czem
do Internetu we w³asn± wirtualn± sieæ w celu bezpo¶redniej,
bezpiecznej komunikacji. Wiêcej informacji znajduje siê w pliku
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

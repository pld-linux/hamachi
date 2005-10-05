#
# TODO:
#   initscripts ?
#
%define		ver 0.9.9.9
%define		subver 3

%define		_noautostrip	.*hamachi

Summary:	hamachi - simple VPN
Summary(pl):	hamachi - prosty VPN
Name:		hamachi
Version:	%{ver}_%{subver}
Release:	0.1
Epoch:		0
License:	free, not-distributable
Group:		Networking
Source0:	http://files.hamachi.cc/linux/%{name}-%{ver}-%{subver}.tar.gz
# NoSource0-md5:	d33566156304f0635659be7d1c48b41a
NoSource:	0
URL:		http://www.hamachi.cc/
BuildRequires:	rpmbuild(macros) >= 1.230
BuildRequires:	sed >= 4.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -n %{name}-%{ver}-%{subver}

%build
sed -i 's, [^/ ]*/hamachi , hamachi ,' Makefile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/sbin}

%{__make} install \
	HAMACHI_DST=$RPM_BUILD_ROOT%{_bindir} \
	TUNCFG_DST=$RPM_BUILD_ROOT/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with initscript}
%post init
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun init
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi
%endif

%files
%defattr(644,root,root,755)
%doc README LICENSE*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /sbin/*

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif

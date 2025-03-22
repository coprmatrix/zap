%define _zapdir  %{_datadir}/zap

Name:           owasp-zap
Version:        2.16.0
Release:        1%{?autorelease}
Summary:        Zed Attack Proxy
Group:          System/Security
Provides:       zap = %{version}
Obsoletes:      zap < %{version}
Obsoletes:      owasp-zap < %{version}
License:        Apache-2.0
URL:            https://www.zaproxy.org/
Source0:        https://github.com/zaproxy/zaproxy/releases/download/v%{version}/ZAP_%{version}_Linux.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-build
BuildArch:      noarch
Requires:       java

%description
The Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding 
vulnerabilities in web applications. It is designed to be used by people with a wide range of 
security experience and as such is ideal for developers and functional testers who are new to 
penetration testing. ZAP provides automated scanners as well as a set of tools that allow you 
to find security vulnerabilities manually. 

%prep
%setup -n zap-%{version}

%build

%install

install -d $RPM_BUILD_ROOT%{_zapdir}
cp -r db lang lib license plugin xml $RPM_BUILD_ROOT%{_zapdir}
cp README $RPM_BUILD_ROOT%{_zapdir}
install -m 644 zap-%{version}.jar $RPM_BUILD_ROOT%{_zapdir}
install -m 755 zap.sh $RPM_BUILD_ROOT%{_zapdir}
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps    
install -m 644 $RPM_SOURCE_DIR/%{name}.png $RPM_BUILD_ROOT/usr/share/pixmaps 
install -d %{buildroot}/usr/share/applications/
install -m 644 $RPM_SOURCE_DIR/%{name}.desktop %{buildroot}/usr/share/applications/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_zapdir}/*
%dir %{_datadir}/applications/
%{_datadir}/applications/%{name}.desktop    
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/zap

%changelog

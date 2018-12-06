# http://github.com/jinzhu/gorm

%global goipath         github.com/jinzhu/gorm
%global commit          82d726bbfd8cefbe2dcdc7f7f0484551c0d40433


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.12%{?dist}
Summary:        ORM library for Golang, aims to be developer friendly
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

#BuildRequires: golang(github.com/denisenkom/go-mssqldb)
#BuildRequires: golang(github.com/erikstmartin/go-testdb)
#BuildRequires: golang(github.com/go-sql-driver/mysql)
#BuildRequires: golang(github.com/jinzhu/now)
#BuildRequires: golang(github.com/lib/pq)
BuildRequires: golang(github.com/lib/pq/hstore)
#BuildRequires: golang(github.com/mattn/go-sqlite3)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
# Deps missing
#%%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license License
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.git82d726b
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.20150721git82d726b
- Autogenerate some parts using the new macros

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git82d726b
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git82d726b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git82d726b
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git82d726b
- First package for Fedora
  resolves: #1270050

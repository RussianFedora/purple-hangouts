%global plugin_name hangouts

%global commit0 2095ac0da92d760cd26fb3258f950ccce9547c86
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global archcommit0 %(c=%{commit0}; echo ${c:0:12})
%global date 20160507

Name: purple-%{plugin_name}
Version: 1.0
Release: 20.%{date}hg%{shortcommit0}%{?dist}
Summary: Hangouts plugin for libpurple

License: GPLv3
URL: https://bitbucket.org/EionRobb/purple-hangouts/
Source0: https://bitbucket.org/EionRobb/purple-hangouts/get/%{commit0}.tar.gz#/purple-hangouts-%{shortcommit0}.tar.gz

%if 0%{?fedora}
Patch0: https://github.com/xvitaly/purple-hangouts/raw/master/fix_build_under_fedora.patch
%endif

BuildRequires: pkgconfig(libprotobuf-c)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(nss)
BuildRequires: gcc

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Hangouts protocol
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: pidgin

%description
Adds support for Hangouts to Pidgin, Adium, Finch and other libpurple
based messengers.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Hangouts protocol inplemented by
hangouts-purple.

%prep
%autosetup -n EionRobb-purple-%{plugin_name}-%{archcommit0} -p1

# fix W: wrong-file-end-of-line-encoding
perl -i -pe 's/\r\n/\n/gs' README.md

# generating empty configure script
echo '#!/bin/bash' > configure
chmod +x configure

%build
%configure
%make_build

%install
# Creating base directories...
mkdir -p %{buildroot}%{_libdir}/purple-2/
mkdir -p %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/{16,22,48}/

# Executing base install from makefile...
%make_install

# Setting correct chmod...
chmod 755 %{buildroot}%{_libdir}/purple-2/lib%{plugin_name}.so

# Installing icons...
install -p hangouts16.png %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/16/%{plugin_name}.png
install -p hangouts22.png %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/22/%{plugin_name}.png
install -p hangouts48.png %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/48/%{plugin_name}.png

%files
%{_libdir}/purple-2/lib%{plugin_name}.so
%license gpl3.txt
%doc README.md

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/%{plugin_name}.png

%changelog
* Sat May 07 2016 V1TSK <vitaly@easycoding.org> - 1.0-20.20160507hg2095ac0
- Updated to latest snapshot.

* Thu May 05 2016 V1TSK <vitaly@easycoding.org> - 1.0-19.20160505hg4cf1d50
- Updated to latest snapshot.

* Wed May 04 2016 V1TSK <vitaly@easycoding.org> - 1.0-18.20160504hge8c30b6
- Updated to latest snapshot.

* Tue May 03 2016 V1TSK <vitaly@easycoding.org> - 1.0-17.20160502hg2631ad2
- Updated to latest snapshot. Added patch for Fedora.

* Tue Apr 26 2016 V1TSK <vitaly@easycoding.org> - 1.0-16.20160426hgac1741f
- Updated to latest snapshot.

* Thu Apr 21 2016 V1TSK <vitaly@easycoding.org> - 1.0-15.20160421hg6f76943
- Updated to latest snapshot.

* Sun Apr 17 2016 V1TSK <vitaly@easycoding.org> - 1.0-14.20160417hg635f50c
- Updated to latest snapshot.

* Fri Apr 15 2016 V1TSK <vitaly@easycoding.org> - 1.0-13.20160413hg92bfbf1
- Updated to latest snapshot.

* Sun Apr 10 2016 V1TSK <vitaly@easycoding.org> - 1.0-12.20160410hga5b0e60
- Updated to latest snapshot.

* Sat Apr 09 2016 V1TSK <vitaly@easycoding.org> - 1.0-11.20160409hg7442ecd
- Updated to latest snapshot.

* Wed Apr 06 2016 V1TSK <vitaly@easycoding.org> - 1.0-10.20160406hgab7c25a
- Added license section. Updated to latest snapshot.

* Tue Apr 05 2016 V1TSK <vitaly@easycoding.org> - 1.0-9.20160405hgbd3b2be
- Fixed SPEC. Updated to latest snapshot.

* Sun Apr 03 2016 V1TSK <vitaly@easycoding.org> - 1.0-8.20160403hg0f3cbbd
- Updated to latest snapshot.

* Fri Apr 01 2016 V1TSK <vitaly@easycoding.org> - 1.0-7.20160401hg8b37dcc
- Updated to latest snapshot.

* Tue Mar 22 2016 V1TSK <vitaly@easycoding.org> - 1.0-6.20160322hg735b7f8
- Updated to latest snapshot.

* Thu Mar 17 2016 V1TSK <vitaly@easycoding.org> - 1.0-5.20160316hgfde2d8a
- Updated to latest snapshot.

* Tue Mar 15 2016 V1TSK <vitaly@easycoding.org> - 1.0-4.20160315hg694bd41
- Updated to latest snapshot.

* Tue Mar 08 2016 V1TSK <vitaly@easycoding.org> - 1.0-3.20160306hgb7ba81f
- Updated to latest snapshot.

* Fri Mar 04 2016 V1TSK <vitaly@easycoding.org> - 1.0-2.20160303hg4789156
- Updated to latest snapshot.

* Mon Feb 29 2016 V1TSK <vitaly@easycoding.org> - 1.0-1.20160227hga2c9af3
- First SPEC version.

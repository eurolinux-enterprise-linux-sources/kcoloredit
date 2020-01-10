
%define iversion 2.0.0

Name:    kcoloredit
Version: 4.4.0
Release: 9%{?dist}
Summary: A color palette Editor

License: GPLv2+
URL:     http://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/extragear/kcoloredit-%{iversion}-kde%{version}.tar.bz2

## upstream patches
# fix FTBFS with the new stricter ld in F13 (#564815): explicitly link libX11
Patch100: kcoloredit-2.0.0-kde4.4.0-ftbfs.patch

BuildRequires:  kdelibs4-devel 
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

%{?_kde4_version:Requires: kdelibs4%{?_isa} >= %{_kde4_version}}

%description
KColorEdit is a palette files editor. It can be used for editing 
color palettes and for color choosing and naming.


%prep
%setup -qn kcoloredit-%{iversion}-kde%{version}
%patch100 -p1 -b .ftbfs


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd


make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --with-kde


%check
desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/kcoloredit.desktop


%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor &> /dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
update-desktop-database -q &> /dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_kde4_bindir}/kcoloredit
%{_kde4_appsdir}/kcoloredit/
%{_kde4_datadir}/applications/kde4/kcoloredit.desktop
%{_kde4_iconsdir}/hicolor/*/*/kcoloredit.*


%changelog
* Tue Jan 28 2014 Daniel Mach <dmach@redhat.com> - 4.4.0-9
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.4.0-8
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Rex Dieter <rdieter@fedoraproject.org> 4.4.0-5
- cleanup spec, fix scriptlets

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.0-2
- fix FTBFS with the new stricter ld in F13 (#564815): explicitly link libX11

* Fri Feb 12 2010 Sebastian Vahl <svahl@fedoraproject.org> - 4.4.0-1
- 4.4.0

* Tue Nov 24 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.3-2
- rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Thu Nov 05 2009 Sebastian Vahl <svahl@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Tue Sep 01 2009 Sebastian Vahl <svahl@fedoraproject.org> - 4.3.1-1
- 4.3.1

* Tue Aug 04 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 10 2009 Sebastian Vahl <fedora@deadbabylon.de> - 4.2.4-1
- 4.2.4

* Tue May 12 2009 Sebastian Vahl <fedora@deadbabylon.de> - 4.2.3-1
- 4.2.3

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Mon Nov 17 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.3-2
- dependency fixes, cosmetics

* Fri Nov 14 2008 Than Ngo <than@redhat.com> 4.1.3-1
- 4.1.3

* Sat Oct 04 2008 Than Ngo <than@redhat.com> 4.1.2-1
- 4.1.2

* Fri Aug 29 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Thu Aug 28 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.1-1
- 4.1 (final)

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta1

* Thu Apr 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- rebuild (again) for the fixed %%{_kde4_buildtype}

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-1
- update to 4.0.3
- rebuild for NDEBUG and _kde4_libexecdir

* Tue Mar 04 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.2-1
- new upstream version: 4.0.2

* Thu Feb 14 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.1-2
- remove reference to KDE 4 in summary

* Fri Feb 08 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.1-1
- new upstream version: 4.0.1

* Fri Jan 25 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.0-1
- Initial version of kde-4.0.0 version

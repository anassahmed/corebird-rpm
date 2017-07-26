Name:           corebird
Version:        1.5.1
Release:        2%{?dist}
Summary:        Native GTK Twitter client

License:        GPLv3+
URL:            http://corebird.baedert.org/
Source0:        https://github.com/baedert/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  gspell-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  rest-devel
BuildRequires:  json-glib-devel
BuildRequires:  libnotify-devel
BuildRequires:  sqlite-devel
BuildRequires:  libsoup-devel
BuildRequires:  vala-devel
BuildRequires:  librsvg2-tools
BuildRequires:  desktop-file-utils

%if 0%{?fedora} < 25
Requires:       gstreamer1-plugins-bad-free%{?_isa}
%else
Requires:       gstreamer1-plugins-bad-free-gtk%{?_isa}
%endif
# For icon directories
Requires:       hicolor-icon-theme

%description
Native GTK Twitter client for the Linux desktop.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%find_lang corebird

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.baedert.corebird.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f corebird.lang
%license COPYING
%{_bindir}/corebird
%{_datadir}/applications/org.baedert.corebird.desktop
%{_datadir}/appdata/org.baedert.corebird.appdata.xml
%{_datadir}/glib-2.0/schemas/org.baedert.corebird.gschema.xml
%{_datadir}/icons/hicolor/*/apps/corebird.png
%{_datadir}/dbus-1/services/org.baedert.corebird.service
%{_mandir}/man1/corebird.1*

%changelog
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.5.1-1
- 1.5.1, stability bug fixes.

* Tue May 02 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.5-1
- 1.5, multiple bug fixes.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Kalev Lember <klember@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Sun Jan 08 2017 Kalev Lember <klember@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Sat Jan 07 2017 Kalev Lember <klember@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Tue Oct 04 2016 Kalev Lember <klember@redhat.com> - 1.3.3-1
- Update to 1.3.3

* Sun Sep 25 2016 Kalev Lember <klember@redhat.com> - 1.3.2-1
- Update to 1.3.2

* Sat Sep 10 2016 Kalev Lember <klember@redhat.com> - 1.3.1-2
- Use upstream bootstrapped tarball
- Require gstreamer1-plugins-bad-free-gtk on F25+

* Thu Sep 08 2016 Kalev Lember <klember@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Mon Aug 01 2016 Kalev Lember <klember@redhat.com> - 1.3-1
- Update to 1.3

* Sun May 22 2016 Kalev Lember <klember@redhat.com> - 1.2.2-1
- Update to 1.2.2

* Wed May 11 2016 Kalev Lember <klember@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 1.2-1
- Update to 1.2
- Run desktop-file-validate in the %%check section

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Ryan Lerch <rlerch@redhat.com> - 1.1-1
- Update to 1.1

* Sat Aug 22 2015 Kalev Lember <klember@redhat.com> - 1.0.1-1
- Update to 1.0.1
- Use license macro for COPYING
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Ryan Lerch <ryanlerch@fedoraproject.org> - 1.0-0
- Update to upstream version 1.0
* Thu Jan 29 2015 Ryan Lerch <ryanlerch@fedoraproject.org> - 0.9-0
- Update to upstream version 0.9
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Kalev Lember <kalevlember@gmail.com> - 0.8-3
- Backport appdata updates from upstream

* Thu Jul 31 2014 Kalev Lember <kalevlember@gmail.com> - 0.8-2
- Correct the appdata file name

* Mon Jul 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.8-1
- Update to 0.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Ryan Lerch <ryanlerch@fedoraproject.org> 0.7.0
* Updated to latest stable release 0.7

* Mon Feb 10 2014 Ryan Lerch <ryanlerch@fedoraproject.org> 0.6.1-201402101407gitde305e8
- Update to recent git snapshot to fix bz#1061571

* Tue Feb 04 2014 Ryan Lerch <ryanlerch@fedoraproject.org> 0.6.1-0
- Update to 0.6.1. This update was released shortly after 0.6, 
  so skipped 0.6.

* Tue Dec 03 2013 Ryan Lerch <ryanlerch@fedoraproject.org> 0.5-2
- Removed line from the spec that removed the old font files
- Changed the spec so the appdata dir is co-owned 

* Fri Nov 29 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.5-1
- Update to 0.5

* Mon Nov 04 2013 Ryan Lerch <ryanlerch@fedoraproject.org> - 0.4-0
- initial package

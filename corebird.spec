Name:           corebird
Version:        0.8
Release:        1%{?dist}
Summary:        Native GTK Twitter client
License:        GPLv3+
URL:            http://corebird.baedert.org/
Source0:        https://github.com/baedert/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Fix-the-build-with-Werror-format-security.patch
BuildRequires:        autoconf
BuildRequires:        automake
BuildRequires:        intltool
BuildRequires:        libtool
BuildRequires:        gtk3-devel >= 3.9
BuildRequires:        glib2-devel >= 2.38
BuildRequires:        gstreamer1-plugins-base-devel
BuildRequires:        rest-devel
BuildRequires:        json-glib-devel
BuildRequires:        libnotify-devel
BuildRequires:        sqlite-devel
BuildRequires:        libsoup-devel
BuildRequires:        vala-devel
BuildRequires:        librsvg2-tools
BuildRequires:        desktop-file-utils
BuildRequires:        libgee-devel

# For icon directories
Requires:           hicolor-icon-theme

%description
Native GTK Twitter client for the Linux desktop.

%prep
%setup -q
%patch0 -p1
NOCONFIGURE=1 ./autogen.sh

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Move the man page to the correct directory
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_mandir}/%{name}.1* \
   %{buildroot}%{_mandir}/man1/%{name}.1*

%find_lang corebird

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
%doc COPYING README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.baedert.corebird.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.baedert.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/appdata/
%{_mandir}/man1/%{name}.1*

%changelog
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

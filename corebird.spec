Name:           corebird
Version:        0.7
Release:        0%{?dist}
Summary:        Native GTK Twitter client
License:        GPLv3+
URL:            http://corebird.baedert.org/
Source0:        https://github.com/baedert/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:        gtk3-devel >= 3.9
BuildRequires:        glib2-devel >= 2.38
BuildRequires:        rest-devel
BuildRequires:        json-glib-devel
BuildRequires:        libnotify-devel
BuildRequires:        sqlite-devel
BuildRequires:        libsoup-devel
BuildRequires:        vala-devel
BuildRequires:        cmake
BuildRequires:        librsvg2-tools
BuildRequires:        desktop-file-utils
BuildRequires:        libgee-devel

# For icon directories
Requires:           hicolor-icon-theme

%description
Native GTK Twitter client for the Linux desktop.

%prep
%setup -q

%build
%{cmake} .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

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

%files
%doc COPYING README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.baedert.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/appdata/
%{_mandir}/man1/%{name}.1*

%changelog
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

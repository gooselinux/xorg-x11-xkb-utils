Summary: X.Org X11 xkb utilities
Name: xorg-x11-xkb-utils
Version: 7.4
Release: 6%{?dist}
License: MIT
Group: User Interface/X
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# use the macro so the doc dir is changed automagically
%define xkbutils_version 1.0.1
Source0: ftp://ftp.x.org/pub/individual/app/xkbutils-%{xkbutils_version}.tar.bz2
Source1: ftp://ftp.x.org/pub/individual/app/xkbcomp-1.1.1.tar.bz2
Source2: ftp://ftp.x.org/pub/individual/app/xkbevd-1.0.2.tar.bz2
Source3: ftp://ftp.x.org/pub/individual/app/xkbprint-1.0.1.tar.bz2
Source4: ftp://ftp.x.org/pub/individual/app/setxkbmap-1.1.0.tar.bz2

BuildRequires: pkgconfig
BuildRequires: libxkbfile-devel
BuildRequires: libX11-devel
BuildRequires: libXaw-devel
BuildRequires: libXt-devel
# FIXME: xkbvleds requires libXext, but autotools doesn't check/require it:
# gcc  -O2 -g -march=i386 -mcpu=i686   -o xkbvleds  xkbvleds-xkbvleds.o
# xkbvleds-LED.o xkbvleds-utils.o -lXaw7 -lXmu -lXt -lSM -lICE -lXext -lXpm -lX11 -ldl
# /usr/bin/ld: cannot find -lXext
# libXext-devel needed for xkbutils (from above error)
BuildRequires: libXext-devel
# FIXME: xkbvleds requires libXext, but autotools doesn't check/require it:
# gcc  -O2 -g -march=i386 -mcpu=i686   -o xkbvleds  xkbvleds-xkbvleds.o
# xkbvleds-LED.o xkbvleds-utils.o -lXaw7 -lXmu -lXt -lSM -lICE -lXext -lXpm -lX11 -ldl
# /usr/bin/ld: cannot find -lXpm
# libXpm-devel needed for xkbutils (from above error)
BuildRequires: libXpm-devel

Provides: setxkbmap xkbcomp
Obsoletes: XFree86 xorg-x11

%package -n xorg-x11-xkb-extras
Summary: X.Org X11 xkb gadgets
Provides: xkbevd xkbprint xkbutils

%description
X.Org X11 xkb core utilities

%description -n xorg-x11-xkb-extras
X.Org X11 xkb gadgets

%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4

%build
export CFLAGS="$RPM_OPT_FLAGS -DHAVE_STRCASECMP -Os"
for pkg in xkbutils setxkbmap xkbcomp xkbevd xkbprint ; do
    pushd $pkg-*
    %configure
    make
    popd
done

%install
rm -rf $RPM_BUILD_ROOT
for pkg in xkbutils setxkbmap xkbcomp xkbevd xkbprint ; do
    pushd $pkg-*
    make install DESTDIR=$RPM_BUILD_ROOT
    popd
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/setxkbmap
%{_bindir}/xkbcomp
%{_mandir}/man1/setxkbmap.1*
%{_mandir}/man1/xkbcomp.1*

%files -n xorg-x11-xkb-extras
%defattr(-,root,root,-)
%doc xkbutils-%{xkbutils_version}/AUTHORS xkbutils-%{xkbutils_version}/COPYING xkbutils-%{xkbutils_version}/INSTALL
%doc xkbutils-%{xkbutils_version}/NEWS xkbutils-%{xkbutils_version}/README
%{_bindir}/xkbbell
%{_bindir}/xkbevd
%{_bindir}/xkbprint
%{_bindir}/xkbvleds
%{_bindir}/xkbwatch
%{_mandir}/man1/xkbevd.1*
%{_mandir}/man1/xkbprint.1*

%changelog
* Wed Oct 07 2009 Adam Jackson <ajax@redhat.com> 7.4-6
- xkbcomp 1.1.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-4
- setxkbmap 1.1.0

* Thu Jul 09 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-3
- xkbcomp 1.1.0

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 7.4-2
- Fix missing %%defattr in -extras

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 7.4-1
- Split Xaw-requiring utilities to extras subpackage

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 25 2008 Peter Hutterer <peter.hutterer@redhat.com> 7.2-7
- xkbcomp 1.0.5
- Remove xkbcomp-1.0.4-open-less.patch.
- xkbcomp-1.0.5-dont-overwrite.patch: Don't overwrite groups unnecessarily.

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 7.2-6
- Fix license tag.

* Wed Apr 16 2008 Adam Jackson <ajax@redhat.com> 7.2-5
- xkbcomp 1.0.4
- xkbcomp-1.0.4-open-less.patch: Make xkbcomp faster by removing uncredible
  fail.

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 7.2-4
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 7.2-3
- Rebuild for ppc toolchain bug

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 7.2-2
- rebuild for toolchain bug

* Tue Jul 24 2007 Adam Jackson <ajax@redhat.com> 7.2-1
- setxkbmap 1.0.4
- Arbitrary version number bump, to match X.org release numbering.  Why not.

* Mon Jan 08 2007 Adam Jackson <ajax@redhat.com> 1.0.2-3
- From OLPC: jam -DHAVE_STRCASECMP into CFLAGS to make xkbcomp (and therefore
  X server startup) slightly less painfully slow.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Wed Jun 21 2006 Mike A. Harris <mharris@redhat.com> 1.0.2-2
- Added xkbutils_version macro, which can be used in the Version field
  in the future, to help prevent accidental bumping of the package version.

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 1.0.2-1
- Update setxkbmap, xkbevd, and xkbcomp

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated all apps to version 1.0.1 from X11R7.0

* Sat Dec 17 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated all apps to version 1.0.0 from X11R7 RC4.
- Changed manpage dir from man1x to man1 to match upstream default.

* Sun Nov 13 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-2
- Change from "Conflicts" to "Obsoletes: XFree86, xorg-x11" for upgrades.
- Rebuild against new libXaw 0.99.2-2, which has fixed DT_SONAME. (#173027)

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated to xkbutils-0.99.1, setxkbmap-0.99.2, xkbcomp-0.99.1, xkbevd-0.99.2,
  xkbprint-0.99.1 from X11R7 RC2.

* Thu Nov 10 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-3
- Updated xkbutils to version 0.99.0 from X11R7 RC1.  The upstream tarball
  changed, but the version stayed the same.  <sigh>
- Updated setxkbmap, xkbcomp, xkbevd, xkbprint.
- Change manpage location to 'man1x' in file manifest.
- Iterate over packages with for loop instead of serialized code duplication.

* Wed Oct 05 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-2
- Use Fedora-Extras style BuildRoot tag.
- Update BuildRequires to use new library package names.
- Tidy up spec file a bit.

* Wed Aug 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-1
- Initial build.

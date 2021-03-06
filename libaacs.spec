%global gitdate 20170926
%global commit0 883d3c07b156dab21f90a00d7ae7ca5b40ef9564
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           libaacs
Version:        0.9.0
Release: 	2%{?gver}%{?dist}
Summary:        Open implementation of AACS specification
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.videolan.org/developers/libaacs.html

# Do you want see the current commit and release? http://git.videolan.org/?p=libaacs.git
Source0:        http://git.videolan.org/?p=libaacs.git;a=snapshot;h=%{commit0};sf=tgz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool


BuildRequires:  libgcrypt-devel
BuildRequires:  flex
BuildRequires:  bison


%description
This library is an open implementation of the AACS specification.


%package utils
Summary:        Test utilities for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
The %{name}-utils package contains test utilities for %{name}.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{shortcommit0}
./bootstrap    
# sed -i -e 's/\r//' KEYDB.cfg


%build

autoreconf -vif

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING KEYDB.cfg ChangeLog README.txt
%{_libdir}/*.so.*

%files utils
%{_bindir}/aacs_info

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libaacs.pc


%changelog

* Tue Sep 26 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.9.0-2.git883d3c0
- Updated to 0.9.0-2.git883d3c0

* Tue Apr 25 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.8.1-3.gite2d31c9
- Updated to 0.8.1-3.gite2d31c9

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Mar 15 2015 Xavier Bachelot <xavier@bachelot.org> 0.8.1-1
- Update to 0.8.1.

* Tue Jan 27 2015 Xavier Bachelot <xavier@bachelot.org> 0.8.0-1
- Update to 0.8.0.

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 04 2014 Xavier Bachelot <xavier@bachelot.org> 0.7.1-1
- Update to 0.7.1.

* Sat Apr 26 2014 Xavier Bachelot <xavier@bachelot.org> 0.7.0-4
- Add patch for libgcrypt 1.6 support.
- Tweak the Release: tag to accomodate rpmdev-bumpspec.
- Modernize specfile.

* Sat Apr 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.7.0-3
- Rebuilt for libgcrypt

* Thu Dec 19 2013 Xavier Bachelot <xavier@bachelot.org> 0.7.0-2
- Move test utilities to their own subpackage to avoid potential multilib conflict.

* Thu Dec 19 2013 Xavier Bachelot <xavier@bachelot.org> 0.7.0-1
- Update to 0.7.0.

* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-4
- Rebuilt

* Sun Sep 08 2013 Xavier Bachelot <xavier@bachelot.org> 0.6.0-3
- Better rpath fix.

* Wed Aug 21 2013 Xavier Bachelot <xavier@bachelot.org> 0.6.0-2
- Fix rpath issue with aacs_info.

* Mon Mar 04 2013 Xavier Bachelot <xavier@bachelot.org> 0.6.0-1
- Update to 0.6.0.
- Switch back to bison.

* Mon Sep 03 2012 Xavier Bachelot <xavier@bachelot.org> 0.5.0-1
- Update to 0.5.0.
- Use byacc instead of bison, libaacs doesn't build with bison 2.6.1.

* Mon May 07 2012 Xavier Bachelot <xavier@bachelot.org> 0.4.0-1
- Update to 0.4.0.

* Thu Mar 22 2012 Xavier Bachelot <xavier@bachelot.org> 0.3.1-1
- Update to 0.3.1.

* Fri Dec 02 2011 Xavier Bachelot <xavier@bachelot.org> 0.3.0-1
- First official upstream release.

* Sat Nov 05 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.3.20111105git876f45a3f727e
- Update to latest snapshot.

* Tue Sep 27 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.2.20110925gite854d6673ad6c
- Make the devel package require arch-specific base package.

* Sun Sep 25 2011 Xavier Bachelot <xavier@bachelot.org> 0.2-0.1.20110925gite854d6673ad6c
- Update to latest snapshot.

* Sun Jul 10 2011 Xavier Bachelot <xavier@bachelot.org> 0.1-0.6.20110710git964342fbf3ed6
- Update to latest snapshot.

* Sun May 15 2011 Xavier Bachelot <xavier@bachelot.org> 0.1-0.5.20110515git497c22423d0e7
- Update to latest snapshot.

* Fri Jan 07 2011 Xavier Bachelot <xavier@bachelot.org> 0.1-0.4.20110107gite7aa4fd42c0d4
- Update to latest snapshot.

* Sun Nov 14 2010 Xavier Bachelot <xavier@bachelot.org> 0.1-0.3.20101114gitfb77542a8f6c7
- Update to latest snapshot.

* Thu Oct 21 2010 Xavier Bachelot <xavier@bachelot.org> 0.1-0.2.20101021git00b2df2bb7598
- Fix release tag.
- Update to latest snapshot.

* Tue Aug 17 2010 Xavier Bachelot <xavier@bachelot.org> 0.1-0.1.20100817
- Initial Fedora release.

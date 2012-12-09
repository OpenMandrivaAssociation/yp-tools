Summary: NIS (or YP) client programs
Name: yp-tools
Version: 2.10
Release: %mkrel 8
License: GPL
Group: System/Configuration/Networking
Source: ftp://ftp.kernel.org/pub/linux/utils/net/NIS/yp-tools-%{version}.tar.bz2
Source1: ftp://ftp.kernel.org/pub/linux/utils/net/NIS/yp-tools-%{version}.tar.bz2.sign
Patch1: yp-tools-2.7-md5.patch
Url: http://www.linux-nis.org/nis/
Requires: ypbind
Buildroot: %{_tmppath}/%{name}-root

%description
The Network Information Service (NIS) is a system which provides
network information (login names, passwords, home directories, group
information) to all of the machines on a network.  NIS can enable
users to login on any machine on the network, as long as the machine
has the NIS client programs running and the user's password is
recorded in the NIS passwd database.  NIS was formerly known as Sun
Yellow Pages (YP).

This package's NIS implementation is based on FreeBSD's YP and is a
special port for glibc 2.x and libc versions 5.4.21 and later.  This
package only provides the NIS client programs.  In order to use the
clients, you'll need to already have an NIS server running on your
network. An NIS server is provided in the ypserv package.

Install the yp-tools package if you need NIS client programs for machines
on your network.  You will also need to install the ypbind package on
every machine running NIS client programs.  If you need an NIS server,
you'll need to install the ypserv package on one machine on the network.

%prep
%setup -q
%patch1 -p1 -b .md5

%build
%configure --disable-domainname
%make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755)
%defattr(-,root,root)
%doc AUTHORS COPYING README ChangeLog NEWS etc/nsswitch.conf
%doc THANKS TODO
%attr(0755, root, root) %{_bindir}/*
%{_mandir}/*/*
%attr(0755, root, root) %{_sbindir}/*
/var/yp/nicknames





%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.10-6mdv2011.0
+ Revision: 671946
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 2.10-5mdv2011.0
+ Revision: 608261
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 2.10-4mdv2010.1
+ Revision: 519084
- rebuild

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 2.10-3mdv2009.1
+ Revision: 317943
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2.10-2mdv2008.1
+ Revision: 178843
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 16 2007 Olivier Thauvin <nanardon@mandriva.org> 2.10-1mdv2007.0
+ Revision: 121727
- 2.10

* Sat Jul 22 2006 Olivier Thauvin <nanardon@mandriva.org> 2.9-4mdv2007.0
+ Revision: 41833
- rebuild
- Import yp-tools

* Fri Oct 21 2005 Olivier Thauvin <nanardon@mandriva.org> 2.9-3mdk
- Fix non standard perm (rpmlint)

* Fri Oct 21 2005 Olivier Thauvin <nanardon@mandriva.org> 2.9-2mdk
- rebuild

* Fri Aug 27 2004 Frederic Lepied <flepied@mandrakesoft.com> 2.9-1mdk
- New release 2.9


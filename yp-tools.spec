Summary:	NIS (or YP) client programs
Name:		yp-tools
Version:	2.14
Release:	6
License:	GPL
Group:		System/Configuration/Networking
Source0:	http://www.linux-nis.org/download/yp-tools/yp-tools-%{version}.tar.bz2
Url:		http://www.linux-nis.org/nis/
Requires:	ypbind
# Not sent to upstream
Patch0:		yp-tools-2.11-shadow.patch
Patch3:		yp-tools-2.12-hash.patch
Patch4:		yp-tools-2.12-crypt.patch
Patch5:		yp-tools-2.12-adjunct.patch

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
%patch0 -p1 -b .shadow
%patch3 -p1 -b .hash
%patch4 -p1 -b .crypt
%patch5 -p1 -b .adjunct
autoreconf -fiv

%build
%configure2_5x --disable-domainname
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog NEWS etc/nsswitch.conf
%doc THANKS TODO
%attr(0755, root, root) %{_bindir}/*
%{_mandir}/*/*
%attr(0755, root, root) %{_sbindir}/*
/var/yp/nicknames

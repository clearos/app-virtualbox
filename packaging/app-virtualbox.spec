
Name: app-virtualbox
Epoch: 1
Version: 1.0.0
Release: 1%{dist}
Summary: VirtualBox Server - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-virtualbox-%{version}.tar.gz
Buildarch: noarch

%description
The VirtualBox Server app provides support for implementing VirtualBox on the server.

%package core
Summary: VirtualBox Server - Core
Requires: app-base-core
Requires: gcc
Requires: kernel-devel
Requires: kernel-headers

%description core
The VirtualBox Server app provides support for implementing VirtualBox on the server.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/virtualbox
cp -r * %{buildroot}/usr/clearos/apps/virtualbox/


%post core
logger -p local6.notice -t installer 'app-virtualbox-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/virtualbox/deploy/install ] && /usr/clearos/apps/virtualbox/deploy/install
fi

[ -x /usr/clearos/apps/virtualbox/deploy/upgrade ] && /usr/clearos/apps/virtualbox/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-virtualbox-core - uninstalling'
    [ -x /usr/clearos/apps/virtualbox/deploy/uninstall ] && /usr/clearos/apps/virtualbox/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/virtualbox/packaging
%exclude /usr/clearos/apps/virtualbox/tests
%dir /usr/clearos/apps/virtualbox
/usr/clearos/apps/virtualbox/deploy
/usr/clearos/apps/virtualbox/language
/usr/clearos/apps/virtualbox/libraries


Name: app-virtualbox
Epoch: 1
Version: 1.6.0
Release: 1%{dist}
Summary: VirtualBox Server
License: Proprietary
Group: ClearOS/Apps
Packager: eLogic
Vendor: eLogic
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base

%description
The VirtualBox Server app provides support for implementing VirtualBox on the server.

%package core
Summary: VirtualBox Server - Core
License: Proprietary
Group: ClearOS/Libraries
Requires: app-base-core
Requires: phpvirtualbox
Requires: virtualbox
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


%post
logger -p local6.notice -t installer 'app-virtualbox - installing'

%post core
logger -p local6.notice -t installer 'app-virtualbox-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/virtualbox/deploy/install ] && /usr/clearos/apps/virtualbox/deploy/install
fi

[ -x /usr/clearos/apps/virtualbox/deploy/upgrade ] && /usr/clearos/apps/virtualbox/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-virtualbox - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-virtualbox-core - uninstalling'
    [ -x /usr/clearos/apps/virtualbox/deploy/uninstall ] && /usr/clearos/apps/virtualbox/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/virtualbox/controllers
/usr/clearos/apps/virtualbox/htdocs
/usr/clearos/apps/virtualbox/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/virtualbox/packaging
%exclude /usr/clearos/apps/virtualbox/tests
%dir /usr/clearos/apps/virtualbox
/usr/clearos/apps/virtualbox/deploy
/usr/clearos/apps/virtualbox/language
/usr/clearos/apps/virtualbox/libraries

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bundle-chroot-builder
Version  : 1.02
Release  : 13
URL      : https://github.com/clearlinux/bundle-chroot-builder/archive/v1.02.tar.gz
Source0  : https://github.com/clearlinux/bundle-chroot-builder/archive/v1.02.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: bundle-chroot-builder-bin
Requires: bundle-chroot-builder-data

%description
Configuration File
==================
Please update the configuration file paths to point to where your
bundle-chroot-builder and clr-bundles directories are on the system.

%package bin
Summary: bin components for the bundle-chroot-builder package.
Group: Binaries
Requires: bundle-chroot-builder-data

%description bin
bin components for the bundle-chroot-builder package.


%package data
Summary: data components for the bundle-chroot-builder package.
Group: Data

%description data
data components for the bundle-chroot-builder package.


%prep
%setup -q -n bundle-chroot-builder-1.02

%build
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bundle-chroot-builder.py

%files data
%defattr(-,root,root,-)
/usr/share/defaults/bundle-chroot-builder/builder.conf

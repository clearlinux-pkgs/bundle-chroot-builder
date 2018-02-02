#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bundle-chroot-builder
Version  : 1.14
Release  : 30
URL      : https://github.com/clearlinux/bundle-chroot-builder/releases/download/v1.14/bundle-chroot-builder-1.14.tar.xz
Source0  : https://github.com/clearlinux/bundle-chroot-builder/releases/download/v1.14/bundle-chroot-builder-1.14.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: bundle-chroot-builder-bin
Requires: bundle-chroot-builder-data

%description
Building this Project
=====================
For help using automake see
http://www.gnu.org/software/automake/manual/html_node/index.html

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
%setup -q -n bundle-chroot-builder-1.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517513352
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1517513352
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

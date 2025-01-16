Name:    libnvme
Summary: Linux-native nvme device management library
Version: 1.11.1
Release: 1
License: LGPLv2+
URL:     https://github.com/sailfishos/libnvme
Source0: %{name}-%{version}.tar.gz

BuildRequires: meson >= 0.53
BuildRequires: json-c-devel >= 0.13
BuildRequires: openssl-devel
BuildRequires: keyutils-libs-devel

%description
Provides type definitions for NVMe specification structures,
enumerations, and bit fields, helper functions to construct,
dispatch, and decode commands and payloads, and utilities to connect,
scan, and manage nvme devices on a Linux system.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package provides header files to include and libraries to link with
for Linux-native nvme device management.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson -Dpython=disabled -Dlibdbus=disabled -Ddocs-build=false
%meson_build

%install
%meson_install

%files
%license COPYING ccan/licenses/*
%{_libdir}/libnvme.so.1
%{_libdir}/libnvme.so.1.11.1
%{_libdir}/libnvme-mi.so.1
%{_libdir}/libnvme-mi.so.1.11.1

%files devel
%{_libdir}/libnvme.so
%{_libdir}/libnvme-mi.so
%{_includedir}/libnvme.h
%{_includedir}/libnvme-mi.h
%dir %{_includedir}/nvme
%{_includedir}/nvme/*.h
%{_libdir}/pkgconfig/*.pc

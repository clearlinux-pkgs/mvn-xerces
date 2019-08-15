#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8BF6F97595597B05 (neilg@ca.ibm.com)
#
Name     : mvn-xerces
Version  : 1.4.4
Release  : 1
URL      : http://archive.apache.org/dist/xml/xerces-j/Xerces-J-src.1.4.4.tar.gz
Source0  : http://archive.apache.org/dist/xml/xerces-j/Xerces-J-src.1.4.4.tar.gz
Source1  : https://repo1.maven.org/maven2/xerces/xerces/1.4.4/xerces-1.4.4.jar
Source2  : https://repo1.maven.org/maven2/xerces/xerces/1.4.4/xerces-1.4.4.pom
Source3 : http://archive.apache.org/dist/xml/xerces-j/Xerces-J-src.1.4.4.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-1.1
Requires: mvn-xerces-data = %{version}-%{release}
Requires: mvn-xerces-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
Xerces Java Build Instructions
Table of Contents
1. Building Xerces
2. Building Documentation
3. Special Instructions
3.1 Building on Windows Platform
3.2 Building on UNIX Platform

%package data
Summary: data components for the mvn-xerces package.
Group: Data

%description data
data components for the mvn-xerces package.


%package license
Summary: license components for the mvn-xerces package.
Group: Default

%description license
license components for the mvn-xerces package.


%prep
%setup -q -n xerces-1_4_4

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-xerces
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-xerces/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/xerces/xerces/1.4.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/xerces/xerces/1.4.4/xerces-1.4.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/xerces/xerces/1.4.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/xerces/xerces/1.4.4/xerces-1.4.4.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/xerces/xerces/1.4.4/xerces-1.4.4.jar
/usr/share/java/.m2/repository/xerces/xerces/1.4.4/xerces-1.4.4.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-xerces/LICENSE

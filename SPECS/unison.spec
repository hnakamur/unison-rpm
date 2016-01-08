Name:           unison
Version:        2.48.3
Release:        1%{dist}
Summary:        File synchronization tool
License:        GPLv3+
URL:            http://www.cis.upenn.edu/~bcpierce/unison
Source0:        http://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-%{version}.tar.gz
Source1:        http://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-%{version}-manual.html
BuildRequires:  gtk2-devel
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Unison is a file-synchronization tool for OSX, Unix, and Windows. It allows
two replicas of a collection of files and directories to be stored on
different hosts (or different disks on the same host), modified separately,
and then brought up to date by propagating the changes in each replica to
the other.

%prep
%setup -q

%build
make UISTYLE=gtk2 NATIVE=true THREADS=true

%install
%{__install} -m 755 -d $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 %name $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 -d $RPM_BUILD_ROOT%{_docdir}
%{__install} -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/unison-manual.html

%files
%defattr(-,root,root)
%doc %{_docdir}/unison-manual.html
%{_bindir}/%{name}

%changelog
* Sat Jan  9 2016 Hiroaki Nakamura <hnakamur@gmail.com>
- 2.48.3

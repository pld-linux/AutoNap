%include	/usr/lib/rpm/macros.perl
Summary:	Napster/OpenNap client written in Perl
Summary(pl):	Klient Napstera/OpenNapa napisany w Perlu
Name:		AutoNap
Version:	0.1.3
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://autonap.sourceforge.net/rel/%{name}-%{version}.tar.gz
# Source0-md5:	c15a9c20a7cb63b88ba07027a60d556a
URL:		http://autonap.sourceforge.net/
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoNap is a (hopefully) fully automatizable Napster/OpenNap client
which consequently serves one lone purpose: Getting mp3s!

%description -l pl
AutoNap jest zdatnym do ca³kowitej automatyzacji klientem
Napstera/OpenNapa, konsekwentnie s³u¿±cym jednemu celowi: uzyskiwaniu
plików mp3.

%prep
%setup -q

%build
%{__perl} configure.PL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5},%{_sysconfdir}} \
	$RPM_BUILD_ROOT%{perl_vendorlib}

install ./target/AutoNap.pl $RPM_BUILD_ROOT%{_bindir}
install AutoNap.pl.1 $RPM_BUILD_ROOT%{_mandir}/man1
install autonap.conf $RPM_BUILD_ROOT%{_sysconfdir}
install autonap.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5
cp -a AutoLib $RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README-running Changelog
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%{perl_vendorlib}/AutoLib
%{_mandir}/man*/*

%include	/usr/lib/rpm/macros.perl
Summary:	Napster/OpenNap client written in Perl
Summary(pl):	Klient Napstera/OpenNapa napisany w Perlu
Name:		AutoNap
Version:	0.1.3
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	http://autonap.sourceforge.net/rel/%{name}-%{version}.tar.gz
URL:		http://autonap.sourceforge.net/
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoNap is a (hopefully) fully automatizable Napster/OpenNap client
which consequently serves one lone purpose: Getting mp3s!

%description -l pl
AutoNap jest zdatnym do ca�kowitej automatyzacji klientem
Napstera/OpenNapa, konsekwentnie s�u��cym jednemu celowi: uzyskiwaniu
plik�w mp3.

%prep
%setup -q

%build
perl configure.PL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5},%{_sysconfdir}} \
	$RPM_BUILD_ROOT%{perl_sitelib}
install ./target/AutoNap.pl $RPM_BUILD_ROOT%{_bindir}
install AutoNap.pl.1 $RPM_BUILD_ROOT%{_mandir}/man1
install autonap.conf $RPM_BUILD_ROOT%{_sysconfdir}
install autonap.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5
cp -a AutoLib $RPM_BUILD_ROOT%{perl_sitelib}

gzip -9nf README-running Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%{perl_sitelib}/AutoLib
%{_mandir}/man*/*

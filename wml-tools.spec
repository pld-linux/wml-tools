Summary:	Utilities for handling WML/WBMP files
Summary(pl):	Programy do obs³ugi plików WML/WBMP
Name:		wml-tools
Version:	0.0.4
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://pwot.org/wml/%{name}-%{version}.tgz
# Source0-md5:	a888ff9611ab735b4c02fa534bbcebbf
URL:		http://pwot.org/wml/
BuildRequires:	libxml-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the latest release of wml-tools. At the moment it only
contains a WBMP viewer, a simple WML bytecode decoder, a very simple
WML deck viewer and a tempremental WML to HTML converter. Also
included as a bonus is a Netscape RDF to WML deck converter. Vital to
get the /. headlines on your WAP device.

%description -l pl
Pakiet zawiera przegl±darkê WBMP, prosty dekoder bytecodu WML, prost±
przegl±darkê WML oraz kompilator WML do HTML. Jako dodatek jest
do³±czony konwerter plików RDF na WML. Pomo¿e w przegl±daniu
wiadomo¶ci ze /. na urz±dzeniu WAP.

%prep
%setup -q -n %{name}

%build
./configure --cc-flags "%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

for i in rdfwml wmlc wmld wmlhtml wmlv; do
	install $i/$i $RPM_BUILD_ROOT%{_bindir}
	install $i/README README.$i
done;
install wbmp/wbmp2xpm $RPM_BUILD_ROOT%{_bindir}
install wbmp/README README.wbmp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README WAP GOTCHAS Changelog README.{rdfwml,wbmp,wmlc,wmld,wmlhtml,wmlv}
%attr(755,root,root) %{_bindir}/*

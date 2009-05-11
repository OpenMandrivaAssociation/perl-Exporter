
%define realname   Exporter
%define version    5.63
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Implements default import method for modules
Source:     http://www.cpan.org/modules/by-module//%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

%description
The Exporter module implements an 'import' method which allows a module to
export functions and variables to its users' namespaces. Many modules use
Exporter rather than implementing their own 'import' method because
Exporter provides a highly flexible interface, with an implementation
optimised for the common case.

Perl automatically calls the 'import' method when processing a 'use'
statement for a module. Modules and 'use' are documented in the perlfunc
manpage and the perlmod manpage. Understanding the concept of modules and
how the 'use' statement operates is important to understanding the
Exporter.

How to Export
    The arrays '@EXPORT' and '@EXPORT_OK' in a module hold lists of symbols
    that are going to be exported into the users name space by default, or
    which they can request to be exported, respectively. The symbols can
    represent functions, scalars, arrays, hashes, or typeglobs. The symbols
    must be given by full name with the exception that the ampersand in
    front of a function is optional, e.g.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*



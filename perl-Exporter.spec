%define upstream_name    Exporter
%define upstream_version 5.66

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Implements default import method for modules
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	perl-devel

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
%setup -q -n %{upstream_name}-%{upstream_version}

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


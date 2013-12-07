%define module Gnome2-Canvas

Summary:	Perl module for the gnomecanvas library
Name:		perl-%module
Version:	1.002
Release:	21
License:	GPLv2 or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	Gnome2-Canvas-%{version}.tar.bz2
BuildRequires:	perl-ExtUtils-Depends 
BuildRequires:	perl-Gtk2 => 0.26
BuildRequires:	perl-ExtUtils-PkgConfig
Buildrequires:	perl-devel
BuildRequires:	pkgconfig(libgnomecanvas-2.0)
Requires:	perl-Gtk2 => 0.26
Provides:	perl-GnomeCanvas = %{version}
Obsoletes:	perl-GnomeCanvas >= 0.28

%description
The Gnome2::Canvas module allows a perl developer to use the GnomeCanvas
widget with Gtk2-Perl.


%prep
%setup -qn %module-%{version}
find -type d -name CVS | rm -rf 
perl Makefile.PL INSTALLDIRS=vendor

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE canvas_demo
%{perl_vendorarch}/Gnome2/Canvas
%{perl_vendorarch}/Gnome2/Canvas.*
%{perl_vendorarch}/auto/*
%{_mandir}/man3/*


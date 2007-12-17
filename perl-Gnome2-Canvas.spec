%define module Gnome2-Canvas

Summary: Perl module for the gnomecanvas library
Name:    perl-%module
Version: 1.002
Release: %mkrel 7
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  Gnome2-Canvas-%version.tar.bz2
URL: http://gtk2-perl.sf.net/

BuildRequires: libgnomecanvas2-devel
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Gtk2 => 0.26
BuildRequires: perl-ExtUtils-PkgConfig
Buildrequires: perl-devel

Requires: perl-Gtk2 => 0.26
Conflicts: drakxtools < 9.1-15mdk
provides: perl-GnomeCanvas = %version
Obsoletes: perl-GnomeCanvas >= 0.28

%description
The Gnome2::Canvas module allows a perl developer to use the GnomeCanvas
widget with Gtk2-Perl.


%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 
perl Makefile.PL INSTALLDIRS=vendor

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc AUTHORS LICENSE canvas_demo
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2/Canvas
%{perl_vendorarch}/Gnome2/Canvas.*
%{perl_vendorarch}/auto/*



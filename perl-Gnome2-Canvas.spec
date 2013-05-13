%define module Gnome2-Canvas

Summary: Perl module for the gnomecanvas library
Name:    perl-%module
Version: 1.002
Release:	18
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  Gnome2-Canvas-%version.tar.bz2
URL: http://gtk2-perl.sf.net/

BuildRequires: pkgconfig(libgnomecanvas-2.0)
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Gtk2 => 0.26
BuildRequires: perl-ExtUtils-PkgConfig
Buildrequires: perl-devel

Requires: perl-Gtk2 => 0.26
Conflicts: drakxtools < 9.1-15mdk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%doc AUTHORS LICENSE canvas_demo
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2/Canvas
%{perl_vendorarch}/Gnome2/Canvas.*
%{perl_vendorarch}/auto/*




%changelog
* Wed Jan 25 2012 Per √òyvind Karlsen <peroyvind@mandriva.org> 1.002-18
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.002-15
+ Revision: 702773
- rebuilt against libpng-1.5.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.002-14
+ Revision: 667181
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.002-13mdv2011.0
+ Revision: 564477
- rebuild for perl 5.12.1

* Tue Jul 20 2010 J√©r√¥me Quelin <jquelin@mandriva.org> 1.002-12mdv2011.0
+ Revision: 555875
- rebuild for perl 5.12

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.002-11mdv2010.1
+ Revision: 426449
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.002-10mdv2009.1
+ Revision: 351775
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.002-9mdv2009.0
+ Revision: 223771
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.002-8mdv2008.1
+ Revision: 152089
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 1.002-7mdv2008.0
+ Revision: 44609
- rebuild


* Mon Feb 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.002-6mdv2007.0
+ Revision: 122790
- rebuild in order to get the same extension on x86_64

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Gnome2-Canvas

* Tue Oct 11 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.002-5mdk
- Fix previous mistake

* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.002-4mdk
- fix buildrequires

* Tue May 10 2005 Stew Benedict <sbenedict@mandriva.com> 1.002-3mdk
- fix buildrequires

* Fri Dec 17 2004 Stew Benedict <sbenedict@mandrakesoft.com> 1.002-2mdk
- rebuild for new perl-5.8.6

* Tue Aug 17 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.002-1mdk
- new release

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.001-2mdk
- rebuild for perl-5.8.5

* Mon Jun 07 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.001-1mdk
- new release

* Wed Mar 31 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.00-1mdk
- new release


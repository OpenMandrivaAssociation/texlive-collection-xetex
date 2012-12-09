# revision 25850
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-xetex
Epoch:		1
Version:	20120413
Release:	1
Summary:	XeTeX packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-xetex.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-arabxetex
Requires:	texlive-euenc
Requires:	texlive-fixlatvian
Requires:	texlive-fontbook
Requires:	texlive-fontwrap
Requires:	texlive-mathspec
Requires:	texlive-philokalia
Requires:	texlive-polyglossia
Requires:	texlive-realscripts
Requires:	texlive-unisugar
Requires:	texlive-xecjk
Requires:	texlive-xecolor
Requires:	texlive-xecyr
Requires:	texlive-xeindex
Requires:	texlive-xepersian
Requires:	texlive-xesearch
Requires:	texlive-xetex
Requires:	texlive-xetex-def
Requires:	texlive-xetex-itrans
Requires:	texlive-xetex-pstricks
Requires:	texlive-xetexconfig
Requires:	texlive-xetexfontinfo
Requires:	texlive-xltxtra
Requires:	texlive-xunicode
Requires:	texlive-collection-basic

%description
Packages for XeTeX, the Unicode/OpenType-enabled TeX by
Jonathan Kew, http://tug.org/xetex.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Sat Apr 14 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120413-1
+ Revision: 790895
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780512
- Update to latest release.
- Import texlive-collection-xetex
- Import texlive-collection-xetex


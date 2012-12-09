# revision 25870
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-mathextra
Epoch:		1
Version:	20120413
Release:	1
Summary:	Advanced math typesetting
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-mathextra.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-12many
Requires:	texlive-amstex
Requires:	texlive-binomexp
Requires:	texlive-boldtensors
Requires:	texlive-bosisio
Requires:	texlive-ccfonts
Requires:	texlive-commath
Requires:	texlive-concmath
Requires:	texlive-concrete
Requires:	texlive-eqnarray
Requires:	texlive-extarrows
Requires:	texlive-extpfeil
Requires:	texlive-faktor
Requires:	texlive-ionumbers
Requires:	texlive-isomath
Requires:	texlive-mathcomp
Requires:	texlive-mattens
Requires:	texlive-mhequ
Requires:	texlive-multiobjective
Requires:	texlive-nath
Requires:	texlive-ot-tableau
Requires:	texlive-oubraces
Requires:	texlive-proba
Requires:	texlive-rec-thy
Requires:	texlive-shuffle
Requires:	texlive-statex
Requires:	texlive-statex2
Requires:	texlive-stmaryrd
Requires:	texlive-subsupscripts
Requires:	texlive-susy
Requires:	texlive-syllogism
Requires:	texlive-synproof
Requires:	texlive-tablor
Requires:	texlive-tensor
Requires:	texlive-tex-ewd
Requires:	texlive-thmbox
Requires:	texlive-turnstile
Requires:	texlive-unicode-math
Requires:	texlive-venn
Requires:	texlive-yhmath
Requires:	texlive-ytableau
Requires:	texlive-collection-fontsrecommended
Requires:	texlive-collection-latex

%description
Extra math.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Sat Apr 14 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120413-1
+ Revision: 790882
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780502
- Update to latest release.
- Import texlive-collection-mathextra
- Import texlive-collection-mathextra


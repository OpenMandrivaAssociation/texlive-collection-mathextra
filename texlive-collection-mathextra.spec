# revision 21870
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-mathextra
Version:	20120223
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
Requires:	texlive-realscripts
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
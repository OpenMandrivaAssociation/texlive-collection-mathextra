# revision 32693
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-mathextra
Epoch:		1
Version:	20140215
Release:	2
Summary:	Mathematics packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-mathextra.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-fontsrecommended
Requires:	texlive-collection-latex
Requires:	texlive-12many
Requires:	texlive-amstex
Requires:	texlive-backnaur
Requires:	texlive-binomexp
Requires:	texlive-boldtensors
Requires:	texlive-bosisio
Requires:	texlive-bropd
Requires:	texlive-ccfonts
Requires:	texlive-commath
Requires:	texlive-concmath
Requires:	texlive-concrete
Requires:	texlive-conteq
Requires:	texlive-eqnarray
Requires:	texlive-extarrows
Requires:	texlive-extpfeil
Requires:	texlive-faktor
Requires:	texlive-interval
Requires:	texlive-ionumbers
Requires:	texlive-isomath
Requires:	texlive-lplfitch
Requires:	texlive-mathcomp
Requires:	texlive-mattens
Requires:	texlive-mhequ
Requires:	texlive-multiobjective
Requires:	texlive-natded
Requires:	texlive-nath
Requires:	texlive-ot-tableau
Requires:	texlive-oubraces
Requires:	texlive-proba
Requires:	texlive-rec-thy
Requires:	texlive-ribbonproofs
Requires:	texlive-shuffle
Requires:	texlive-skmath
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

%description
TeXLive collection-mathextra package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install

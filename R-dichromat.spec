%global packname dichromat
%global rlibdir %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.0_0
Release:          1
Summary:          Color Schemes for Dichromats
Group:            Sciences/Mathematics
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-0.tar.gz
BuildArch:        noarch
Requires:         R-stats
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-stats

%description
Collapse red-green or green-blue distinctions to simulate
the effects of different types of color-blindness.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R

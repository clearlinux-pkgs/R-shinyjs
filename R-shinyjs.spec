#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-shinyjs
Version  : 2.0.0
Release  : 35
URL      : https://cran.r-project.org/src/contrib/shinyjs_2.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/shinyjs_2.0.0.tar.gz
Summary  : Easily Improve the User Experience of Your Shiny Apps in Seconds
Group    : Development/Tools
License  : MIT
Requires: R-digest
Requires: R-htmltools
Requires: R-jsonlite
Requires: R-shiny
BuildRequires : R-digest
BuildRequires : R-htmltools
BuildRequires : R-jsonlite
BuildRequires : R-shiny
BuildRequires : buildreq-R

%description
greatly improve your apps without having to know any JavaScript. Examples

%prep
%setup -q -c -n shinyjs
cd %{_builddir}/shinyjs

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599849333

%install
export SOURCE_DATE_EPOCH=1599849333
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinyjs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinyjs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shinyjs
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc shinyjs || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/shinyjs/DESCRIPTION
/usr/lib64/R/library/shinyjs/INDEX
/usr/lib64/R/library/shinyjs/LICENSE
/usr/lib64/R/library/shinyjs/Meta/Rd.rds
/usr/lib64/R/library/shinyjs/Meta/features.rds
/usr/lib64/R/library/shinyjs/Meta/hsearch.rds
/usr/lib64/R/library/shinyjs/Meta/links.rds
/usr/lib64/R/library/shinyjs/Meta/nsInfo.rds
/usr/lib64/R/library/shinyjs/Meta/package.rds
/usr/lib64/R/library/shinyjs/Meta/vignette.rds
/usr/lib64/R/library/shinyjs/NAMESPACE
/usr/lib64/R/library/shinyjs/NEWS.md
/usr/lib64/R/library/shinyjs/R/shinyjs
/usr/lib64/R/library/shinyjs/R/shinyjs.rdb
/usr/lib64/R/library/shinyjs/R/shinyjs.rdx
/usr/lib64/R/library/shinyjs/doc/index.html
/usr/lib64/R/library/shinyjs/doc/shinyjs-example.R
/usr/lib64/R/library/shinyjs/doc/shinyjs-example.Rmd
/usr/lib64/R/library/shinyjs/doc/shinyjs-example.html
/usr/lib64/R/library/shinyjs/doc/shinyjs-extend.R
/usr/lib64/R/library/shinyjs/doc/shinyjs-extend.Rmd
/usr/lib64/R/library/shinyjs/doc/shinyjs-extend.html
/usr/lib64/R/library/shinyjs/doc/shinyjs-usage.R
/usr/lib64/R/library/shinyjs/doc/shinyjs-usage.Rmd
/usr/lib64/R/library/shinyjs/doc/shinyjs-usage.html
/usr/lib64/R/library/shinyjs/doc/shinyjs.R
/usr/lib64/R/library/shinyjs/doc/shinyjs.Rmd
/usr/lib64/R/library/shinyjs/doc/shinyjs.html
/usr/lib64/R/library/shinyjs/examples/basic/DESCRIPTION
/usr/lib64/R/library/shinyjs/examples/basic/app.R
/usr/lib64/R/library/shinyjs/examples/basic/helper-text.R
/usr/lib64/R/library/shinyjs/examples/demo/helpers.R
/usr/lib64/R/library/shinyjs/examples/demo/server.R
/usr/lib64/R/library/shinyjs/examples/demo/ui.R
/usr/lib64/R/library/shinyjs/examples/demo/www/github-green-right.png
/usr/lib64/R/library/shinyjs/examples/demo/www/header.png
/usr/lib64/R/library/shinyjs/examples/demo/www/style.css
/usr/lib64/R/library/shinyjs/examples/sandbox/helpers.R
/usr/lib64/R/library/shinyjs/examples/sandbox/server.R
/usr/lib64/R/library/shinyjs/examples/sandbox/ui.R
/usr/lib64/R/library/shinyjs/examples/sandbox/www/github-green-right.png
/usr/lib64/R/library/shinyjs/examples/sandbox/www/header.png
/usr/lib64/R/library/shinyjs/examples/sandbox/www/style.css
/usr/lib64/R/library/shinyjs/help/AnIndex
/usr/lib64/R/library/shinyjs/help/aliases.rds
/usr/lib64/R/library/shinyjs/help/paths.rds
/usr/lib64/R/library/shinyjs/help/shinyjs.rdb
/usr/lib64/R/library/shinyjs/help/shinyjs.rdx
/usr/lib64/R/library/shinyjs/html/00Index.html
/usr/lib64/R/library/shinyjs/html/R.css
/usr/lib64/R/library/shinyjs/img/banner.png
/usr/lib64/R/library/shinyjs/img/colourPickerGadget.gif
/usr/lib64/R/library/shinyjs/img/colourpickerscrnshot.png
/usr/lib64/R/library/shinyjs/img/demo-basic-v1.png
/usr/lib64/R/library/shinyjs/img/extendshinyjs-demo.gif
/usr/lib64/R/library/shinyjs/img/extendshinyjs-params.gif
/usr/lib64/R/library/shinyjs/img/shinyjs-logo-whitebg-small.png
/usr/lib64/R/library/shinyjs/srcjs/inject.js
/usr/lib64/R/library/shinyjs/srcjs/shinyjs-default-funcs.js
/usr/lib64/R/library/shinyjs/tests/testthat.R
/usr/lib64/R/library/shinyjs/tests/testthat/test-hidden.R

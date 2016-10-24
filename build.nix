{ pkgs ?  import <nixpkgs> {}
, stdenv ? pkgs.stdenv
} :
let

  pydev = stdenv.mkDerivation {
    name = "pydev";
    buildInputs =
      with pkgs;
      with pkgs.python2Packages;
    [
      ipython
      python
      scipy
      numpy
      matplotlib
      xlibs.xeyes
      pycairo
      pyqt5
      pygobject2
      gtk3
      gobjectIntrospection

      beautifulsoup
      clientform
      mechanize
      pyrss2gen
    ];

    shellHook = ''
      export MPLBACKEND='Qt5Agg'
      alias ipython='ipython --matplotlib=qt5'
    '';
  };

in
  pydev

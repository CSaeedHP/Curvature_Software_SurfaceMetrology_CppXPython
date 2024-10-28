{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "Curvature-env";
  buildInputs = with pkgs; with python312Packages; [
    tkinter
    numpy
    matplotlib
    plotly
    alive-progress
    numba
    pandas
    xmltodict
    # math
    
    git
    wget
    # (python312.withPackages (p: with p; [
    #   pip
    #   alive_progress
    #   matplotlib
    #   plotly
    # ]))
  ];

}

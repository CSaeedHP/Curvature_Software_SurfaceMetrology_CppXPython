{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "Curvature-env";
  buildInputs = with pkgs; [
    git
    wget
    gcc
    cmake
  ];

}

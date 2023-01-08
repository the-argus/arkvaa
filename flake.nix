{
  description = "Documents relating to Arkv'aa Desert Tavern";
  inputs.nixpkgs.url = github:nixos/nixpkgs?ref=nixos-22.11;
  inputs.lonesome-stranger.url = github:the-argus/lonesome-stranger;

  outputs = {
    self,
    nixpkgs,
    lonesome-stranger,
  }: let
    supportedSystems = [
      "x86_64-linux"
      "aarch64-linux"
    ];
    genSystems = nixpkgs.lib.genAttrs supportedSystems;
    pkgs = genSystems (system: import nixpkgs {inherit system;});
  in {
    devShell = genSystems (system:
      pkgs.${system}.mkShell {
        packages = with pkgs.${system}; [
          (pkgs.${system}.python310.withPackages (_: [
            lonesome-stranger.packages.${system}.dungeonsheets
          ]))
          pdftk
          texlive.combined.scheme-basic
        ];
      });
  };
}

{ lib, stdenvNoCC, python3, librsvg, xorg }:

stdenvNoCC.mkDerivation rec {
  pname = "bibata-cursor";
  version = "0.2.0";

  src = ./.;

  nativeBuildInputs = [
    python3
    librsvg
    xorg.xcursorgen
  ];

  dontConfigure = true;

  buildPhase = ''
    runHook preBuild
    python3 src/cursor_utils.py --hypr --x11 --out-dir out
    runHook postBuild
  '';

  installPhase = ''
    runHook preInstall
    mkdir -p "$out/share/icons"
    cp -r out/Bibata-* "$out/share/icons/"
    runHook postInstall
  '';

  meta = with lib; {
    description = "Bibata cursor theme for X11 and Hyprland";
    homepage = "https://github.com/rtgiskard/bibata_cursor";
    license = licenses.gpl3Plus;
    platforms = platforms.linux;
  };
}
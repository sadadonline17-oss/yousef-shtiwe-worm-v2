# nix/packages.nix — YOUSEF SHTIWE Agent package built with uv2nix
{ inputs, ... }: {
  perSystem = { pkgs, system, ... }:
    let
      yousef shtiweVenv = pkgs.callPackage ./python.nix {
        inherit (inputs) uv2nix pyproject-nix pyproject-build-systems;
      };

      # Import bundled skills, excluding runtime caches
      bundledSkills = pkgs.lib.cleanSourceWith {
        src = ../skills;
        filter = path: _type:
          !(pkgs.lib.hasInfix "/index-cache/" path);
      };

      runtimeDeps = with pkgs; [
        nodejs_20 ripgrep git openssh ffmpeg tirith
      ];

      runtimePath = pkgs.lib.makeBinPath runtimeDeps;
    in {
      packages.default = pkgs.stdenv.mkDerivation {
        pname = "yousef shtiwe-agent";
        version = (builtins.fromTOML (builtins.readFile ../pyproject.toml)).project.version;

        dontUnpack = true;
        dontBuild = true;
        nativeBuildInputs = [ pkgs.makeWrapper ];

        installPhase = ''
          runHook preInstall

          mkdir -p $out/share/yousef shtiwe-agent $out/bin
          cp -r ${bundledSkills} $out/share/yousef shtiwe-agent/skills

          ${pkgs.lib.concatMapStringsSep "\n" (name: ''
            makeWrapper ${yousef shtiweVenv}/bin/${name} $out/bin/${name} \
              --suffix PATH : "${runtimePath}" \
              --set YOUSEF SHTIWE_BUNDLED_SKILLS $out/share/yousef shtiwe-agent/skills
          '') [ "yousef shtiwe" "yousef shtiwe-agent" "yousef shtiwe-acp" ]}

          runHook postInstall
        '';

        meta = with pkgs.lib; {
          description = "AI agent with advanced tool-calling capabilities";
          homepage = "https://github.com/YOUSEF SHTIWE-OVERLORD/yousef shtiwe-agent";
          mainProgram = "yousef shtiwe";
          license = licenses.mit;
          platforms = platforms.unix;
        };
      };
    };
}

# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running ‘nixos-help’).

{ config, pkgs, ... }:

{
  imports =
    [ # Include the results of the hardware scan.
      ./hardware-configuration.nix
    ];

  # Bootloader.
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;

  networking.hostName = "nixos"; # Define your hostname.
  # networking.wireless.enable = true;  # Enables wireless support via wpa_supplicant.

  # Configure network proxy if necessary
  # networking.proxy.default = "http://user:password@proxy:port/";
  # networking.proxy.noProxy = "127.0.0.1,localhost,internal.domain";

  # Enable networking
  networking.networkmanager.enable = true;

  # Set your time zone.
  time.timeZone = "Europe/Madrid";

  # Select internationalisation properties.
  i18n.defaultLocale = "en_US.UTF-8";

  i18n.extraLocaleSettings = {
    LC_ADDRESS = "en_US.UTF-8";
    LC_IDENTIFICATION = "en_US.UTF-8";
    LC_MEASUREMENT = "en_US.UTF-8";
    LC_MONETARY = "en_US.UTF-8";
    LC_NAME = "en_US.UTF-8";
    LC_NUMERIC = "en_US.UTF-8";
    LC_PAPER = "en_US.UTF-8";
    LC_TELEPHONE = "en_US.UTF-8";
    LC_TIME = "en_US.UTF-8";
  };

  # virt-manager ----------------------------------------------------------------
  virtualisation.libvirtd.enable = true;
  programs.virt-manager.enable = true;
  # users.users.jesus.extraGroups = [ "libvirtd" ];
  # virt-manager END ----------------------------------------------------------------

  # Enable the X11 windowing system.
  services.xserver.enable = true;

  # Enable the KDE Plasma Desktop Environment.
  services.xserver.displayManager.sddm.enable = true;
  services.xserver.desktopManager.plasma5.enable = true;

  # Configure keymap in X11
  services.xserver = {
    layout = "us";
    xkbVariant = "";
  };

  # Enable CUPS to print documents.
  services.printing.enable = true;

  # obs --------------------------------------
  # hardware.opengl.enable = true;
  # obs END --------------------------------------
  # Enable sound with pipewire.
  sound.enable = true;
  hardware.pulseaudio.enable = false;
  security.rtkit.enable = true;
  services.pipewire = {
    enable = true;
    alsa.enable = true;
    alsa.support32Bit = true;
    pulse.enable = true;
    # If you want to use JACK applications, uncomment this
    #jack.enable = true;

    # use the example session manager (no others are packaged yet so this is enabled by default,
    # no need to redefine it in your config for now)
    #media-session.enable = true;
  };

  # Enable touchpad support (enabled default in most desktopManager).
  # services.xserver.libinput.enable = true;

  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users.jesus = {
    isNormalUser = true;
    description = "jesus";
    # extraGroups = [ "networkmanager" "wheel" ];
    # extraGroups = [ "networkmanager" "wheel" "libvirtd" ]; # added to use Virtual manager
    extraGroups = [
      "networkmanager" "wheel" "libvirtd" "video"
    ]; # added to use obs
    packages = with pkgs; [
      firefox
      kate
    #  thunderbird
    ];
  };

  # Allow unfree packages
  nixpkgs.config.allowUnfree = true;

  # List packages installed in system profile. To search, run:
  # $ nix search wget
  environment.systemPackages = with pkgs; [
  #  vim # Do not forget to add an editor to edit configuration.nix! The Nano editor is also installed by default.
  #  wget
  # personal
  xclip
  skypeforlinux
  git
  vlc
  # obs-studio
  (pkgs.wrapOBS {
    plugins = with pkgs.obs-studio-plugins; [
      obs-3d-effect
      obs-backgroundremoval
      obs-vintage-filter
      obs-freeze-filter
      obs-scale-to-sound
      ];
  })
  openshot-qt
  discord
  # chromium
  libreoffice
  neofetch
  # glsl language server
  glslls
  # doom emacs prerequisites
  emacs
  ripgrep
  fd
  coreutils
  clang
  multimarkdown
  shellcheck
  # python with packages ----------------------------------------
  (python3.withPackages(ps: with ps; [
  numpy
  pygame
  moderngl
  pyglm
  # needed for load .obj
  (
    buildPythonPackage rec {
      pname = "PyWavefront";
      version = "1.3.3";
      src = fetchurl {
        url = "https://github.com/pywavefront/PyWavefront/archive/refs/tags/1.3.3.tar.gz";
        # If you don't know the hash, the first time, set:
        # sha256 = "sha256-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=";
        # then nix will fail the build with such an error message and the true sha256
        sha256 = "sha256-Cf1M0ft46WWe4zuCsbXHFp35f5CNUM0/6/zibGxhkD0=";
      };
      doCheck = false;
      #propagaBuildInputs = [
      #];
      }
  )
  # just to visualize the commits line with Kate
  python-lsp-server
  # read e2e
  h5py # requeriment for oct_converter
  construct # requeriment for oct_converter
  opencv4 # requeriment for oct_converter
  imageio # requeriment for oct_converter
  matplotlib # requeriment for oct_converter
  pydicom # requeriment for oct_converter
  imageio-ffmpeg
  pyavm
  (
    buildPythonPackage rec {
      pname = "oct_converter";
      version = "0.5.7";
      src = fetchPypi {
        inherit pname version;
        sha256 = "3d6299e0c781f2d520f5475845d6360ac73eb542cd9542645f1bdb628c978424";
      };
      doCheck = false;
      #propagaBuildInputs = [
      #];
      }
  )
  #
  pillow # requeriment for heyexReader
  (
    buildPythonPackage rec {
      pname = "heyexReader";
      version = "0.1.3";
      src = fetchPypi {
        inherit pname version;
        sha256 = "0544a48645921289b82e5108aeeb7476ff08442a26ac57ad44c093464fa84392";
      };
      doCheck = false;
      #propagaBuildInputs = [
      #];
      }
  )
  # jupyter on python -----------
  jupyter
  ipython
  # jupyter on python END -----------
  # deep learning
  tensorflow
  keras
  sklearn-deap
  pandas
  # other python packages
  ]))
  # jupyter on python -----------
  pandoc
  texliveFull
  quarto
  # jupyter on python END -----------
  # other nixos packages
  neovim
  screenkey # show key on screen
  ];

  fonts.packages = with pkgs; [ nerdfonts ];
  # Some programs need SUID wrappers, can be configured further or are
  # started in user sessions.
  # programs.mtr.enable = true;
  # programs.gnupg.agent = {
  #   enable = true;
  #   enableSSHSupport = true;
  # };

  # List services that you want to enable:

  # Enable the OpenSSH daemon.
  # services.openssh.enable = true;

  # Open ports in the firewall.
  # networking.firewall.allowedTCPPorts = [ ... ];
  # networking.firewall.allowedUDPPorts = [ ... ];
  # Or disable the firewall altogether.
  # networking.firewall.enable = false;

  # This value determines the NixOS release from which the default
  # settings for stateful data, like file locations and database versions
  # on your system were taken. It‘s perfectly fine and recommended to leave
  # this value at the release version of the first install of this system.
  # Before changing this value read the documentation for this option
  # (e.g. man configuration.nix or on https://nixos.org/nixos/options.html).
  system.stateVersion = "23.11"; # Did you read the comment?

}

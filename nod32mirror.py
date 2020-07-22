import config

version = "0.0.1"

if __name__ == "__main__":
    path = "settings.ini"
    cf = config.Nod32mirrorConfig(path)
    if not config.config_exists(path):
        cf.create_config()
    cf.config_read()

    if cf.get("Actions", "show_version") == "1":
        print("Nod32 Update Mirror Script, version {}".format(version))

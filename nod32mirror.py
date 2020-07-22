import config

if __name__ == "__main__":
    path = "settings.ini"
    cf = config.Nod32mirrorConfig(path)
    if not config.config_exists(path):
        cf.create_config()

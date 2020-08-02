import config
import glob
import os
import constants

import keys

version = "0.0.1"


def flush_base_dir():
    mirror_dir = cf.get("Settings", "mirror_dir")
    if not mirror_dir:
        print("Не указан каталог хранения баз (mirror_dir).")
        return

    list_files = (mirror_dir + "\\**\\*.nup",
                  mirror_dir + "\\**\\*._*",
                  mirror_dir + "\\**\\*.ver",
                  mirror_dir + "\\**\\" + cf.get("Settings", "timestamp_file_name"),
                  mirror_dir + "\\**\\" + cf.get("Settings", "version_file_name"),)

    for str_file in list_files:
        files = glob.glob(str_file, recursive=True)
        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print("Ошибка: {} : {}".format(f, e.strerror))


if __name__ == "__main__":
    path = constants.PATH_SETTINGS
    cf = config.Nod32mirrorConfig(path)
    if not config.config_exists(path):
        cf.create_config()
    cf.config_read()

    if cf.get("Actions", "show_version") == "1":
        print("Nod32 Update Mirror Script, version {}".format(version))

    if cf.get("Actions", "make_flush") == "1":
        flush_base_dir()

    if cf.get("Actions", "get_key"):
        key = keys.Key()
        key.get_random_key()

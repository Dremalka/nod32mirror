import configparser
import os


def config_exists(path):
    """ Конфиг файл существует? """
    return os.path.exists(path)


class Nod32mirrorConfig:

    def __init__(self, path):
        self.cf = configparser.ConfigParser()
        self.path = path

    def create_config(self):
        """
        Создать конфиг-файл
        """
        self.cf.add_section("Settings")
        self.cf.set("Settings", "debug_mode", "0")
        self.cf.set("Settings", "use_free_key", "0")
        self.cf.set("Settings", "mirror_dir", "")
        self.cf.set("Settings", "temp_dir", "")
        self.cf.set("Settings", "platforms", "all")
        self.cf.set("Settings", "types", "all")
        self.cf.set("Settings", "languages", "1033 1049")
        self.cf.set("Settings", "versions", "pcu 7 8")
        self.cf.set("Settings", "win10upgrade_enabled", "1")
        self.cf.set("Settings", "version_file_crlf", "1")
        self.cf.set("Settings", "log_path", "nod32mirror.log")
        self.cf.set("Settings", "curl_bin", "false")
        self.cf.set("Settings", "wget_bin", "false")
        self.cf.set("Settings", "test_uri", "http://update.eset.com:80/v8-rel-sta/mod_010_smon_1036/em010_32_l0.nup")
        self.cf.set("Settings", "download_delay", "1")
        self.cf.set("Settings", "download_max_time", "60")
        self.cf.set("Settings", "useragent", "ESS Update")
        self.cf.set("Settings", "timestamp_file_name", "lastevent.txt")
        self.cf.set("Settings", "version_file_name", "version.txt")
        self.cf.set("Settings", "version_file_name", "version.txt")

        self.cf.add_section("Mirrors")
        self.cf.set("Mirrors", "server_1", "")
        self.cf.set("Mirrors", "server_2", "")
        self.cf.set("Mirrors", "server_3", "")
        self.cf.set("Mirrors", "server_4", "")

        self.cf.add_section("Actions")
        self.cf.set("Actions", "make_update", "0")
        self.cf.set("Actions", "make_flush", "0")
        self.cf.set("Actions", "get_key", "0")
        self.cf.set("Actions", "keys_update", "0")
        self.cf.set("Actions", "keys_clean", "0")
        self.cf.set("Actions", "keys_show", "0")
        self.cf.set("Actions", "disable_network_limits", "0")
        self.cf.set("Actions", "show_help", "0")
        self.cf.set("Actions", "show_version", "0")

        self.cf.add_section("Keys")
        self.cf.set("Keys", "keys_directory", "")
        self.cf.set("Keys", "valid_keys_filename", "validkeys.txt")
        self.cf.set("Keys", "invalid_keys_filename", "invalidkeys.txt")

        with open(self.path, "w") as config_file:
            self.cf.write(config_file)

    def config_read(self):
        self.cf.read(self.path)

    def get(self, section, option):
        return self.cf.get(section, option)

    def set(self, section, option):
        self.cf.set(section, option)

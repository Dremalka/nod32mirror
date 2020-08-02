import config
import constants


class Key:
    def __init__(self):
        self.path = constants.PATH_SETTINGS
        self.cf = config.Nod32mirrorConfig(self.path)
        if not config.config_exists(self.path):
            self.cf.create_config()
        self.cf.config_read()

    def get_valid_key(self):
        ok, random_key = self.get_random_key()
        if not ok:
            print("Не удалось получить ключ")
            return False
        self.remove_invalid_keys()
        self.update_keys()
        ok, random_key = self.get_random_key()
        if not ok:
            print("Не удалось получить ключ")
            return False
        return True

    def get_random_key(self):
        print(self.cf.get("Keys", "valid_keys_filename"))

        pass

        return True, ""


    def remove_invalid_keys(self):
        pass


    def update_keys(self):
        pass

import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6972167779:AAGBweg8rJY4V6pYFiTjMz_3D8FzuYVwNZ4")

    APP_ID = int(os.environ.get("APP_ID", 24030976))

    API_HASH = os.environ.get("API_HASH", "aac06d2fddb5c3e0c1c8aa59a94c94aa)

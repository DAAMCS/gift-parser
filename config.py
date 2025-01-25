from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = env.list('ADMINS')

ADMINS = list(map(int, ADMINS))

API_ID = env.int('API_ID')
API_HASH = env.str('API_HASH')

GIFT_IDS = env.list('GIFT_IDS')
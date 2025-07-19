from starlette.config import Config

config = Config()
ENVIRONMENT = config('ENVIRONMENT', default='development')
PORT = config('PORT', cast=int, default=8000)
CORS_ORIGINS = config('CORS_ORIGINS', default='http://localhost:5173')
DB_FILE = config('DB_FILE', default='data.db')

_default_log_level = 'INFO' if ENVIRONMENT != 'development' else 'DEBUG'
LOG_LEVEL = config('LOG_LEVEL', default=_default_log_level)

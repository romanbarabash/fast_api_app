from environs import Env

env = Env()
env.read_env(verbose=True)

PROJECT_TITLE: str = "Job Board"
PROJECT_VERSION: str = "0.1"

POSTGRES_USER: str = env.str("POSTGRES_USER")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
POSTGRES_SERVER: str = env.str("POSTGRES_SERVER", "localhost")
POSTGRES_PORT: str = env.int("POSTGRES_PORT", 5432)  # default postgres port is 5432
POSTGRES_DB: str = env.str("POSTGRES_DB")
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# SECRET_KEY: str = env.str("SECRET_KEY")
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
# TEST_USER_EMAIL = "test@example.com"

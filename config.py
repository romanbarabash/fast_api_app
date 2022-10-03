from environs import Env

env = Env()
env.read_env(verbose=True)

PROJECT_TITLE: str = "Job Board"
PROJECT_VERSION: str = "0.1"

DATABASE_URL: str = env.str("DATABASE_URL")

SECRET_KEY: str = env.str("SECRET_KEY")
ALGORITHM: str = env.str("ALGORITHM")
TOKEN_EXPIRE_TIME: int = env.int("TOKEN_EXPIRE_TIME")
TEST_USER_EMAIL: str = env.str("TEST_USER_EMAIL")

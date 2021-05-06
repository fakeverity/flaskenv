from alembic import Config
from dotenv  import dotenv_values


# Initialize and import values from .ENV file
settings = dotenv_values(".env")

# Alembic environment configuration setup
alembic_cfg = Config()
alembic_cfg.set_main_option("sqlalchemy.url", ALCHEMY_URL);

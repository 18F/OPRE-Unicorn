DEBUG = True  # make sure DEBUG is off unless enabled explicitly otherwise

# pragma: allowlist secret
SQLALCHEMY_DATABASE_URI = (
    "postgresql+psycopg2://postgres:local_password@localhost:5432/postgres"  # pragma: allowlist secret
)
SQLALCHEMY_ECHO = False

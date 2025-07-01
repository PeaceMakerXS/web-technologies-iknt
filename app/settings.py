import os
from dotenv import load_dotenv
load_dotenv()


def get_db_url():
	return (f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@'
			f'{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}'
			f'/{os.getenv("DB_NAME")}')


class Config:
	SQLALCHEMY_DATABASE_URI = get_db_url()

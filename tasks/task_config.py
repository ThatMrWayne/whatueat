import os
#from dotenv import load_dotenv



#load_dotenv()
CACHE_REDIS_HOST = os.getenv("CACHE_REDIS_HOST")
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
MONGODB_URL=os.getenv("MONGODB_URL")
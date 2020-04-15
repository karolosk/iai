import logging
import settings

logging.basicConfig(level=settings.LOG_LEVEL,
            handlers=[
                logging.FileHandler(filename=settings.LOG_FILE),
                logging.StreamHandler()
            ],
            format=('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            )



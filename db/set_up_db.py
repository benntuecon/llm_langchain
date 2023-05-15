from .vector_store import get_collection, uuid_gen
from collector.get_user import get_user
from config import logger, Bcolors


user = get_user()
collection = get_collection()


def setup_db():
    logger.info(
        f"{Bcolors.BOLD}{Bcolors.HEADER}--- Setting up DB ---{Bcolors.ENDC}{Bcolors.ENDC}"
    )
    for url, texts in user.url_readme_texts_pair:
        logger.info(
            f"{Bcolors.HEADER} Adding {len(texts)} documents from {url}{Bcolors.ENDC}"
        )

        collection.add(
            documents=texts,
            metadatas=[{'url': url} for _ in texts],
            ids=[uuid_gen() for _ in texts]
        )

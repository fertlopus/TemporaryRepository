import pandas as pd
import logging
from typing import Generator, Iterable

logger = logging.getLogger(__name__)


def read_csv_in_chunks(file_path: str, chunk_size: int = 10000) -> Generator[pd.DataFrame, None, None]:
    """
    Reads a CSV file in chunks.

    Args:
        file_path (str): The path to the CSV file to read.
        chunk_size (int): The number of rows per chunk.

    Yields:
        DataFrame: A chunk of the pandas DataFrame.
    """
    try:
        logger.info(f"Reading CSV file in chunks from {file_path}")
        for chunk in pd.read_csv(file_path, chunksize = chunk_size):
            yield chunk
    except Exception as e:
        logger.error(f"Error reading CSV file in chunks: {e}")


def write_csv_in_chunks(df_iterator: Iterable[pd.DataFrame], file_path: str) -> None:
    """
    Writes chunks of pandas DataFrame to a CSV file.

    Args:
       df_iterator (Iterable[DataFrame]): An iterator that yields DataFrame chunks.
       file_path (str): The path to the CSV file to write.
    """
    try:
        logger.info(f"Writing CSV file in chunks to {file_path}")
        first_chunk = True
        for chunk in df_iterator:
            if first_chunk:
                chunk.to_csv(file_path, index = False, mode = "w")
                first_chunk = False
            else:
                chunk.to_csv(file_path, index = False, mode = "a", header = False)
    except Exception as e:
        logger.error(f"Error writing CSV file in chunks: {e}")

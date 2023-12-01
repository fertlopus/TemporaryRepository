import argparse
import os
import logging
import pandas as pd
from typing import Dict
from datetime import datetime
from src.scripts.converter import fetch_exchange_rates
from src.scripts.csv_builder import read_csv_in_chunks, write_csv_in_chunks


def process_chunk(chunk: pd.DataFrame, exchange_rates: Dict[str, float]):
    chunk["budget_local"] = chunk.apply(lambda row: row["budget_EUR"] * exchange_rates.get(row["local_currency"], 1),
                                        axis = 1)
    return chunk


def main(input_file: str, output_path: str) -> None:
    exchange_rates = fetch_exchange_rates()
    chunk_iterator = (process_chunk(chunk, exchange_rates) for chunk in read_csv_in_chunks(input_file))
    write_csv_in_chunks(chunk_iterator, output_path)


if __name__ == "__main__":
    os.makedirs("logs", exist_ok = True)

    log_filename = datetime.now().strftime("run_%d_%m_%y_%H_%M_%S.log")
    log_filepath = os.path.join('logs', log_filename)

    logging.basicConfig(level = logging.INFO,
                        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename = log_filepath,
                        filemode = 'w')

    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description = "Convert budget amounts in a CSV file from EUR to local currencies")
    parser.add_argument("input_file", help = "Path to the input CSV file.")
    parser.add_argument("output_file", help = "Path to the output CSV file.")
    args = parser.parse_args()

    logger.info("Starting the currency conversion process")
    main(args.input_file, args.output_file)
    logger.info("Currency conversion process completed")

from src.utils.all_utils import read_yaml
import argparse
import pandas as pd

def get_data(config_path):
    config = read_yaml(config_path)

    remote_data_path = config["data_source"]
    df = pd.read_csv(remote_data_path, sep=";")

    # save the dataset in the local directory 
    # create path to directory : artifacts/raw_local_dir/data.csv


if __name__=="__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)
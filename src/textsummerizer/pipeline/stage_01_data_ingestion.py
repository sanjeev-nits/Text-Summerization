from textsummerizer.config.configuration import ConfiggurationManager
from textsummerizer.components.data_ingestion import DataIngestion
from textsummerizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfiggurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

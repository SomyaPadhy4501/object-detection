import sys
import os
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.components.data_ingestion import DataIngestion


from signLanguage.entity.config_entity import (DataIngestionConfig)
from signLanguage.entity.artifacts_entity import (DataIngestionArtifact)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info(
                "Entered the staret data ingestion method of Training pipeline class" 
            )
            logging.info("Getting data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config= self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.inititate_data_ingestion()
            logging.info("Got data from URL")
            logging.info(
                "Exited the start data_ingestion method of Training pipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e , sys)


    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise SignException(e , sys)
                

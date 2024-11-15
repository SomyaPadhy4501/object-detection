import sys
import os
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_validation import DataValidation


from signLanguage.entity.config_entity import (DataIngestionConfig , ValidationConfig)
from signLanguage.entity.artifacts_entity import (DataIngestionArtifact , DataValidationArtifact)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = ValidationConfig()
    

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
        
    def start_data_validation(
            self, data_ingestion_artifact:DataIngestionArtifact
    )-> DataValidationArtifact:
        logging.info("Entered start_data_validation method of training pipeline")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact= data_ingestion_artifact,
                data_validation_config= self.data_validation_config
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed data validation")
            logging.info("Exited start_data_validation method of training pipeline")

            return data_validation_artifact
        
        except Exception as e:
            raise SignException(e , sys)



    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact= data_ingestion_artifact
            )

        except Exception as e:
            raise SignException(e , sys)
                

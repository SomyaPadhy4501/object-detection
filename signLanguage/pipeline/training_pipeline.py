import sys
import os
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_validation import DataValidation
from signLanguage.components.model_trainer import ModelTrainer


from signLanguage.entity.config_entity import (DataIngestionConfig , ValidationConfig , ModelTrainerConfig)
from signLanguage.entity.artifacts_entity import (DataIngestionArtifact , DataValidationArtifact , ModelTrainerArtifact)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = ValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()
    

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
        
    def start_model_training(self) -> ModelTrainerArtifact:
        try:
            model_trainer= ModelTrainer(
                model_trainer_config= self.model_trainer_config,
            )
            model_trainer_artifact= model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        
        except Exception as e:
            raise SignException(e , sys)




    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact= data_ingestion_artifact
            )

            if data_validation_artifact.validation_status == True:
                model_trainer_artifact = self.start_model_training()

            else:
                raise Exception("Data not in right format")

        except Exception as e:
            raise SignException(e , sys)
                

import sys
from signLanguage.configuration.s3_operations import S3Operation
from signLanguage.entity.artifacts_entity import (ModelPusherArtifacts , ModelTrainerArtifact)
from signLanguage.entity.config_entity import ModelPusherConfig
from signLanguage.exception import SignException
from signLanguage.logger import logging


class ModelPusher:
    def __init__(self , model_pusher_config: ModelPusherConfig , model_trainer_artifact: ModelTrainerArtifact , s3 : S3Operation):
        self.model_pusher_config = model_pusher_config
        self.model_trainer_artifacts = model_trainer_artifact
        self.s3 = s3
        

    
    def inititate_model_pusher(self) -> ModelPusherArtifacts:
        """
        Method Name : initiate_model_pusher

        Description : This method initiated model pusher

        Output      : Model pusher artifact
        """

        logging.info("Entered initiate model pusher method of ModelPusher class")
        try:
            self.s3.upload_file(
                self.s3.upload_file(
                    self.model_trainer_artifacts.trained_model_file_path,
                    self.model_pusher_config.S3_MODEL_KEY_PATH,
                    self.model_pusher_config.BUCKET_NAME,
                    remove= False,

                )
            )
            logging.info("Uploaded best model to S3 bucket")
            logging.info("Exited initiate model pusher method of ModelPusher class")

            model_pusher_artifact = ModelPusherArtifacts(
                bucket_name= self.model_pusher_config.BUCKET_NAME,
                s3_model_path=self.model_pusher_config.S3_MODEL_KEY_PATH
            )

            return model_pusher_artifact
        
        except Exception as e:
            raise SignException(e , sys) from e



import os
import sys
import shutil
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import ValidationConfig
from signLanguage.entity.artifacts_entity import (DataIngestionArtifact , DataValidationArtifact)



class DataValidation:
    def __init__(
        self,data_ingestion_artifact: DataIngestionArtifact, data_validation_config: ValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise SignException(e , sys)

    
    def validate_all_file_exsist(self) -> bool:
        try:
            validation_status = None
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir , exist_ok= True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir , exist_ok= True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            
            return validation_status
            
        except Exception as e:
            raise SignException(e , sys)

        
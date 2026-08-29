import sys

from src.exception import MyException
from src.logger import logging
from src.cloud_storage.aws_storage import SimpleStorageService
from src.entity.artifact_entity import ModelEvaluationArtifact, ModelPusherArtifact
from src.entity.config_entity import ModelPusherConfig
from src.entity.s3_estimator import proj1Estimator

class ModelPusher:
    def __init__(self, model_evaluation_artifact: ModelEvaluationArtifact,
                 model_pusher_config: ModelPusherConfig) :
        """
        : param model_evaluation_artifact : Output reference of data evalution artifact stage.
        : param model_pusher_config : configuration for model_pusher
        """
        self.s3 = SimpleStorageService()
        self.model_evaluation_artifact = model_evaluation_artifact
        self.model_pusher_config = model_pusher_config
        self.proj1_estimator = proj1Estimator(bucket_name=model_pusher_config.bucket_name,
                                              model_path=model_pusher_config.s3_model_key_path)

    def initate_model_pusher(self) -> ModelPusherArtifact:
        """
        Method Name : initate_model_pusher
        Description : This function is used to initate the all steps of model pusher

        Output      : Returns the model pusher artifact
        On Failure : Write an exception log and raise an exception
        """
        logging.info("Entered initate_model_pusher method of ModelPusher class.")
        try:
            print("----------------------------------------------------------------------------------------------")
            logging.info("Uploading artifacts folder to s3 bucket")

            logging.info("Uploading new model to s3 bucket.......")
            self.proj1_estimator.save_model(from_file=self.model_evaluation_artifact.trained_model_path)
            model_pusher_artifact = ModelPusherArtifact(bucket_name=self.model_pusher_config.bucket_name,
                                                        s3_model_path=self.model_pusher_config.s3_model_key_path)
            logging.info("Uploaded artifacts foldet to s3 bucket")
            logging.info(f"Model pusher artifact : [{model_pusher_artifact}]")
            logging.info("Exited initate_model_pusher method of ModelPusher class.")

            return model_pusher_artifact
        except Exception as e:
            raise MyException(e, sys) from e
import os
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging
from src.exception import CustomException


def run_training_pipeline():
    logging.info("Training pipeline started")
    try:
        ingestion = DataIngestion()
        train_path, test_path = ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")

        transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = transformation.initiate_data_transformation(train_path, test_path)
        logging.info("Data transformation completed")

        trainer = ModelTrainer()
        r2_score = trainer.initiate_model_trainer(train_arr, test_arr)
        logging.info(f"Model training completed. Best model R2 score: {r2_score}")

    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    run_training_pipeline()

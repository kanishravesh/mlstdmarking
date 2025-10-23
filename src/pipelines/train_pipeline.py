from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging

if __name__ == "__main__":
    logging.info("Training Pipeline Initiated")

    # Step 1: Data Ingestion
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()
    logging.info("Data Ingestion completed")

    # Step 2: Data Transformation
    transformation = DataTransformation()
    train_arr, test_arr, preprocessor_path = transformation.initiate_data_transformation(train_path, test_path)
    logging.info(f"Data Transformation completed. Preprocessor saved at: {preprocessor_path}")

    # Step 3: Model Training
    trainer = ModelTrainer()
    r2_square = trainer.initiate_model_trainer(train_arr, test_arr)
    logging.info(f"Model Training completed with R2 Score: {r2_square}")
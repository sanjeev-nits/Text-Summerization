from textsummerizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummerizer.logging import logger
from textsummerizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummerizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(f">>>>>> stage {STAGE_NAME} failed <<<<<<")


STAGE_NAME = "Data validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(f">>>>>> stage {STAGE_NAME} failed <<<<<<")
    raise e


STAGE_NAME = "Data tranformation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(f">>>>>> stage {STAGE_NAME} failed <<<<<<")
    raise e

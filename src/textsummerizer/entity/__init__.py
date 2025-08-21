from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: str
    data_path: str
    model_ckpt: str
    num_train_epochs: int 
    warmup_steps: int      
    weight_decay: float
    logging_steps: float

    per_device_train_batch_size : int
    per_device_eval_batch_size : int
    eval_strategy: str
    eval_steps: float      
    save_steps: float
    gradient_accumulation_steps: int
from datetime import datetime

from beanie import Document, PydanticObjectId


class Experiment(Document):
    name: str
    description: str
    publication_ids: list[str]
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

    experiment_type_id: PydanticObjectId
    dataset_id: str
    model_id: str
    metrics: list[str]

    save_logs: bool
    save_files: bool

    class Settings:
        name = "experiments"

import json
from datetime import datetime

from beanie import Document, PydanticObjectId

from app.config import LOGS_FILENAME, METRICS_FILENAME, settings
from app.schemas.experiment_run import ExperimentRunDetails
from app.schemas.states import RunState


class ExperimentRun(Document):
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    run_number: int
    state: RunState = RunState.CREATED
    experiment_id: PydanticObjectId

    class Settings:
        name = "experimentRuns"
        indexes = ["experiment_id"]

    def update_state(self, state: RunState) -> None:
        self.state = state
        self.updated_at = datetime.utcnow()

    def map_to_response(self) -> ExperimentRunDetails:
        run_path = settings.get_experiment_run_output_path(self.id)
        m_path = run_path / METRICS_FILENAME
        log_path = run_path / LOGS_FILENAME

        metrics = {}
        if m_path.exists():
            with open(m_path) as f:
                metrics = json.load(f)
        logs = log_path.read_text() if log_path.is_file() else ""

        return ExperimentRunDetails(**self.dict(), metrics=metrics, logs=logs)

    def create_following_run(self):
        return ExperimentRun(
            experiment_id=self.experiment_id,
            run_number=self.run_number + 1,
        )
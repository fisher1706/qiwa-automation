import config
from src.database.client.db_client import DBClient
from src.database.models.laborer_sso_tables_description import Activities


class ActivityRequest:
    def __init__(self):
        self.db_client = DBClient(db_url=config.settings.sso_auth_db_url)
        self.session = self.db_client.set_db_session

    def delete_activities_request(self, national_id: str) -> None:
        activities_data = (
            self.session.query(Activities).filter(Activities.entity_value == national_id).all()
        )
        for activities in activities_data:
            self.session.delete(activities)
            self.session.commit()

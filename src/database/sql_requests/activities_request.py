from src.database.client.db_client import DBClient
from src.database.models.db_tables_description import Activities


class ActivityRequest:
    session = DBClient().set_auth_db_session()

    def delete_activities_request(self, national_id: str) -> None:
        activities_data = (
            self.session.query(Activities).filter(Activities.entity_value == national_id).all()
        )
        for activities in activities_data:
            self.session.delete(activities)
            self.session.commit()

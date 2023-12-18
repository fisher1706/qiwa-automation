import config
from src.database.client.db_client import DBClient
from src.database.models.laborer_sso_tables_description import SecurityQuestions


class SecurityQuestionsRequest:
    session = DBClient(db_url=config.settings.sso_auth_db_url).set_db_session

    def delete_security_question_request(self, account_id: str) -> None:
        security_question_data = (
            self.session.query(SecurityQuestions)
            .filter(SecurityQuestions.account_id == account_id)
            .all()
        )
        for question in security_question_data:
            self.session.delete(question)
            self.session.commit()

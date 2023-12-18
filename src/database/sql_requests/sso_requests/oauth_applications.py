from sqlalchemy import DateTime

import config
from src.database.client.db_client import DBClient
from src.database.models.laborer_sso_tables_description import (
    OauthApplications,
    OauthGrants,
)


class AppRequest:
    session = DBClient(db_url=config.settings.sso_auth_db_url).set_db_session

    def create_applications_request(self, account_id: str, application_add):
        application_add = OauthApplications(
            account_id=account_id,
            name=application_add.app_name,
            description=application_add.app_description,
            homepage_url=application_add.url,
            redirect_uri=application_add.uri,
            client_id=application_add.client_id,
            client_secret=application_add.client_secret,
            permissions=application_add.permissions,
            scopes=application_add.scopes,
            main=application_add.main,
        )
        self.session.add(application_add)
        self.session.commit()

    def get_application_id_request(self, account_id: str, name: str) -> str:
        application_data = (
            self.session.query(OauthApplications)
            .filter(OauthApplications.account_id == account_id, OauthApplications.name == name)
            .first()
        )
        return application_data.id

    def expired_temporary_token_request(
        self, temporary_token: str, expired_time: DateTime
    ) -> None:
        oauth_grant_data = (
            self.session.query(OauthGrants).filter(OauthGrants.code == temporary_token).first()
        )
        oauth_grant_data.expires_in = expired_time
        self.session.commit()

    def delete_oauth_grants_data_request(self, account_id: str):
        oauth_grant_data = (
            self.session.query(OauthGrants).filter(OauthGrants.account_id == account_id).all()
        )
        for oauth_grant in oauth_grant_data:
            self.session.delete(oauth_grant)
            self.session.commit()

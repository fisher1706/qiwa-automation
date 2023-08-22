import allure

from src.api.models.mock_mlsd.ibm.getsaudicert import GetSaudiCertificateRsBody
from src.api.models.mock_mlsd.ibm.root import IBMResponseData
from utils.assertion import assert_that


class SaudizationApiActions:
    @allure.step
    def assert_error(self, response: dict, expected: IBMResponseData) -> None:
        expected_status = expected.Header.ResponseStatus
        assert_that(response["data"]).has("type")("error")
        (
            assert_that(response["data"]["attributes"])
            .has("id")(1)
            .has("code")(expected_status.Code)
            .has("ar-message")(expected_status.ArabicMsg)
            .has("en-message")(expected_status.EnglishMsg)
        )

    @allure.step
    def assert_certificate_values(
        self, response: dict, expected: IBMResponseData[GetSaudiCertificateRsBody]
    ) -> None:
        expected = expected.Body.SCDetailsList.SCDetailsItem
        assert_that(response).has("saudi_certificate_number")(expected.CertificateNumber).has(
            "national_unified_number"
        )(None).has("labor_office_id")(expected.LaborOfficeId).has("sequence_number")(
            expected.SequenceNumber
        ).has(
            "saudi_cert_status_id"
        )(
            expected.SaudiCertStatus.SaudiCertStatusId
        ).has(
            "saudi_cert_status_en"
        )(
            expected.SaudiCertStatus.SaudiCertStatusEn
        ).has(
            "saudi_cert_status_ar"
        )(
            expected.SaudiCertStatus.SaudiCertStatusAr
        ).has(
            "establishment_name"
        )(
            expected.EstablishmentName
        ).has(
            "cr_number"
        )(
            expected.CRNumber
        ).has(
            "cert_issue_date"
        )(
            expected.SaudiCertIssueDate
        ).has(
            "cert_expiry_date"
        )(
            expected.SaudiCertExpiryDate
        )
        if expected.RenewalStartDate:
            assert_that(response).has("renew_start_date")(expected.RenewalStartDate)
        else:
            assert_that(response).has("renew_start_date")(None)
        # TODO:
        #  .has("requester-personal-number")
        #  .has("requester-user-id")
        #  .has("company-id")

    @allure.step
    def assert_extended_certificate_values(
        self, response: dict, expected: IBMResponseData[GetSaudiCertificateRsBody]
    ) -> None:
        expected = expected.Body.SCDetailsList.SCDetailsItem
        assert_that(response["data"]).has("type")("saudization-certificate")
        assert_that(response["data"]["attributes"]).has("saudi-certificate-number")(
            expected.CertificateNumber
        ).has("national-unified-number")(None).has("labor-office-id")(expected.LaborOfficeId).has(
            "sequence-number"
        )(
            expected.SequenceNumber
        ).has(
            "saudi-cert-status-id"
        )(
            expected.SaudiCertStatus.SaudiCertStatusId
        ).has(
            "saudi-cert-status-en"
        )(
            expected.SaudiCertStatus.SaudiCertStatusEn
        ).has(
            "saudi-cert-status-ar"
        )(
            expected.SaudiCertStatus.SaudiCertStatusAr
        ).has(
            "establishment-name"
        )(
            expected.EstablishmentName
        ).has(
            "cr-number"
        )(
            expected.CRNumber
        ).has(
            "cert-issue-date"
        )(
            expected.SaudiCertIssueDate
        ).has(
            "cert-expiry-date"
        )(
            expected.SaudiCertExpiryDate
        )
        if expected.RenewalStartDate:
            assert_that(response["data"]["attributes"]).has("renew-start-date")(
                expected.RenewalStartDate
            )
        else:
            assert_that(response["data"]["attributes"]).has("renew-start-date")(None)

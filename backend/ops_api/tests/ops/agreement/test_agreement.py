import pytest
from models import ContractAgreement, GrantAgreement
from models.cans import Agreement
from sqlalchemy import func, select


@pytest.mark.usefixtures("app_ctx")
def test_agreement_retrieve(loaded_db):
    stmt = select(Agreement).where(Agreement.id == 1)
    agreement = loaded_db.scalar(stmt)

    assert agreement is not None
    assert agreement.number == "AGR0001"
    assert agreement.name == "Contract #1: African American Child and Family Research Center"
    assert agreement.id == 1
    assert agreement.agreement_type == "CONTRACT"


@pytest.mark.usefixtures("app_ctx")
def test_agreements_get_all(auth_client, loaded_db):
    stmt = select(func.count()).select_from(Agreement)
    count = loaded_db.scalar(stmt)
    assert count == 6

    response = auth_client.get("/api/v1/agreements/")
    assert response.status_code == 200
    assert len(response.json) == count


@pytest.mark.usefixtures("app_ctx")
def test_agreements_get_by_id(auth_client, loaded_db):
    response = auth_client.get("/api/v1/agreements/1")
    assert response.status_code == 200
    assert response.json["name"] == "Contract #1: African American Child and Family Research Center"


@pytest.mark.usefixtures("app_ctx")
def test_agreements_get_by_id_404(auth_client, loaded_db):
    response = auth_client.get("/api/v1/agreements/1000")
    assert response.status_code == 404


@pytest.mark.usefixtures("app_ctx")
def test_agreements_serialization(auth_client, loaded_db):
    response = auth_client.get("/api/v1/agreements/1")
    assert response.status_code == 200

    # Remove extra keys that make test flaky or noisy
    json_to_compare = response.json  # response.json seems to be immutable
    del json_to_compare["created_on"]
    del json_to_compare["updated_on"]
    del json_to_compare["budget_line_items"]
    del json_to_compare["research_project"]

    assert json_to_compare == {
        "agreement_reason": "NEW_REQ",
        "agreement_type": "CONTRACT",
        "contract_number": "CT00XX1",
        "contract_type": "RESEARCH",
        "created_by": None,
        "delivered_status": False,
        "description": "",
        "id": 1,
        "incumbent": "",
        "name": "Contract #1: African American Child and Family Research Center",
        "number": "AGR0001",
        "procurement_shop": None,
        "product_service_code": 1,
        "project_officer": None,
        "research_project_id": 1,
        "support_contacts": [],
        "team_members": [],
        "vendor": "Vendor 1",
    }


@pytest.mark.usefixtures("app_ctx")
def test_agreements_with_research_project_empty(auth_client, loaded_db):
    response = auth_client.get("/api/v1/agreements/?research_project_id=")
    assert response.status_code == 200
    assert len(response.json) == 6


@pytest.mark.usefixtures("app_ctx")
def test_agreements_with_research_project_found(auth_client, loaded_db):
    response = auth_client.get("/api/v1/agreements/?research_project_id=1")
    assert response.status_code == 200
    assert len(response.json) == 2

    assert response.json[0]["id"] == 1
    assert response.json[1]["id"] == 2


@pytest.mark.usefixtures("app_ctx")
def test_agreements_with_research_project_not_found(auth_client, loaded_db):
    response = auth_client.get("/api/v1/agreements/?research_project_id=1000")
    assert response.status_code == 200
    assert len(response.json) == 0


def test_agreement_search(auth_client, loaded_db):
    response = auth_client.get("/api/v1/agreements/?search=")

    assert response.status_code == 200
    assert len(response.json) == 0

    response = auth_client.get("/api/v1/agreements/?search=contract")

    assert response.status_code == 200
    assert len(response.json) == 2

    response = auth_client.get("/api/v1/agreements/?search=fcl")

    assert response.status_code == 200
    assert len(response.json) == 2


@pytest.mark.usefixtures("app_ctx")
def test_agreements_get_by_id_auth(client, loaded_db):
    response = client.get("/api/v1/agreements/1")
    assert response.status_code == 401


@pytest.mark.usefixtures("app_ctx")
def test_agreements_auth(client, loaded_db):
    response = client.get("/api/v1/agreements/")
    assert response.status_code == 401


@pytest.mark.usefixtures("app_ctx")
def test_agreement_as_contract_has_contract_fields(loaded_db):
    stmt = select(Agreement).where(Agreement.id == 1)
    agreement = loaded_db.scalar(stmt)

    assert agreement.agreement_type == "CONTRACT"
    assert agreement.contract_number == "CT00XX1"


@pytest.mark.usefixtures("app_ctx")
def test_agreement_create_contract_agreement(loaded_db):
    contract_agreement = ContractAgreement(
        agreement_id=1,
        contract_number="CT0002",
        contract_type="Research",
        product_service_code=2,
    )
    loaded_db.add(contract_agreement)
    loaded_db.commit()

    stmt = select(Agreement).where(Agreement.id == 1)
    agreement = loaded_db.scalar(stmt)

    assert agreement.contract_agreement.contract_number == "CT0002"
    assert agreement.contract_agreement.contract_type == "Research"
    assert agreement.contract_agreement.product_service_code == 2


@pytest.mark.usefixtures("app_ctx")
def test_agreement_create_grant_agreement(loaded_db):
    grant_agreement = GrantAgreement(
        agreement_id=2,
        grant_number="GR0002",
        funding_source="NIH",
    )
    loaded_db.add(grant_agreement)
    loaded_db.commit()

    stmt = select(Agreement).where(Agreement.id == 2)
    agreement = loaded_db.scalar(stmt)

    assert agreement.grant_agreement.grant_number == "GR0002"
    assert agreement.grant_agreement.funding_source == "NIH"


@pytest.mark.usefixtures("app_ctx")
def test_agreements_patch_by_id(auth_client, loaded_db):
    response = auth_client.patch(
        "/api/v1/agreements/1",
        json={
            "name": "New Contract Name",
            "description": "New Contract Description",
            "support_contacts": [{"name": "Support Name", "email": "support@test.com"}],
        },
    )
    assert response.status_code == 200

    stmt = select(Agreement).where(Agreement.id == 1)
    agreement = loaded_db.scalar(stmt)

    assert agreement.name == "New Contract Name"
    assert agreement.description == "New Contract Description"
    assert len(agreement.support_contacts) == 1
    assert agreement.support_contacts[0].name == "Support Name"
    assert agreement.support_contacts[0].email == "support@test.com"


@pytest.mark.usefixtures("app_ctx")
def test_agreements_delete_by_id(auth_client, loaded_db):
    response = auth_client.delete("/api/v1/agreements/1")
    assert response.status_code == 204

    stmt = select(Agreement).where(Agreement.id == 1)
    agreement = loaded_db.scalar(stmt)

    assert agreement is None

from fastapi.testclient import TestClient
from main import app
from security import DUMMY_TOKEN

# Initialize the test client
client = TestClient(app)

def test_missing_auth_token():
    """Test that a valid request returns a 200 OK and a markdown response."""
    response = client.get("/analyze/technology")
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized! Please provide a guest token in the X-API-Key Header!"}


def test_successful_auth_and_response():
    """Tests if a valid request returns status code 200 OK and a markdown reponse."""
    # Note: We use a very obscure sector here so its fast and doesn't eat up the Gemini quota heavily during testing
    headers = {"X-API-Key": DUMMY_TOKEN}
    response = client.get("/analyze/handicrafts", headers=headers)
    assert response.status_code == 200

    # Checking if the reponse is plain text or markdown
    assert "text/markdown" in response.headers["content-type"]

    # Checking that our new runtime footer is somewhere in the text
    assert "Report generated in" in response.text
def test_check_connection(local_fastapi_client) -> None:
    response = local_fastapi_client.get("/check")
    assert response.status_code == 200

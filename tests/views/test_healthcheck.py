def test_heath(client):
    assert client.get("/api/health").content == b"ok"

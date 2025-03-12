# Accela SDK

Lightweight Python client for the [Accela API](https://developer.accela.com/).

## Usage

### Authentication

This SDK supports creating a token with the [Password Credential Login](https://developer.accela.com/docs/construct-passwordCredentialLogin.html) flow. To make an access token, you'll need:

- An Accela developer app
- A citizen account with an Accela agency

```python
from accela import get_access_token, AccelaClient

# Get an access token
token = get_access_token(
    client_id="your_client_id",
    client_secret="your_client_secret",
    username="your_username",
    password="your_password",
    agency_name="AGENCY",
    environment="PROD",
    grant_type="password",
    scope="records",
    id_provider="citizen"
)

# Create a client
client = AccelaClient(
    access_token=token.access_token,
    agency="AGENCY",
    environment="PROD"
)
```

### Records

```python
# List records
records = client.records.list(limit=10)

# Iterate through records
for record in records:
    print(f"Record ID: {record.id}, Type: {record.type}")

# Paginate through all records
for record in records.auto_paging_iter():
    print(f"Record ID: {record.id}, Type: {record.type}")

# Get a specific record
record = client.records.retrieve("RECORD-123")
```

### Record Addresses

```python
# Get addresses for a record
addresses = client.record_addresses.list("RECORD-123")

# Iterate through addresses
for address in addresses:
    ...
```

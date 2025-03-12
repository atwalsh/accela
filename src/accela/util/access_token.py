from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

import requests


@dataclass(kw_only=True)
class AccelaAccessToken:
    access_token: str
    refresh_token: str
    expires_at: datetime
    scopes: list[str]


def get_access_token(
    *,
    client_id: str,
    client_secret: str,
    username: str,
    password: str,
    agency_name: str,
    environment: str,
    grant_type: str,
    scope: str,
    id_provider: str,
) -> AccelaAccessToken:
    before_req_time = datetime.now(tz=timezone.utc)
    r = requests.post(
        "https://apis.accela.com/oauth2/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "username": username,
            "password": password,
            "agency_name": agency_name,
            "environment": environment,
            "grant_type": grant_type,
            "scope": scope,
            "id_provider": id_provider,
        },
    )
    r.raise_for_status()

    data = r.json()
    return AccelaAccessToken(
        access_token=data["access_token"],
        refresh_token=data["refresh_token"],
        expires_at=before_req_time + timedelta(seconds=data["expires_in"]),
        scopes=data["scope"].split(" "),
    )

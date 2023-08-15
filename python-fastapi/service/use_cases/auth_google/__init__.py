from .business import Business


def compose(
    google_client_id: str,
) -> Business:
    return Business(google_client_id)

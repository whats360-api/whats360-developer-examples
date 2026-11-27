"""Maps error codes from user-supplied, unverified notes to suggested actions. Pure function, easy to unit test. Not confirmed against the live API."""
ACTIONS = {
    400: "Unverified: fix the request: a parameter is missing or malformed.",
    401: "Unverified: token is invalid or expired. Get a fresh token from the dashboard.",
    403: "Unverified: a message or request limit was reached. Check your plan limits.",
    404: "Unverified: device (instance_id) not found. List devices to find the right ID.",
    463: "Recipient-related per unverified notes. Do not message the number to work around the error; confirm the cause in the dashboard or with support.",
    500: "Unverified: server error. Retry later with backoff.",
}

def explain(status: int) -> str:
    return ACTIONS.get(status, f"Undocumented status {status}. Check the dashboard and contact support.")

def retryable(status: int) -> bool:
    return status == 500

if __name__ == "__main__":
    for code in (400, 401, 403, 404, 463, 500, 418):
        print(code, explain(code))

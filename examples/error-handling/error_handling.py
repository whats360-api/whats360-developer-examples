"""Maps documented Whats360 error codes to actions. Pure function, easy to unit test."""
ACTIONS = {
    400: "Fix the request: a parameter is missing or malformed.",
    401: "Token is invalid or expired. Get a fresh token from the dashboard.",
    403: "A message or request limit was reached. Check your plan limits.",
    404: "Device (instance_id) not found. List devices to find the right ID.",
    463: "Recipient-related per unverified notes. Do not message the number to work around the error; confirm the cause in the dashboard or with support.",
    500: "Server error. Retry later with backoff.",
}

def explain(status: int) -> str:
    return ACTIONS.get(status, f"Undocumented status {status}. Check the dashboard and contact support.")

def retryable(status: int) -> bool:
    return status == 500

if __name__ == "__main__":
    for code in (400, 401, 403, 404, 463, 500, 418):
        print(code, explain(code))

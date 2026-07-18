import sys

# OAuth 2.0 roles (RFC 6749 §1.1):
# Resource Owner, Client, Authorization Server, Resource Server
ROLES = {
    "user grants access": "RESOURCE_OWNER",
    "third-party app": "CLIENT",
    "issues tokens": "AUTHORIZATION_SERVER",
    "hosts protected resources": "RESOURCE_SERVER",
    "validates tokens": "RESOURCE_SERVER",
    "redirects to login": "CLIENT",
}

for raw in sys.stdin:
    line = raw.rstrip("\n").strip().lower()
    if not line: continue
    for k, v in ROLES.items():
        if k in line:
            print(v); break
    else:
        print("UNKNOWN")



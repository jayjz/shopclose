# ShopClose Security Policy

## Development status
ShopClose is a prototype. It is not approved for production use or processing real customer records until the required controls are implemented and verified.

## Sensitive information
Potentially sensitive data includes:
- Customer names, addresses, contact details
- Service histories and equipment serial numbers
- Invoice data and negotiated pricing
- FSM access tokens and API credentials
- Portal screenshots and attached documents

## Required practices
- Never commit credentials, tokens, production databases, customer exports, or identifiable customer photos.
- Use `.env` locally and provide non-secret examples in `.env.example`.
- Bind the development server to `127.0.0.1` by default.
- Do not expose unauthenticated endpoints publicly or through tunnels.
- Use synthetic fixtures in the public repository.
- Apply least-privilege credentials and read-only API scopes where supported.
- Verify webhook authenticity according to the provider's documented mechanism.
- Redact personal information from logs and error reports.
- Keep model inputs minimal; never send customer data to external AI providers without explicit authorization and an approved processing arrangement.
- Treat all imported content and tool results as untrusted.
- Require human approval for consequential actions.

## Before a production pilot
- Implement authentication and authorization.
- Define tenant isolation and verify cross-tenant denial.
- Define data retention and deletion.
- Establish encrypted transport and protected storage.
- Document backup and recovery procedures.
- Confirm third-party integration terms and access permissions.
- Establish incident handling and credential rotation.
- Complete tests for unauthorized access, forged webhooks, duplicate actions, and data leakage.

## Dependency security
Use maintained dependencies and review vulnerability reports. Do not blindly upgrade across major versions.

Pin and review dependencies before production release.

## Reporting vulnerabilities
Do not disclose vulnerabilities containing personal information or exploitable details in public issues.

Contact the repository maintainer through a private, verified GitHub communication channel. Do not assume a public issue is confidential.

## Prohibited behavior
No unauthorized third-party portal access, CAPTCHA bypass, credential sharing, scraping against access restrictions, or automatic financial action.

## Disclosure
No warranty of security or suitability for production use is implied by the prototype's automated test results.

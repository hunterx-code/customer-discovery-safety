# Safe Approval Packet

ACTION: send one email
CHANNEL: email
ACCOUNT_OR_IDENTITY: founder@example.com
TARGET: ops-lead@example.com
SUBJECT: Customer-discovery question
BODY:
BEGIN_BODY
Hi,

I am doing early customer-discovery work on a workflow tool and trying to understand how teams currently review external data before analysis.

Would you be open to a 10-minute conversation about who usually owns that readiness check? I am not selling anything and I am not asking for private customer data.

If you are not the right person, a pointer to the right role or public resource is completely fine.
END_BODY

ATTACHMENTS_OR_LINKS: none
PURPOSE: Test whether this route can produce one current-behavior interview.
NOT_AUTHORIZED: follow-ups, calls, attachments, links, public posts
PRECHECKS: source verified; duplicate checked; account/identity checked; body reviewed; attachment/link state checked; stop words checked
STOP_CONDITIONS: stop if the user hesitates, changes the target/body/account, or asks to wait
APPROVAL_PHRASE: Send this exact email with no attachments

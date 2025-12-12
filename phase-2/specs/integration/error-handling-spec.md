# Error Handling Integration Spec

Mapping:
- validation_error -> show inline field errors if available else toast
- unauthorized -> logout & redirect to /login, toast "Session expired"
- forbidden -> toast "Access denied"
- not_found -> toast "Not found"
- conflict -> inline or toast "Conflict"
- server_error -> toast "Something went wrong"

UI must present friendly messages while retaining machine code in dev logs

# Synthetic authorization SDK

This test library exports requireTenantAccess(actor, tenantId). It validates tenant boundaries for the invoice API at https://github.com/gatsby003/security-autolink-firstscan-api. The API calls this function before returning dummy invoices. Review changes to this shared authorization function together with its caller in the API. No real customer data or credentials.

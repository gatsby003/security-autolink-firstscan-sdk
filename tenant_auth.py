def require_tenant_access(actor, tenant_id):
    if actor is None or actor.get("tenant_id") != tenant_id:
        raise PermissionError("Forbidden")
    return True

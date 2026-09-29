export function requireTenantAccess(actor, tenantId) {
  if (!actor || actor.tenantId !== tenantId) throw new Error("Forbidden");
  return true;
}

# Synthetic authorization SDK

JavaScript index.js and Python tenant_auth.py implement the same tenant authorization check. The API at https://github.com/gatsby003/security-autolink-firstscan-api imports require_tenant_access from this Python package and calls it before returning dummy invoice data. Security analysis of the API needs this authorization implementation. This library has no network service or real credentials. All data is synthetic.

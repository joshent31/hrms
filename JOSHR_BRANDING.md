# JOSHR branding — mergify/bp/version-15-hotfix/pr-4423

## Compatibility

Branding base: `6dc60e376afb2ce78dda7c6e1a2652875789e192`. HRMS version: **15.33.2**. This change preserves this branch's existing business logic, dependencies, migrations and app routes. It does not upgrade or downgrade HRMS. Use a matching Frappe/ERPNext release; a development or backport branch is not automatically suitable for production.

For Frappe/ERPNext v15 use the `version-15` or `joshr-version-15` branch. Never install a develop/v16 branch on a v15 bench. For an already partially migrated database, first test recovery from a verified pre-migration backup on an isolated bench.

## Branding

JOSHR by JOSHENT Technology uses the supplied J symbol, navy #12293A, brass #E8C27A and ivory #F2EFE9. Interfaces present on this branch are branded; older branches do not gain new apps or interfaces. Upstream attribution and GPL licensing remain intact.

## Apply on a compatible staging bench

After backing up and updating the app source:

```sh
bench build --app hrms
bench --site YOUR_SITE migrate
bench --site YOUR_SITE execute hrms.branding.apply_branding
bench --site YOUR_SITE clear-cache
bench restart
```

The branding command changes shared Navbar and Website Settings. Existing PWA installations may need reinstalling to refresh OS-cached branding. Verify login, Desk, dark mode, mobile/roster where available, and HR/payroll workflows before production. Static validation does not replace full bench testing.

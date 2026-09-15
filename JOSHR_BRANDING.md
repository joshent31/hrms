# JOSHR branding

JOSHR by JOSHENT Technology is based on Frappe HR. Original copyright, author credits, GPL license, API paths, DocTypes, database schemas and business logic are preserved.

## Identity

The supplied `joshent_logo_sheet.svg` is the source of the J symbol and palette: navy #12293A, deep navy #0B1A24, brass #E8C27A / #C99B4A, ivory #F2EFE9. JOSHR is the product name. Dark navy primary buttons use white text; brass is an accent.

## Deploy in an existing bench

Back up your site, check out this branding branch in `apps/hrms`, and run:

```sh
bench build --app hrms
bench --site YOUR_SITE migrate
bench --site YOUR_SITE execute hrms.branding.apply_branding
bench --site YOUR_SITE clear-cache
bench restart
```

The branding command sets the shared site logo and website identity. To adjust these manually, set **Navbar Settings → App Logo** to `/assets/hrms/images/joshr-logo.svg`. In **Website Settings**, set App Name to JOSHR and the banner image, splash image and favicon to the JOSHR asset as appropriate. Explicit site settings can override application defaults. These settings affect the shared Frappe site, including other installed apps.

Reinstall an existing mobile PWA if the OS retains its old name or icon. The app URL remains `/hrms`; roster remains `/hr`.

## Review

Check Desk navigation, login including SSO/password reset, mobile login and installation, roster, job openings, keyboard focus, narrow screens and dark mode on a staging site. Historical screenshots and upstream documentation retain upstream branding. GitHub organization/avatar and repository social preview are account settings rather than code assets.

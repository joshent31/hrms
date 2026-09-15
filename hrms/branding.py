"""Apply JOSHR site identity without changing HR or payroll records."""

import frappe


def apply_branding():
	logo = "/assets/hrms/images/joshr-logo.svg"
	for doctype, values in {
		"Navbar Settings": {"app_logo": logo},
		"Website Settings": {
			"app_name": "JOSHR",
			"banner_image": logo,
			"splash_image": logo,
			"favicon": logo,
		},
	}.items():
		meta = frappe.get_meta(doctype)
		for field, value in values.items():
			if meta.has_field(field):
				frappe.db.set_single_value(doctype, field, value)
	frappe.clear_cache()

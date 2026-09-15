<div align="center">
  <img src=".github/joshr-logo.svg" width="96" height="96" alt="JOSHR logo" />
  <h1>JOSHR</h1>
  <p>HR and Payroll by JOSHENT Technology</p>
</div>

JOSHR is a branded distribution of [Frappe HR](https://github.com/frappe/hrms), with JOSHENT's navy and brass visual identity across Desk, employee self-service, and roster. It retains the upstream HR and payroll functionality and the internal `hrms` app name.

**Compatibility:** this branch is based on HRMS v15.64.0 and targets Frappe/ERPNext v15. Do not use the develop-based joshr-branding branch on a v15 bench.

See [branding and deployment](JOSHR_BRANDING.md) for installation steps and scope.

## Key Features

- Employee Management
- Employee Lifecycle
- Leave and Attendance
- Shift Management
- Expense Claims and Advances
- Hiring
- Performance Management
- Fleet Management
- Training
- Payroll
- Taxation
- Compensation
- Analytics

## Installation

### Manual Installation

1. [Install bench](https://github.com/frappe/bench).
2. [Install ERPNext](https://github.com/frappe/erpnext#installation).
3. Once ERPNext is installed, add the hrms app to your bench by running

	```sh
	$ bench get-app --branch joshr-version-15 https://github.com/joshent31/hrms.git
	```
4. After that, you can install the hrms app on the required site by running
	```sh
	$ bench --site sitename install-app hrms
	```


## Learning and Community

1. [Documentation](https://docs.frappe.io/hr) - Extensive documentation for Frappe HR.
2. [User Forum](https://discuss.erpnext.com/) - Engage with the community of ERPNext users and service providers.
3. [Telegram Group](https://t.me/frappehr) - Get instant help from the community of users.

## Contribute

1. [Issue Guidelines](https://github.com/frappe/erpnext/wiki/Issue-Guidelines) - [Create an issue](https://github.com/frappe/hrms/issues/new)
1. [Contribution Guidelines](https://github.com/frappe/erpnext/wiki/Contribution-Guidelines)

## License

GNU GPL V3. (See [license.txt](license.txt) for more information).

The HR code is licensed as GNU General Public License (v3) and the copyright is owned by Frappe Technologies Pvt Ltd (Frappe) and Contributors.

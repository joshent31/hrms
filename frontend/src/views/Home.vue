<template>
	<BaseLayout>
		<template #body>
			<div class="joshr-home">
				<div class="joshr-home-heading">
					<p class="joshr-eyebrow">{{ __("YOUR WORKDAY") }}</p>
					<h1>{{ __("Complete HRMS, ready for every workday.") }}</h1>
				</div>
				<CheckInPanel />
				<QuickLinks :items="quickLinks" :title="__('Core HRMS')" />
				<QuickLinks :items="reportLinks" :title="__('Reports & Compliance')" />
				<RequestPanel />
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { inject, markRaw } from "vue"

import CheckInPanel from "@/components/CheckInPanel.vue"
import QuickLinks from "@/components/QuickLinks.vue"
import BaseLayout from "@/components/BaseLayout.vue"
import RequestPanel from "@/components/RequestPanel.vue"
import AttendanceIcon from "@/components/icons/AttendanceIcon.vue"
import ShiftIcon from "@/components/icons/ShiftIcon.vue"
import LeaveIcon from "@/components/icons/LeaveIcon.vue"
import ExpenseIcon from "@/components/icons/ExpenseIcon.vue"
import EmployeeAdvanceIcon from "@/components/icons/EmployeeAdvanceIcon.vue"
import SalaryIcon from "@/components/icons/SalaryIcon.vue"

const __ = inject("$translate")

const quickLinks = [
	{
		icon: markRaw(AttendanceIcon),
		title: __("Attendance & Regularisation"),
		description: __("Checkins, requests, and corrections"),
		route: "AttendanceDashboard",
	},
	{
		icon: markRaw(ShiftIcon),
		title: __("On-Duty Management"),
		description: __("Use attendance request with On Duty"),
		route: "AttendanceRequestFormView",
	},
	{
		icon: markRaw(LeaveIcon),
		title: __("Leave & Permission"),
		description: __("Leave, permission, and holidays"),
		route: "LeavesDashboard",
	},
	{
		icon: markRaw(ExpenseIcon),
		title: __("Claim an Expense"),
		route: "ExpenseClaimFormView",
	},
	{
		icon: markRaw(EmployeeAdvanceIcon),
		title: __("Request an Advance"),
		route: "EmployeeAdvanceFormView",
	},
	{
		icon: markRaw(SalaryIcon),
		title: __("Payroll & Salary"),
		description: __("Salary slips and payroll history"),
		route: "SalarySlipsDashboard",
	},
]

const reportLinks = [
	{
		icon: markRaw(AttendanceIcon),
		title: __("Attendance Reports"),
		description: __("Monthly and shift attendance"),
		href: "/app/query-report/Monthly%20Attendance%20Sheet",
	},
	{
		icon: markRaw(ShiftIcon),
		title: __("40-Hour Weekly Tracking"),
		description: __("Standard hours utilization"),
		href: "/app/query-report/Employee%20Hours%20Utilization%20Based%20On%20Timesheet",
	},
	{
		icon: markRaw(SalaryIcon),
		title: __("Payroll Reports"),
		description: __("Salary register and payments"),
		href: "/app/query-report/Salary%20Register",
	},
	{
		icon: markRaw(EmployeeAdvanceIcon),
		title: __("MIS / HR Reports"),
		description: __("HR analytics and scheduled reports"),
		href: "/app/hr",
	},
]
</script>

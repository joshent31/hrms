<template>
	<ion-tab-bar
		slot="bottom"
		class="joshr-tab-bar"
	>
		<ion-tab-button
			v-for="item in tabItems"
			:key="item.title"
			:tab="item.title"
			:href="item.route"
			:class="[
				'joshr-tab',
				route.path === item.route
					? 'joshr-tab-active'
					: 'joshr-tab-idle',
			]"
		>
			<span class="joshr-tab-icon"><component :is="item.icon" class="h-5 w-5" aria-hidden="true" /></span>
			<div>{{ item.title }}</div>
		</ion-tab-button>
	</ion-tab-bar>
</template>

<script setup>
import { useRoute } from "vue-router"

import { IonTabBar, IonTabButton } from "@ionic/vue"

import HomeIcon from "@/components/icons/HomeIcon.vue"
import LeaveIcon from "@/components/icons/LeaveIcon.vue"
import ExpenseIcon from "@/components/icons/ExpenseIcon.vue"
import SalaryIcon from "@/components/icons/SalaryIcon.vue"
import AttendanceIcon from "@/components/icons/AttendanceIcon.vue"
import { inject } from "vue"

const __ = inject("$translate")

const route = useRoute()

const tabItems = [
	{
		icon: HomeIcon,
		title: __("Home"),
		route: "/home",
	},
	{
		icon: AttendanceIcon,
		title: __("Attendance"),
		route: "/dashboard/attendance",
	},
	{
		icon: LeaveIcon,
		title: __("Leaves"),
		route: "/dashboard/leaves",
	},
	{
		icon: ExpenseIcon,
		title: __("Expenses"),
		route: "/dashboard/expense-claims",
	},
	{
		icon: SalaryIcon,
		title: __("Salary"),
		route: "/dashboard/salary-slips",
	},
]
</script>

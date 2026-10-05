<template>
	<BaseLayout :pageTitle="__('Leaves & Holidays')" :intro="__('Plan your time away and keep track of every request.')" icon="sun">
		<template #body>
			<div class="joshr-dashboard flex flex-col items-center py-4">
				<LeaveBalance />

				<div class="flex flex-col gap-7 mt-5 px-4 w-full">
					<router-link
						:to="{ name: 'LeaveApplicationFormView' }"
						v-slot="{ navigate }"
					>
						<Button
							@click="navigate"
							variant="solid"
							class="joshr-primary-action py-5 text-base w-full"
						>
							{{ __("Request a Leave") }}
						</Button>
					</router-link>
					<div>
						<div class="text-lg text-gray-800 font-bold">{{ __('Recent Leaves') }} </div>
						<RequestList
							:component="markRaw(LeaveRequestItem)"
							:items="myLeaves.data"
							:addListButton="true"
							listButtonRoute="LeaveApplicationListView"
						/>
					</div>
					<Holidays />
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { markRaw } from "vue"

import BaseLayout from "@/components/BaseLayout.vue"
import LeaveBalance from "@/components/LeaveBalance.vue"
import RequestList from "@/components/RequestList.vue"
import LeaveRequestItem from "@/components/LeaveRequestItem.vue"
import Holidays from "@/components/Holidays.vue"

import { myLeaves } from "@/data/leaves"
</script>

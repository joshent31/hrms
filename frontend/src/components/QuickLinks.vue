<template>
	<div class="joshr-quick-links">
		<h2 class="joshr-section-title">{{ title || __("Quick Links") }}</h2>
		<div class="joshr-action-grid">
			<router-link
				class="joshr-action-card"
				v-for="link in props.items"
				:key="link.title"
				:to="{ name: link.route }"
			>
				<div class="joshr-action-content">
					<component :is="link.icon" class="joshr-action-icon" />
					<div class="text-base font-normal text-gray-800">
						{{ link.title }}
					</div>
				</div>
				<FeatherIcon name="arrow-up-right" class="joshr-action-arrow" aria-hidden="true" />
			</router-link>
		</div>
	</div>
</template>

<script setup>
import { FeatherIcon } from "frappe-ui"

const props = defineProps({
	title: {
		type: String,
		required: false,
		default: "",
	},
	items: {
		type: Array,
		required: true,
	},
})
</script>

<template>
	<div class="joshr-quick-links">
		<h2 class="joshr-section-title">{{ title || __("Quick Links") }}</h2>
		<div class="joshr-action-grid">
			<component
				:is="link.href ? 'a' : 'router-link'"
				class="joshr-action-card"
				v-for="link in props.items"
				:key="link.title"
				:to="link.route ? { name: link.route } : undefined"
				:href="link.href"
			>
				<div class="joshr-action-content">
					<component :is="link.icon" class="joshr-action-icon" />
					<div>
						<div class="text-base font-normal text-gray-800">
							{{ link.title }}
						</div>
						<div v-if="link.description" class="joshr-action-description">
							{{ link.description }}
						</div>
					</div>
				</div>
				<FeatherIcon name="arrow-up-right" class="joshr-action-arrow" aria-hidden="true" />
			</component>
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

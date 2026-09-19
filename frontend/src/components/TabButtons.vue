<template>
	<div class="joshr-segmented flex p-1">
		<button
			v-for="button in buttons"
			:key="button.key ?? button.label ?? button"
			type="button"
			:aria-pressed="modelValue === (button.key ?? button.label ?? button)"
			class="joshr-segment flex-auto font-medium text-sm"
			:class="
				modelValue === (button.key ?? button.label ?? button)
					? 'bg-white drop-shadow text-gray-900'
					: 'text-gray-600'
			"
			@click="$emit('update:modelValue', button.key ?? button.label ?? button)"
		>
			{{ button.label ?? __(button) }}
		</button>
	</div>
</template>

<script setup>
const props = defineProps({
	buttons: {
		type: Array,
		required: true,
	},
	modelValue: {
		type: String,
	},
})

defineEmits(["update:modelValue"])
</script>

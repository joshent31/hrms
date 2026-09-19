<template>
	<ion-page>
		<ion-header class="ion-no-border joshr-header">
			<div class="joshr-shell">
				<div class="joshr-header-inner">
					<div class="flex flex-row justify-between items-center">
						<div class="flex flex-row items-center gap-2">
							<FrappeHRLogo class="h-8 w-8" />
							<h2 class="text-xl font-bold text-gray-900">
								{{ props.pageTitle || __("JOSHR") }}
							</h2>
						</div>
						<div class="flex flex-row items-center gap-3 ml-auto">
							<router-link
								:to="{ name: 'Notifications' }"
								:aria-label="__('Notifications')"
								class="joshr-header-action"
							>
								<span class="relative inline-block">
									<FeatherIcon name="bell" class="h-6 w-6" />
									<span
										v-if="unreadNotificationsCount.data"
										class="absolute top-0 right-0.5 inline-block w-2 h-2 bg-red-600 rounded-full border border-white"
									>
									</span>
								</span>
							</router-link>
							<router-link
								:to="{ name: 'Profile' }"
								:aria-label="__('My profile')"
								class="joshr-header-action"
							>
								<Avatar
									:image="user.data?.user_image"
									:label="user.data?.first_name"
									size="xl"
								/>
							</router-link>
						</div>
					</div>
				</div>
			</div>
		</ion-header>

		<ion-content class="ion-no-padding joshr-content">
			<div class="joshr-shell joshr-page-body">
				<slot name="body"></slot>
			</div>
		</ion-content>
	</ion-page>
</template>

<script setup>
import FrappeHRLogo from "@/components/icons/FrappeHRLogo.vue"
import { IonHeader, IonContent, IonPage } from "@ionic/vue"
import { FeatherIcon, Avatar } from "frappe-ui"

import { unreadNotificationsCount } from "@/data/notifications"

import { inject } from "vue"

const user = inject("$user")

const props = defineProps({
	pageTitle: {
		type: String,
		required: false,
		default: "",
	},
})
</script>

<template>
	<view>
		<view>
			<!-- <input type="text" value="" @input="onTextInput" /> -->
			<router-link to="pages/test/index">
				<button type="primary" @click="send">
					開始遊戲
				</button>
			</router-link>

			<router-link to="pages/test/index">
				<button type="primary" @click="send_dan">
					單機版
				</button>
			</router-link>


			<view style="position: fixed; bottom: 0;">
				<button type="primary" @click="logout">
					登出
				</button>
			</view>
		</view>
	</view>
</template>

<script>
	import * as firebase from '@/common/app';
	import '@/common/firestore.min';

	export default {
		data() {
			return {
				text: '',

			}
		},
		onLoad() {
			var config = {
				apiKey: "AIzaSyC99xG1nJDaoDgBFK5_v26H-Q9wUB2TCwc",
				authDomain: "willion-54d6b.firebaseapp.com",
				databaseURL: "https://willion-54d6b.firebaseio.com",
				projectId: "willion-54d6b",
				storageBucket: "willion-54d6b.appspot.com",
				messagingSenderId: "762283103134"
			};


			if (!firebase.apps.length) {
				firebase.initializeApp(config);

				console.log(firebase.app().name);
			};

		},
		methods: {
			// 			onTextInput: function(e) {
			// 				this.text = e.target.value;
			// 			},
			send: function() {
				var userid = ""
				uni.getStorage({
					key: "id",
					success: function(res) {
						userid = res.data;
						console.log(res.data);

					},

				})
				console.log(userid)

				var game = firebase.firestore().collection("game").doc("game1")
				var match = firebase.firestore().collection("user").doc(userid).set({

					"now_match": "",

				});
				var a = "waiting." + userid
				game.update({
					[a]: ""
				})
				uni.redirectTo({
					url: '../test/index'
				});





			},
			// 			
			logout: function() {
				firebase.auth().signOut().then(function() {
					// Sign-out successful.
					uni.redirectTo({
						url: '../index/login'
					});
				}).catch(function(error) {
					// An error happened.
				});
			},
			send_dan: function() {
				var userid = ""
				uni.getStorage({
					key: "id",
					success: function(res) {
						userid = res.data;
						console.log(res.data);

					},

				})
				console.log(userid)

				var game = firebase.firestore().collection("game").doc("game1")
				var match = firebase.firestore().collection("user").doc(userid).set({

					"now_match": "",

				});
				var a = "waiting." + userid
				game.update({
					[a]: ""
				})
				const requestTask2 = uni.request({
					url: 'https://asia-east2-willion-54d6b.cloudfunctions.net/demo_create_user',
					method:'GET',
					success: function(res) {
						console.log(res.data);
						uni.redirectTo({
							url: '../demo/demo'
						});
					}
				});
			},
		}
	}
</script>

<style>
</style>

<template>

	<view>
		<view class="uni-form-item uni-column">
			<view class="title">信箱</view>
			<input class="uni-input" type="text" @input="onAccInput" placeholder="請輸入信箱"/>
		</view>
		<view class="uni-form-item uni-column">
			<view class="title">密碼</view>
			<view class="with-fun">
				<input class="uni-input" placeholder="請輸入密碼" @input="onPassInput" :password="showPassword" />
				<view class="uni-icon uni-icon-eye" :class="[!showPassword ? 'uni-active' : '']" @click="changePassword"></view>
			</view>
		</view>
		<button type="primary" @click="emailLogin">
			登入
		</button>
		<br>
		<button type="primary" @click="register">
			註冊

		</button>
		<br>
		<view>
			<button type="primary" @click="login_fb">
				fb 登入
			</button>

		</view>
		<br>
		<view>

			<button type="primary" @click="login_ano">
				訪客登入
			</button>
		</view>
	</view>

</template>
<script>
	import * as firebase from '@/common/app';
	import '@/common/firestore.min';
	import '@/common/auth.min';
	export default {
		data() {
			return {
				text: '',
				showPassword: true,
				passwordValue: '',
				accountValue: '',


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

			this.getinfo();




		},
		methods: {
			onAccInput: function(event) {
				this.accountValue = event.target.value

			},
			onPassInput: function(event) {

				this.passwordValue = event.target.value
			},
			emailLogin: function() {
				firebase.auth().signInWithEmailAndPassword(this.accountValue, this.passwordValue).catch(function(error) {
					// Handle Errors here.
					var errorCode = error.code;
					var errorMessage = error.message;
					console.log(errorMessage)

				});

			},
			register: function() {
				firebase.auth().createUserWithEmailAndPassword(this.accountValue, this.passwordValue).catch(function(error) {
					// Handle Errors here.
					var errorCode = error.code;
					var errorMessage = error.message;
					console.log(errorMessage)
				});
			},


			changePassword: function() {
				this.showPassword = !this.showPassword;
			},
			login_fb: function() {

				var provider = new firebase.auth.FacebookAuthProvider();
				firebase.auth().signInWithRedirect(provider).then(function(result) {
					// This gives you a Facebook Access Token. You can use it to access the Facebook API.
					uni.showLoading({
						title: "登入中"
					})
					var token = result.credential.accessToken;
					// The signed-in user info.
					var user = result.user;


					// ...
				}).catch(function(error) {
					// Handle Errors here.
					var errorCode = error.code;
					var errorMessage = error.message;
					// The email of the user's account used.
					var email = error.email;
					// The firebase.auth.AuthCredential type that was used.
					var credential = error.credential;

				});


			},
			login_ano: function() {

				firebase.auth().signInAnonymously().catch(function(error) {
					// Handle Errors here.
					var errorCode = error.code;
					var errorMessage = error.message;
					// ...
				});
				uni.showLoading({
					title: '登入中'
				});

			},
			getinfo: function() {
				firebase.auth().onAuthStateChanged(function(user) {
					if (user) {
						// User is signed in.
						var displayName = user.displayName;
						var email = user.email;
						var emailVerified = user.emailVerified;
						var photoURL = user.photoURL;
						var isAnonymous = user.isAnonymous;
						var uid = user.uid;
						var providerData = user.providerData;
						uni.setStorage({
							key: 'id',
							data: user.uid,

						})
						uni.redirectTo({
							url: '../database/database'
						});
						// ...
					} else {
						// User is signed out.
						// ...
					}
				});




			},


		},

	}
</script>
<style>
</style>

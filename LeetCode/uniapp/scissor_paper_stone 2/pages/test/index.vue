<template>
	<view>
		<page-head :title="title"></page-head>

		<view class="uni-padding-wrap uni-flex uni-column ">
			<view>
				<view style="text-align: left; font-size: 20px;">
					myID :{{user_name + "  "}}

					<!-- <uni-countdown :show-day="false" :second="time" @timeup="timeup" /> -->
					出拳剩餘時間{{ sessionTime }}

				</view>
				<view style="text-align: right; font-size: 20px;">

					<!-- {{ score }} -->
				</view>
				<view style=" font-size: 18px;">
					{{ round +"     "+ turn    }} <br>Score :
				</view>

				<br>

				<view class="uni-flex uni-row " style="flex-wrap: wrap;">

					<view v-for="(item,index) in player" :key="index" v-if="player.length === 1">
						<view class="uni-flex-item-with-height-1 uni-bg-red">{{item.name}}
							<button type="default" @tap="modalTap" style="background:#F76260; font-size:0;">
								<view style="flex: 1;height: 300upx;display: flex; justify-content: center;align-items: center; background:#F76260; font-size:0;">

									<image class="image" mode="widthFix" style="align-items: center;" src="../../static/問號.jpg" />
								</view>
							</button>
						</view>

					</view>

					<view v-for="(item,index) in player" :key="index" v-if="player.length === 2">
						<view class="uni-flex-item-with-height-2 uni-bg-red">{{item.name}}
							<button type="default" @tap="modalTap" style="background:#F76260; font-size:0;">
								<view style="flex: 1;height: 300upx;display: flex; justify-content: center;align-items: center; background:#F76260; font-size:0;">
									<image class="image" mode="widthFix" src="../../static/問號.jpg" />
								</view>
							</button>
						</view>

					</view>
					<view v-for="(item,index2) in player" :key="index2" v-if="player.length === 4">
						<view class="uni-flex-item-with-height-2 uni-bg-red">{{item.name}}


							<button class="uni-bg-red" position="button" @click="show_his(item.name)">
								<image class="image" mode="widthFix" :src='display[item.name]' />
							</button>


							<uni-popup :show="type === 'middle-list'" :msg="his_id" position="middle" mode="fixed" @hidePopup="togglePopup('')">
								<scroll-view class="uni-center center-box" scroll-y="true">

									<view class="" v-for="(item1, index1) in play_history" :key="index1" v-if="index1.indexOf(his_id)>-1">
										<!-- {{item1}} -->
										<view class="" v-for="(item2, index2) in item1" :key="index2">
											<view>{{index2}} : </view>

											<image style="width: 50px; height: 50px;" class="image" mode="widthFix" :src="detail_pic_show(item2)" />
										</view>
									</view>


								</scroll-view>
							</uni-popup>

						</view>

					</view>
					<view v-for="(item,index) in player" :key="index" v-if="player.length >= 2 && player.length !=4">
						<view class="uni-flex-item-with-height uni-bg-red">{{item.name}}


							<button v-for="(item,index) in play_history" :key="index" class="uni-bg-red" type="button" @click="togglePopup('middle-list')">
								<image class="image" mode="widthFix" src="../../static/item.round.jpg" />
							</button>

							<uni-popup :show="type === 'middle-list'" position="middle" mode="fixed" @hidePopup="togglePopup('')">
								<scroll-view class="uni-center center-box" scroll-y="true">
									<view v-for="(item, index) in list" :key="index">
										我的自不見了 {{ list[index] }}
									</view>
								</scroll-view>
							</uni-popup>

						</view>

					</view>
				</view>
			</view>

		</view>




		<view class="uni-flex " style="position: fixed; bottom: 0;" v-if="(lose == false) && (if_end==false)">
			<view>
				<button data-id="scissors" data-choose="../../static/scissors.jpeg" @click="choose">
					<image class="image" mode="widthFix" src="../../static/scissors.jpeg" />
				</button>
			</view>
			<view>
				<button data-id="stone" data-choose="../../static/stone.jpeg" @click="choose">
					<image class="image" mode="widthFix" src="../../static/stone.jpeg" />
				</button>
			</view>
			<view>
				<button data-id="paper" data-choose="../../static/paper.jpeg" @click="choose">
					<image class="image" mode="widthFix" src="../../static/paper.jpeg" />
				</button>
			</view>


			<view>
				<text> &nbsp;&nbsp;&nbsp;</text>
			</view>
			<view style="text-align: right;">
				<button>
					<image class="image" mode="widthFix" :src='pic' />
				</button>
				<button @click="play" v-if="submit_button_show==true">
					<text style="height: 20upx;"> submit</text>
				</button>
			</view>

		</view>
		<!-- 		<view v-if="lose == true&& if_end == false">
			you lose ,please wait until next round
			<button @click="demo_play">
				<text style="height: 20upx;"> 其他四人猜拳</text>
			</button>
		</view> -->
		<view v-if="if_end == true">
			<button @click="back_to_homepage">
				<text style="height: 20upx;"> 回首頁</text>
			</button>
		</view>




	</view>

</template>
<script>
	import uniCountdown from '@/components/uni-countdown/uni-countdown.vue';
	import uniPopup from '@/components/uni-popup/uni-popup.vue';
	import * as firebase from '@/common/app';
	import '@/common/firestore.min';
	import '@/common/function.min';
	import uniNoticeBar from '@/components/uni-notice-bar/uni-notice-bar.vue';

	var _self;
	export default {
		components: {
			uniPopup,
			uniCountdown,
			uniNoticeBar,


		},
		data() {
			return {
				title: '配對中',
				type: '',

				list: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
				radioItems: [{
						name: 'Scissors',
						value: '剪刀',
						checked: 'true'
					},
					{
						name: 'Stones',
						value: '石頭',
						checked: 'true'
					},
					{
						name: 'Papers',
						value: '布',
						checked: 'true'
					}
				],

				player: [

				],
				pic: "../../static/問號.jpg",
				user: "",
				match: "",
				user_choose: "",
				round: "",
				turn: "",

				result: "",
				user_name: "",
				modalHidden: true,
				modalHidden2: true,
				lose: false,
				play_history: [],
				display: {},
				turnround: "",
				lastturnround: "",
				listOfObjects: "",
				last_advance: [1, 1, 1, 1, 1],
				his_id: "",
				submit_button_show: false,
				time: null,
				sessionTime: 30,
				if_end: false,
				timer_active: false,

			}

		},
	
		onLoad() {

			_self = this;

			this.showLoading("配對中");
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

			this.user = uni.getStorage({
				key: "id",
				success: function(res) {
					// console.log(res.data);
				}
			});

			// 
			this.wait();

			this.lastturnround = uni.getStorage({
				key: "lastturnround",
				success: function(res) {},
			})
		},
		onBackPress() {
			if (this.type !== '') {
				this.type = '';
				return true;
			}
		},
		methods: {
			timer() {
				let my = this
				my.sessionTime = 30
				if (my.timer_active === false) {
					console.log("starttime")
					this.time = setInterval(() => {
						if (my.sessionTime > 0) {
							my.sessionTime--
						}
			
						if (my.sessionTime === 0) {
							my.timeup();
							my.stoptimer();
							return;
						}
					}, 1000)
					my.timer_active = true
				}
			
			
			},
			stoptimer() {
				console.log("stoptime")
				clearInterval(this.time)
				this.timer_active = false
			},
			timeup() {
				uni.showToast({
					title: '時間到'
				})
			},
			show_his: function(id) {
				console.log(id)
				this.his_id = id
				console.log(this.his_id)
				this.togglePopup('middle-list');
			},
			detail_pic_show(e) {

				return ('../../static/' + e + '.jpeg')
			},

			togglePopup(type) {
				this.type = type;
			},
			showLoading: function(e) {
				uni.showLoading({
					title: e
				});
			},

			showLoading_lose: function() {
				uni.showLoading({
					title: '你輸了'
				});
			},
			showLoading_win: function() {
				uni.showLoading({
					title: '你贏了'
				});
			},
			hideLoading: function() {
				uni.hideLoading();
			},

			toast4Tap: function() {
				uni.showToast({
					title: "logo",

				})
			},


			tapEvent: function(e) {
				console.log('按钮被点击')
			},
			rowCount: function(player) {
				console.log(player.name)

			},


			// 				noTitle
			modalTap: function(e) {
				uni.showModal({
					content: "出拳情況",
					showCancel: false,


				})
			},
			modalTap_new: function(e) {
				uni.showModal({
					content: e,
					showCancel: false,
					confirmText: "繼續"

				})
			},
			choose: function(e) {
				this.pic = e.target.dataset.choose
				this.user_choose = e.target.dataset.id
				console.log(this.pic)
				console.log(this.user_choose)
			},
			back_to_homepage: function() {
				uni.redirectTo({
					url: '../database/database'
				});
			},


			wait: function(e) {




				uni.getStorage({
					key: "id",
					success: function(res) {
						_self.user = res.data;
						_self.user_name = (res.data.substring(0, 5))
						// console.log(res.data);

					},

				})

				var game = firebase.firestore().collection("user").doc(_self.user)

				game.onSnapshot(function(doc) {
					var data = doc.data();
					var value = data.now_match;

					console.log(data)
					// console.log(value)
					_self.match = value
					var game1 = firebase.firestore().collection("game").doc("game1").collection("match").doc(_self.match)
					//＊＊＊會多跑很多次＊＊＊
					game1.get().then(function(doc) {

						_self.player = [];
						_self.hideLoading();
						var data = doc.data();
						for (var index in Object.keys(data.play)) {
							// console.log(Object.keys(data.play)[index])
							if (Object.keys(data.play)[index] == _self.user) {
								continue
							} else {
								_self.player.push({
									"name": Object.keys(data.play)[index].substring(0, 5)
								})
								_self.display[Object.keys(data.play)[index].substring(0, 5)] = "../../static/問號.jpg"

							}

						}
					})
					_self.timer();
					_self.submit_button_show = true
					_self.getRound();
					_self.getResult();


				})


			},

			play: function() {
				this.showLoading("等待其他玩家出拳");
				this.stoptimer();
				this.submit_button_show = false
				var game = firebase.firestore().collection("game").doc("game1").collection("match").doc(_self.match)
				// console.log(this.user_choose)
				game.get().then(function(doc) {
					var data = doc.data()
					uni.setStorage({
						key: 'lastturnround',
						data: data.status["processing"]

					})
					_self.lastturnround = data.status["processing"]
					console.log(_self.lastturnround)
				})
				var a = "play." + this.user
				game.update({
					[a]: this.user_choose

				});
				console.log(this.lastturnround)
				console.log(_self.user)
				console.log(_self.match)
				// 				const requestTask3 = uni.request({
				// 					url: 'https://us-central1-willion-54d6b.cloudfunctions.net/function-1',
				// 
				// 					data: {
				// 
				// 						'user_id': _self.user,
				// 						'match': _self.match
				// 					},
				// 					method: "GET",
				// 
				// 					success: function(res) {
				// 
				// 						console.log(res.data);
				// 					}
				// 				});
				// 


				// this.getResult();


			},


			getResult: function() {

				var game = firebase.firestore().collection("game").doc("game1").collection("match").doc(_self.match)
				var game2 = game.collection("play_data").doc("play_data")
				console.log(_self.match)
				game2.onSnapshot(function(doc) {

					var data = doc.data();
					console.log(data)
					var round = data[Object.keys(data)[Object.keys(data).length - 1]]
					// _self.round = Object.keys(data)[Object.keys(data).length - 1]
					console.log(round)
					var turn = round[Object.keys(round)[Object.keys(round).length - 2]]
					// _self.turn = Object.keys(round)[Object.keys(round).length - 2]
					console.log(turn['advance'].length)


					console.log(_self.last_advance)
					_self.submit_button_show = true

					if (turn["advance"].length > 1) {
						if (turn["advance"].includes(_self.user) === false) {
							if (_self.lose !== true) {
								_self.modalTap_new("你輸了請等待本局結束");
								_self.lose = true
							}


						} else {
							if (turn["winner_chose"] === "no one win!") {
								_self.modalTap_new("平手，請繼續出拳");
							} else {
								_self.modalTap_new("你贏了，請繼續出拳");
							}

						}
						_self.last_advance = turn["advance"]

					} else if (turn["advance"].length === 0) {
						_self.getRound();
					} else {
						if (turn["advance"].includes(_self.user) === false) {
							_self.modalTap_new("本局結束，" + turn["advance"][0] + "為本局贏家");
							_self.lose = false

						} else {
							_self.modalTap_new("你贏了本局");
						}



					}

					_self.getRound();
					_self.getPlayHistory();
					_self.hideLoading();
					_self.stoptimer();
					console.log(_self.if_end)
					if (_self.if_end === false) {
						_self.timer();
					}


				})


			},
			demo_play: function() {
				var game = firebase.firestore().collection("game").doc("game1").collection("match").doc(_self.match)
				// console.log(this.user_choose)
				game.get().then(function(doc) {
					var data = doc.data()
					uni.setStorage({
						key: 'lastturnround',
						data: data.status["processing"]

					})
					_self.lastturnround = data.status["processing"]
					console.log(_self.lastturnround)
				})
				var a = "play." + this.user

				console.log(this.lastturnround)
				console.log(_self.user)
				console.log(_self.match)
				const requestTask3 = uni.request({
					url: 'https://us-central1-willion-54d6b.cloudfunctions.net/function-1',

					data: {

						'user_id': _self.user,
						'match': _self.match
					},
					method: "GET",

					success: function(res) {

						console.log(res.data);
					}
				});
				this.getResult();
			},
			getRound() {
				var game = firebase.firestore().collection("game").doc("game1").collection("match").doc(_self.match)
				game.get().then(function(doc) {
					var data = doc.data()
					try {
						_self.round = (data.status["processing"]).split("/")[0]
						_self.turn = (data.status["processing"]).split("/")[1]
						return (data.status["processing"])

					} catch (e) {
						_self.if_end = true
						console.log(data.status)
						if (data.status == 'end') {
							_self.submit_button_show = false
							_self.modalTap_new("比賽結束");
							_self.stoptimer();
						}
						return (data.status)
					}


				})

			},


			getPlayHistory: function() {
				var game = firebase.firestore().collection("game").doc("game1").collection("match").doc(_self.match)
				game.get().then(function(doc) {
					var data = doc.data()

					_self.play_history = data.play_history
					_self.display = []

					for (var index in Object.keys(data.play_history)) {
						var lastturnround = uni.getStorage({
							key: "lastturnround",
							success: function(res) {
								_self.lastturnround = res.data
							},
						})

						console.log(lastturnround)
						console.log(data.play_history[Object.keys(data.play)[index]][_self.lastturnround])
						// 						
						if (Object.keys(data.play_history)[index] !== _self.user) {
							if (data.play_history[Object.keys(data.play)[index]][_self.lastturnround] === "-") {
								_self.display[Object.keys(data.play)[index].substring(0, 5)] = "../../static/loser.jpeg"
							} else {
								_self.display[Object.keys(data.play)[index].substring(0, 5)] = "../../static/" + data.play_history[Object.keys(
									data.play)[index]][_self.lastturnround] + ".jpeg"
							}

						}
					}



				})
			}

		}
	}
</script>

<style>
	.text {
		margin: 15upx 10upx;
		padding: 0 20upx;
		background-color: #ebebeb;
		height: 70upx;
		line-height: 70upx;
		text-align: center;
		color: #777;
		font-size: 26upx;
	}

	.desc {
		/* text-indent: 40upx; */
	}

	.uni-list-cell {
		justify-content: flex-start
	}

	.uni-list .label-3 {
		padding: 0;
	}

	.image {
		margin: 20upx 0;
		width: 100upx;
	}



	page {
		display: flex;
		flex-direction: column;
		box-sizing: border-box;
		background-color: #fff
	}

	view {
		font-size: 28upx;
		line-height: inherit
	}

	.example {
		padding: 0 30upx 30upx
	}

	.example-title {
		font-size: 32upx;
		line-height: 32upx;
		color: #777;
		margin: 40upx 25upx;
		position: relative
	}

	.example .example-title {
		margin: 40upx 0
	}

	.example-body {
		padding: 0 40upx
	}

	.uni-padding-wrap {
		padding: 0 30upx;
	}

	button {
		margin: 20upx 0;
	}

	.uni-helllo-text {
		height: 100upx;
		line-height: 100upx;
		text-align: center;
	}

	.center-box {
		width: 500upx;
		height: 500upx;
	}

	.uni-list-item {
		text-align: left;
		line-height: 80upx;
		border-bottom: 1px #f5f5f5 solid;
	}



	.uni-list-item:last-child {
		border: none;
	}

	.center-box .image {
		width: 100%;
		height: 100%;
	}

	.bottom-title {
		line-height: 60upx;
		font-size: 24upx;
		padding: 15upx 0;
	}

	.bottom-content {
		display: flex;
		flex-wrap: wrap;
		padding: 0 35upx;
	}

	.bottom-content-box {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-bottom: 15upx;
		width: 25%;
		box-sizing: border-box;
	}

	.bottom-content-image {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 90upx;
		height: 90upx;
		overflow: hidden;
		background: #007aff;
		border-radius: 10upx;
	}

	.bottom-content-text {
		font-size: 26upx;
		color: #333;
		margin-top: 10upx;
	}

	.bottom-btn {
		height: 90upx;
		line-height: 90upx;
		border-top: 1px #f5f5f5 solid;
	}

	.bottom-content-image.wx {
		background: #00ce47;
	}

	.bottom-content-image.qq {
		background: #00b6f6;
	}

	.bottom-content-image.sina {
		background: #ff766a;
	}

	.bottom-content-image.copy {
		background: #07ccd0;
	}

	@font-face {
		font-family: 'iconfont';
		/* project id 1028200 */
		src: url('https://at.alicdn.com/t/font_1028200_47ewtwy4t04.ttf') format('truetype');
	}

	.icon {
		font-family: 'iconfont';
		font-size: 40upx;
		color: #fff;
	}
</style>

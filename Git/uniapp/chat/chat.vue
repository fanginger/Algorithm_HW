<template>
	<view class="wholePage">
		<view class="topChat">
			<scroll-view id="scrollview" class="contentShowStyle" :scroll-top="scrollTop" :style="{height:styleSV.contentViewHeight+'px'}"
			 :scroll-with-animation="true" scroll-y="true">
				<view class="contentSaveStyle" v-for="(item,index) in contentSave">
					<view class="textMe" v-if="item['userId'] == userId">
						<view class="timeMe">{{item['realTime']}}</view><view class="borderMe">{{item['text']}}</view>{{item['userId']}}
					</view>
					<view class="textOther" v-if="item['userId'] != userId">
						{{item['userId']}}<view class="borderOther">{{item['text']}}</view><view class="timeOther">{{item['realTime']}}</view>
					</view>
				</view>
			</scroll-view>
		</view>
		<view class="bottomChat" :style="{height:styleBC.showHeight+'px'}">
			<textarea class="contentDec" :style="{width:styleBC.showWidth+'px'}" v-model="contentShow" />
			<view size="mini" :style="{width:styleBC.showWidthButton+'px'}" class="buttonSend" @click="submitDb">傳送</view>
		</view>		
	</view>
</template>

<script>
	import * as firebase from '@/common/app';
	import '@/common/firestore.min';
	import '@/common/function.min';

	var _self;

	export default {
		props:{
			config: {
				type: Object,
				default() {
					return {
						apiKey: "AIzaSyA2P0T3COrV1DHStIEBLnJoIuY4LunGmNg",
						authDomain: "fir-test-84116.firebaseapp.com",
						databaseURL: "https://fir-test-84116.firebaseio.com",
						projectId: "fir-test-84116"
					};
				}
			},
			userId: {
				type: String,
				default: "John"
			}
		},
		data() {
			return {
				styleSV : {
					contentViewHeight: 0,
					mitemHeight: 0
				},
				styleBC : {
					showHeight: 0,
					showWidth: 0,
					showWidthButton: 0
				},
				// 用於顯示
				contentSave : [],
				// 用於push並儲存聊天記錄
				contentShow : '',
				scrollTop : 0,
				chatLength : 0
			}
		},
		onLoad(data) {
			_self = this;
			this.pixelCalculation(); 
			// var config = {
			// 	apiKey: "AIzaSyA2P0T3COrV1DHStIEBLnJoIuY4LunGmNg",
			// 	authDomain: "fir-test-84116.firebaseapp.com",
			// 	databaseURL: "https://fir-test-84116.firebaseio.com",
			// 	projectId: "fir-test-84116"
			// };
			
			// 連接Firestore並啟動
			firebase.initializeApp(this.config);
			// 將相關對應項目寫入變數，方便帶入
			var db = firebase.firestore();
			var chatConnect = db.collection('Chatroom').doc('game_match_round').collection('message');
			// 監聽最新資訊並併入contentSave，方便顯示
			chatConnect.orderBy('time').onSnapshot(function(messageToLocal){
				_self.contentSave = [];
				this.chatLength = messageToLocal.docs.length;
				messageToLocal.forEach(function(doc){
					_self.contentSave.push(doc.data());
				});
			});
			// 將上頁登入賬號名稱代入本頁
			// this.userId = data.userId;	
		},
		methods: {
			// 登入本頁時，按照手機長寬進行有效佈局
			pixelCalculation: function() {
				const phoneData = uni.getSystemInfoSync();
				this.styleBC.showHeight = phoneData.windowHeight*0.07;
				this.styleBC.showWidth = phoneData.windowWidth - (phoneData.windowWidth * 0.26)
				this.styleBC.showWidthButton = phoneData.windowWidth - (phoneData.windowWidth * 0.8);
				this.styleSV.contentViewHeight = phoneData.windowHeight*0.93;
				var scrollViewHeight = phoneData.windowHeight;
				console.log(phoneData);
				uni.onWindowResize((res) => {
					if (res.deviceOrientation == 'portrait') {
						this.pixelCalculation();
					} else {
						this.styleBC.showHeight = res.size.windowHeight*0.13;
						this.styleBC.showWidth = res.size.windowWidth - (res.size.windowWidth * 0.24)
						this.styleBC.showWidthButton = res.size.windowWidth - (res.size.windowWidth * 0.8);
						this.styleSV.contentViewHeight = res.size.windowHeight*0.87;
					};
				});
			},
			// 每新增一筆資訊，將自動滑動到最新消息
			scrollToBottom: function () {
				var query = uni.createSelectorQuery();
				// selectAll 為選取所有row
				query.selectAll('.contentSaveStyle').boundingClientRect();
				query.select('#scrollview').boundingClientRect();	
				// query.select('.contentShow').boundingClientRect();
				// 執行時針對現屏幕進行半段做出置底
				query.exec(function (res) {
					_self.styleSV.mitemHeight = 0;
					_self.styleSV.mitemHeight = res[1].height;
					res[0].forEach(function (rect) {
						_self.styleSV.mitemHeight = _self.styleSV.mitemHeight + rect.height + 40;
						// console.log(_self.styleSV.mitemHeight);
					});
					if (_self.styleSV.mitemHeight > (_self.styleSV.contentViewHeight - 100)) {
						_self.scrollTop = _self.styleSV.mitemHeight;
					}
				});
			},
			// Local端顯示及儲存，再推送到資料庫
			submitDb : function(){
				// 先把格式（Dic）設定好
				var checkSpace = this.contentShow.trim();
				if (checkSpace == '' || checkSpace == null) {
					uni.showModal({
						title: '警告',
						content: '聊天內容不可空白！',
						confirmText: '了解',
						showCancel: false
					})
				}else{
 					var db = firebase.firestore();
					var chatConnect = db.collection('Chatroom').doc('game_match_round').collection('message');
					var message = {
						text : this.contentShow,
						userId : this.userId,
						time : new Date().getTime(),
						order : this.chatLength + 1,
						realDate : new Date().toDateString(),
						realTime : new Date().toLocaleTimeString()
					};
					// 發送信息時先上傳firestore
					this.uploadDB(message);
				};
				//完成一切作業後將textarea清空
				_self.contentShow = '';
			},
			uploadDB : async function(message){
				var db = firebase.firestore();
				var chatConnect = db.collection('Chatroom').doc('game_match_round').collection('message');
				await chatConnect.add(message).then(function(docRef) {
					// 上傳firestore後console相關id
					console.log("Document written with ID: ", docRef.id);
					_self.scrollToBottom();
				})
				.catch(function(error) {
					console.error("Error adding document: ", error);
				});
			}
		}
	}
</script>

<style lang="scss">
	@import "@/pages/chat/chat.scss" ;
</style>

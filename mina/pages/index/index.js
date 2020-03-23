//login.js
//获取应用实例
var app = getApp();
Page({
    data: {
        remind: '加载中',
        angle: 0,
        userInfo: {},
        regFlag: true     //表示是否已经注册，默认为true
    },
    goToIndex: function () {
        wx.switchTab({
            url: '/pages/food/index',
        });
    },
    onLoad: function () {
        wx.setNavigationBarTitle({
            title: app.globalData.shopName
        });
        this.checkLogin();
    },
    onShow: function () {

    },
    onReady: function () {
        var that = this;
        setTimeout(function () {
            that.setData({
                remind: ''
            });
        }, 1000);
        wx.onAccelerometerChange(function (res) {
            var angle = -(res.x * 30).toFixed(1);
            if (angle > 14) {
                angle = 14;
            } else if (angle < -14) {
                angle = -14;
            }
            if (that.data.angle !== angle) {
                that.setData({
                    angle: angle
                });
            }
        });
    },
    checkLogin: function () {
        var that = this;
        wx.login({
            success: function (res) {
                if (!res.code) {
                    app.alert({'content': '登陆失败，请再次尝试'});
                    return;
                }
                wx.request({
                    url: app.buildUrl('/member/check-reg'),
                    header: app.getRequestHeader(),
                    method: 'POST',
                    data: {code: res.code},
                    success: function (res) {
                        if (res.data.code != 200) {
                            that.setData({
                                regFlag: false
                            });
                            return;
                        }
                         app.setCache("token",res.data.data.token);
                        // that.goToIndex();  //进入首页
                    }
                });
            }
        });
    },
    login: function (e) {
        var that = this;
        if (!e.detail.userInfo) {
            app.alert({'content': '登錄失敗，請再次嘗試'});
            return;
        }
        var data = e.detail.userInfo;

        wx.login({
            success: function (res) {
                if (!res.code) {
                    app.alert({'content': '登陆失败，请再次尝试'});
                    return;
                }
                data['code'] = res.code;
                wx.request({
                    url: app.buildUrl('/member/login'),
                    header: app.getRequestHeader(),
                    method: 'POST',
                    data: data,
                    success: function (res) {
                        if (res.data.code != 200) {
                            app.alert({'content': res.data.msg});
                            return;
                        }
                        app.setCache("token",res.data.data.token);
                        that.goToIndex();
                    }
                });
            }
        });


    }
});
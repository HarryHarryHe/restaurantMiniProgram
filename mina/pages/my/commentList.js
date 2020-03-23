var app = getApp();
Page({
    data: {
        list: [
            {
                date: "2019-12-01 22:30:23",
                order_number: "20191201223023001",
                content: "加辣变态辣那种",
            },
            {
                date: "2019-12-02 22:30:23",
                order_number: "20191202223023001",
                content: "不要辣",
            }
        ]
    },
    onLoad: function (options) {
        // 生命周期函数--监听页面加载

    },
    onShow: function () {
        this.getCommentList();
    },
    getCommentList:function(){
        var that = this;
        wx.request({
            url: app.buildUrl("/my/comment/list"),
            header: app.getRequestHeader(),
            success: function (res) {
                var resp = res.data;
                if (resp.code != 200) {
                    app.alert({"content": resp.msg});
                    return;
                }

                that.setData({
                    list: resp.data.list
                });

            }
        });
    }
});

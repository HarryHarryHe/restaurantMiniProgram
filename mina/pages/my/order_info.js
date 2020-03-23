var app = getApp();
Page({
    data: {},
    onLoad: function (e) {
        var that = this;
    },
    onShow: function () {
        var that = this;
        that.setData({
            info: {
                order_sn:"123123",
                status: -8,
                status_desc: "待支付",
                deadline:"2018-07-31 12:00",
                pay_price: "85.00",
                yun_price: 0.00,
                total_price: "85.00",
                address: {
                    name: "海涛",
                    mobile: "12345678901",
                    address: "广东省广州市从化区"
                },
                goods: [
                    {
                        name: "抹茶蛋糕",
                        price: "15.00",
                        unit: 1,
                        pic_url: "/images/food.jpg"
                    },
                    {
                        name: "双层芝士堡",
                        price: "25.00",
                        unit: 1,
                        pic_url: "/images/food.jpg"
                    }
                ]
            }
        });
    }
});
'''
python manager.py runjob -m pay/index
'''
import datetime

from application import app,db
from common.libs.pay.PayService import PayService
from common.models.pay.PayOrder import PayOrder


class JobTask():
    def __init__(self):
        pass

    def run(self, params):
        now = datetime.datetime.now()
        date_before_30min = now + datetime.timedelta(minutes=-30)
        list = PayOrder.query.filter_by(status=-8).filter(
            PayOrder.created_time <= date_before_30min.strftime("%Y-%m-%d %H:%M:%S")).all()

        if not list:
            app.logger.info("no data")
            return

        pay_target = PayService()
        for item in list:
            pay_target.closeOrder(pay_order_id=item.id)

        app.logger.info("over~")
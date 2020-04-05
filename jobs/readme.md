Job 列表  需要自己在服务器上配置 我还没配
======
* 队列Job

        * * * * * { . /developer/git-repository/Reservation_System/jobs/bash_jobs && cd /developer/git-repository/Reservation_System && python manager.py runjob -m queue/index ;} >> /developer/git-repository/Reservation_System/data/www/job_logs/queue_list.`date +\%Y_\%m_\%d`.log 2>&1
        * * * * * { . /developer/git-repository/Reservation_System/jobs/bash_jobs && cd /developer/git-repository/Reservation_System && python manager.py runjob -m pay/index ;} >> /developer/git-repository/Reservation_System/data/www/job_logs/pay_index.`date +\%Y_\%m_\%d`.log 2>&1
        1 2 * * * { . /developer/git-repository/Reservation_System/jobs/bash_jobs && cd /developer/git-repository/Reservation_System && python manager.py runjob -m stat/daily -a member ;} >> /developer/git-repository/Reservation_System/data/www/job_logs/pay_index.`date +\%Y_\%m_\%d`.log 2>&1
        2 2 * * * { . /developer/git-repository/Reservation_System/jobs/bash_jobs && cd /developer/git-repository/Reservation_System && python manager.py runjob -m stat/daily -a food ;} >> /developer/git-repository/Reservation_System/data/www/job_logs/pay_index.`date +\%Y_\%m_\%d`.log 2>&1
        3 2 * * * { . /developer/git-repository/Reservation_System/jobs/bash_jobs && cd /developer/git-repository/Reservation_System && python manager.py runjob -m stat/daily -a site ;} >> /developer/git-repository/Reservation_System/data/www/job_logs/pay_index.`date +\%Y_\%m_\%d`.log 2>&1
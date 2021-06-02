from Api_Run import auto_run
import time
import logging
import logging.config
CON_LOG="config/log.conf"
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
if __name__=="__main__":
    # 后台运行方式
    # nohup python3 timing_run.py > timenohup.log 2>&1 &
    while True:
        time_now = time.strftime("%H:%M", time.localtime())  # 刷新
        logging.info(time_now)
        if time_now=="00:00":  #设置定时执行的时间
            logging.info("定时时间到了，开始执行")
            logging.info(time_now)
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 定时执行用例"
            logging.info(now_time)
            auto_run()
        else:
            logging.info("定时时间没有到，等待30s")
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 不执行用例"
            logging.info(now_time)
            time.sleep(30)



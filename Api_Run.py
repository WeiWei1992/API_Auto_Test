import requests

import logging
import logging.config
CON_LOG="config/log.conf"
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

import os
from common.operate_excel import Operate_Excel,save_result,save_result_norun
from api.run_main import run_main
from common.send_eamil import my_send_email
import time
from openpyxl import load_workbook

# import logging
# import logging.config
# CON_LOG='log.conf'
# logging.config.fileConfig(CON_LOG)
# logging=logging.getLogger()
my_path=os.path.abspath(os.getcwd())
casefile=my_path+'/case/case.xlsx'
logging.info("casefile: "+str(casefile))
from common.sign import sha256

def auto_run():
    operate_excel=Operate_Excel(casefile)
    result_file=operate_excel.creat_excel()
    logging.info("结果保存路径： "+str(result_file))
    Cases=operate_excel.handle_casedata()
    #logging.info("读取到的用例是： "+str(Cases))

    #result_file=operate_excel.creat_excel()

    i=3

    for case in Cases:
        logging.info("-------用例"+str(i-2)+"-------------")
        if case['isrun']=='N':

            case_values=[]
            #case是字典，保存结果需要传入的是list,这里是把提取字典的value
            for value in case.values():
                case_values.append(value)

            save_result_norun(result_file,i,case_values)
        else:
            run_main(case,result_file,i)
            time.sleep(1)
        i=i+1
    #332315237@qq.com 张艳邮箱
    #msg_to = ['weiwei.uh@haier.com','zhangyan.xian@haier.com','zhangxiangrong2@haier.com','zhanluping@haier.com','caoke@haier.com','1508691067@qq.com']
    # msg_to = ['weiwei.uh@haier.com','1508691067@qq.com']
    # my_send_email(msg_to, result_file)


if __name__=="__main__":
    #后台运行方式
    #nohup python3 Api_Run.py > nohup.log 2>&1 &
    auto_run()
    # OpExcel=Operate_Excel(casefile)
    # OpExcel.creat_excel()
    # msg_to = ['1508691067@qq.com']
    # file_path='D:\\Python_Project\\API_Auto_Test\\result\\result_2021_04_30_09_59_08.xlsx'
    # # test_times=5
    # # sucess_nums=1
    # my_send_email(msg_to,file_path)

    # url = "/emuplus/secuag/account/v1.0/login"
    # body = '{"username":"18161982838", "password":"12345 6","captchaToken":"","captchaAnswer":""}'
    # timestamp = '1616047412445'
    # op=sha256(url,body,timestamp)
    # res=op.get_sign()
    # print(res)
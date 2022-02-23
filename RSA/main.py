# 读取原始excel数据文件，输出RSA加密文本文件
# sample source file:test_data.xls
# sample encode file：encode_file.txt

import pandas as pd
import en_decrypt 

def encode():
    while(1):#打开源数据文件
        source_excelf=input('Please enter the name of the excel file to be encrypted:')
        try:
            df=pd.read_excel(source_excelf)
            break
        except Exception as e:
            print(e)

    encode_file=input('Please enter the generated encrypted file name:')#输入目标加密文件名
    f=open(encode_file,'w')   #打开目标加密文件

    #逐行读取列表数据
    columns=df.columns.values.tolist()
    headmsg=''
    for column in columns:
        headmsg=headmsg+column+','
    headmsg=headmsg[0:-1]
    print(headmsg)
    encodemsg = encrypt_data(headmsg) #RSA加密
    f.writelines(encodemsg)   #将加密数据写入文件

    for idx,row in df.iterrows():
        msg=''
        for column in columns:
            msg=msg+str(row[column])+','
        msg=msg[0:-1]
        print(msg)
        encodemsg = encrypt_data(msg)  # RSA加密,被加密数据最长117字节，否则需增加密钥长度或拆分
        f.writelines('\n'+encodemsg)  # 将加密数据写入文件

    f.close()
    print(encode_file,'加密文件已生成')


def decode_test():     #解密测试
    encode_file = 'encode_file.txt'
    f=open( encode_file,'r')
    lines=f.readlines()
    print('解密测试结果')
    for line in lines:
        decodemsg=decrypt_data(line)
        print(decodemsg)

encode()

#decode_test()    #执行解密测试
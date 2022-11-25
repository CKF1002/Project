from futu import *

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret, data, page_req_key = quote_ctx.request_history_kline('HK.00700', start='2019-09-11', end='2021-09-18',  ktype=KLType.K_DAY, max_count=999999999999)  # 每页5个，请求第一页
if ret == RET_OK:
    print(data)
    try:
        data.to_csv('HK.00700.csv')
    except:
        print('error:', data)
print('All pages are finished!')
quote_ctx.close()  # 结束后记得关闭当条连接，防止连接条数用尽

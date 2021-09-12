import requests

if __name__ == '__main__':
    while True:
        k_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        place = input("请输入一个地址:")
        data = {
            'cname': '',
            'pid': '',
            'keyword': place,
            'pageIndex': '1',  # 第一页
            'pageSize': '40',  # 一页40个
        }
        resp = requests.post(url=k_url, data=data, headers=headers)
        list_data = resp.json()
        for i in list_data['Table1']:
            store = i['storeName']
            address = i['addressDetail']
            print('地点:' + store, '具体位置:' + address + '\n')

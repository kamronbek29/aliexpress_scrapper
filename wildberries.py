import json
import requests


def get_wildberries_item_info(wildberries_id):
    wildberries_url = 'https://www.wildberries.ru/catalog/{}/detail.aspx'.format(wildberries_id)
    get_request = requests.get(wildberries_url)
    get_request_content = get_request.content
    get_request_content_str = str(get_request_content, 'utf-8').replace('\\', '')

    info_json_str = get_request_content_str.split('data: ')[1].split('if (false)')[0]
    info_json_str = info_json_str.split('link')[0].replace(',\n', '')
    info_json = json.loads(info_json_str)

    good_name = info_json['goodsName']
    brand_name = info_json['brandName']
    title = '{0} / {1}'.format(brand_name, good_name)
    image_url = get_request_content_str.split('<meta property="og:image"')[1].split('content="')[1].split('"')[0]

    info_dict = {'title': title, 'image_url': image_url}

    return info_dict


if __name__ == '__main__':
    item_info = get_wildberries_item_info('12920336')
    print(item_info)

    'src="//images.wbstatic.net/big/new/12920000/12920336-1.jpg"'


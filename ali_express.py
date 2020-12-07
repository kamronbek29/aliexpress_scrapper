import requests
import json


class AliExpress(object):
    def __init__(self, express_id):
        self.express_id = express_id

    def get_item(self):
        express_url = 'https://aliexpress.ru/item/{}.html'.format(self.express_id)
        get_request = requests.get(express_url)
        get_request_content = get_request.content
        get_request_content_str = str(get_request_content, 'utf-8')

        info_json_str = get_request_content_str.split('window.runParams = ')[1].split('data: ')[1].split('csrfToken')[0]
        info_json_str_1 = info_json_str.split('"}},\n')[0] + '"}}'
        info_json = json.loads(info_json_str_1)

        items_left = info_json['actionModule']['totalAvailQuantity']

        start_price = info_json['priceModule']['minActivityAmount']['value']
        end_price = info_json['priceModule']['maxActivityAmount']['value']
        image_url = info_json['imageModule']['imagePathList'][0]
        title = info_json['titleModule']['subject']

        item_info_dict = {'items_left': items_left, 'start_price': start_price, 'end_price': end_price,
                          'title': title, 'image_url': image_url}

        return item_info_dict


if __name__ == '__main__':
    express = AliExpress('4001237617664')
    info = express.get_item()
    print(info)


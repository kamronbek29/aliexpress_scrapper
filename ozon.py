import requests


def get_ozon_item_info(ozon_id):
    express_url = 'https://api.ozon.ru/composer-api.bx/page/json/v1?url=%2Fproducts%2F{}%2F'.format(ozon_id)
    get_request = requests.get(express_url)
    request_json = get_request.json()

    title = request_json['pdp']['addToFavorite']['addToFavorite-347772-default-1']['cellTrackingInfo']['product']['title']
    image_url = request_json['pdp']['webGallery']['webGallery-393698-default-1']['coverImage']

    info_dict = {'title': title, 'image_url': image_url}

    return info_dict


if __name__ == '__main__':
    item_info = get_ozon_item_info('198042622')
    print(item_info)

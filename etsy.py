import requests


def get_etsy_item_info(etsy_id):
    etsy_url = 'https://www.etsy.com/listing/{}'.format(etsy_id)
    get_request = requests.get(etsy_url)
    get_request_content = get_request.content
    get_request_content_str = str(get_request_content, 'utf-8').replace('\\', '')

    title = get_request_content_str.split('<title>')[1].split('</title>')[0]
    image_url = get_request_content_str.split('<meta property="og:image" content="')[1].split('"')[0]

    info_dict = {'title': title, 'image_url': image_url}

    return info_dict


if __name__ == '__main__':
    item_info = get_etsy_item_info('765530234')
    print(item_info)



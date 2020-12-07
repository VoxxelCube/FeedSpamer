import parse_module
import vk_api




def captcha_handler(captcha): 

    key = input("Enter captcha code {0}  (Type 'quite' or press Ctrl+C for stopping): ".format(captcha.get_url())).strip() 
    return captcha.try_again(key)

if __name__ == "__main__":

    res = []

    vk_login = input('Phone number for authorization (Format: +7123445667890): ')
    vk_pass = input('Password of account: ')
    search = input('Search query for Avito: ')
    pages = int(input('Page amount: '))

    par = parse_module.Parser()

    vk_session = vk_api.VkApi(vk_login, vk_pass, captcha_handler=captcha_handler) 

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)

    vk = vk_session.get_api()

    

    if pages > 1:
        for i in range(pages):
            par.parse(f'https://www.avito.ru/rossiya?p={i}&q={search}', res)
    else:
        par.parse(f'https://www.avito.ru/rossiya?q={search}', res)
    
    for result in res:
        

        print(vk.wall.post(message=f'Смотри, что нашёл!\n 🔥🔥🔥{result["title"]}🔥🔥🔥\n Всего за {result["price"]}!\n Успей купить, пока Хафи Грязючка не покарал тебя!\n', attachments = f'{result["link"]}')['post_id'])



    

   
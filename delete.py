import vk_api

def captcha_handler(captcha):

    key = input("Enter captcha code {0}  (Type 'quite' or press Ctrl+C for stopping): ".format(captcha.get_url())).strip()
    if key == 'quit':
        pass
    return captcha.try_again(key)

vk_login = input('Phone number for authorization (Format: +7123445667890): ')
vk_pass = input('Password of account: ')

first_post_id = int(input('Post id of first post (number in terminal): '))
last_post_id = int(input('Post id of last post: '))

vk_session = vk_api.VkApi(vk_login, vk_pass, captcha_handler=captcha_handler)
vk_session.auth()

vk = vk_session.get_api()

for i in range(first_post_id, last_post_id + 1):
    vk.wall.delete(post_id = f'{i}')
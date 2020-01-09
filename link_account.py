import dropbox


def link_acc():
    app_key = '05edkw3y5uun47z'
    app_secret = 'orbvhpaj4i7w41w'

    flow = dropbox.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

    authorise_url = flow.start()

    print('1. Go to:' +authorise_url)
    print('2. Click "Allow" (you might have to log in first)')
    print('3. Copy the authorisation code')
    code = input('Enter your code:'.strip())

    access_token, user_id = flow.finish(code)

    client = dropbox.client.DropboxClient(access_token)
    print('linked account', client.account_info())

    print('.....One Pocess Done......')
    print('\n')

link_acc()


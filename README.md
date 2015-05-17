## About

Basic module for `recon-ng` framework to enumerate vkontakte contacts. Based on my [vkrecon](https://github.com/lctrcl/vkrecon) script.

You need to add 'vkontakte_token' to KEY_RESOURCES in the `core/base.py` of the recon-ng.

Then you have to retrieve token for VK - [https://vk.com/dev/auth_mobile](https://vk.com/dev/auth_mobile), [https://vk.com/dev/authentication](https://vk.com/dev/authentication). 

If you don't want to go full dev way, you can retrieve token via some app like [https://oauth.vk.com/authorize?client_id=35569&scope=groups&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.0&response_type=token](https://oauth.vk.com/authorize?client_id=35569&scope=groups&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.0&response_type=token) (use it on your own risk).

Copy `vkontakte.py` into `modules/recon/companies-contacts/`.

## Usage

Launch recon-ng

    workspace add test
    keys add vkontakte_token <your_VK_token>
    add companies # add companies you want to investigate
    use recon/companies-contacts/vkontakte # or just 'use vk'
    run

After that you will have contacts populated with users that have company set in the profile.


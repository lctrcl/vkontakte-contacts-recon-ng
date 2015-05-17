# packages required for framework integration
# # -*- coding: utf8 -*-
import module

class Module(module.Module):

    def __init__(self, params):
        module.Module.__init__(self, params, query='SELECT DISTINCT company FROM companies WHERE company IS NOT NULL')
        self.info = {
            'Name': 'Vkontakte Contact Enumerator',
            'Author': 'Igor Ivanov (@lctrcl)',
            'Version': 'v0.0.1',
            'Description': 'Harvests contacts from vk.com. Updates the \'contacts\' table with the results',
            }
        self.basevkurl = 'https://api.vk.com/method/'

    def module_run(self, companies):
        token = self.get_key('vkontakte_token')
        if self.login(token):
            for company in companies:
                self.heading(company, level=0)
                self.get_contacts(company,token)
                print company

    def login(self, token):
        if token:
            url  = self.basevkurl +  u'users.get?user_ids=1&access_token=%s' % token
            resp = self.request(url)
            if resp.status_code == 200:
                return True
        else:
            return False

    def get_contacts(self, company, token):
        method = 'users.search'
        url = self.basevkurl + method
        resp = self.request(url, payload = {'company': company, 'access_token': token, 'fields': 'contacts'})
        for user in resp.json['response']:
            if type(user) is not int:
                name = user[u'first_name']
                last_name = user[u'last_name']
                uid = user[u'uid']
                self.output('%s - %s, ID: %s' % (name, last_name, uid))
                self.add_contacts(first_name=name,  last_name=last_name)
        return

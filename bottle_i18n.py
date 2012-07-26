import gettext
import os
import re

from bottle import PluginError, request

from utils import LOG

# Format of http.request.header.Accept-Language.
# refs: http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4
REQUEST_ACCEPT_LANGUAGE_RE = re.compile(r'''
        ([A-Za-z]{1,8}(?:-[A-Za-z]{1,8})*|\*)   # "en", "en-au", "*"
        (?:;q=(0(?:\.\d{,3})?|1(?:.0{,3})?))?   # Optional "q=1.00", "q=0.8"
        (?:\s*,\s*|$)                           # Multiple accepts per header.
        ''', re.VERBOSE)

class I18NPlugin(object):
    name = 'i18n'
    api = 2

    def __init__(self, domain, locale_dir=None, lang_code=None):
        self.domain = domain
        if locale_dir is None:
            locale_dir = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locale'))
        if not os.path.exists(locale_dir):
            raise PluginError('No locale directory found, please assign a right one.')
        self.locale_dir = locale_dir
        self.lang_code = lang_code
        
        self.prepared = {}
        self.app = None
    
    def setup(self, app):
        self.app = app
        self.app._ = lambda s: s
        self.app.set_lang = self.prepare
        self.app.hooks.add('before_request', self.prepare)

    def extra_client_expected_langs(self):
        """Return language list from http.request.header.Accept-Languag, ordered by 'q'."""
        result = []
        pieces = REQUEST_ACCEPT_LANGUAGE_RE.split(request.headers.get('Accept-Language', ''))
        if pieces[-1]:
            return []
        for i in range(0, len(pieces)-1, 3):
            first, lang, priority = pieces[i : i + 3]
            if first:
                return []
            priority = priority and float(priority) or 1.0
            result.append((lang, priority))
        result.sort(key=lambda k: k[1], reverse=True)
        return result
        
    def get_language_list(self):
        if self.lang_code is not None:
            return [self.lang_code]

        expected_langs = self.extra_client_expected_langs()
        LOG.debug('web client accept langs: %s', expected_langs)

        lang_codes = []
        
        for lang, priority in expected_langs:
            lang_country = lang.split('-')
            if len(lang_country) == 1:
                lang_codes.append(lang)
                continue
            country = lang_country[1]
            lang_codes.append('%s_%s' % (lang_country[0], country))
            lang_codes.append('%s_%s' % (lang_country[0], country.swapcase()))

        return lang_codes
   
    def prepare(self, langs=None):
        LOG.debug('bottle request.headers.keys %s', request.headers.get('Accept-Language', None))
        if langs is None:
            langs = self.get_language_list()
            LOG.debug('web client accept langs: %s', langs)
        
        prepared_key = tuple(langs)
        if prepared_key in self.prepared:
            trans = self.prepared.get(prepared_key)
            if trans:
                trans.install(True)
                self.app._ = trans.gettext
            else:
                self.app._ = lambda s: s
            return
        
        LOG.debug('setup i18n ...')
        try:
            trans = gettext.translation(self.domain, self.locale_dir, languages=langs)
            trans.install(True)
            self.app._ = trans.gettext
            self.prepared[prepared_key] = trans
        except Exception, e:
            LOG.warn('can not install application for language "%s" with locale path as "%s"', langs, self.locale_dir)
            LOG.warn(e)
            self.app._ = lambda s: s
            self.prepared[prepared_key] = None

    def apply(self, callback, context):
        return callback
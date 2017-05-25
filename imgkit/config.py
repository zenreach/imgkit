# -*- coding: utf-8 -*-
import subprocess
import sys


def _find_process(name):
    if sys.platform == 'win32':
        return subprocess.Popen(['where', name], stdout=subprocess.PIPE).communicate()[0].strip()
    else:
        return subprocess.Popen(['which', name], stdout=subprocess.PIPE).communicate()[0].strip()


class Config(object):
    def __init__(self, wkhtmltoimage='', meta_tag_prefix='imgkit-', xvfb='', headless=False):
        self.meta_tag_prefix = meta_tag_prefix

        self.headless = headless
        self.xvfb = xvfb
        self.wkhtmltoimage = wkhtmltoimage

        if not self.wkhtmltoimage:
            self.wkhtmltoimage = _find_process('wkhtmltoimage')

        try:
            with open(self.wkhtmltoimage) as f:
                pass
        except IOError:
            raise IOError('No wkhtmltoimage executable found: "%s"\n'
                          'If this file exists please check that this process can '
                          'read it. Otherwise please install wkhtmltopdf - '
                          'http://wkhtmltopdf.org' % self.wkhtmltoimage)

        if headless:
            if not self.xvfb:
                self.xvfb = _find_process('xvfb')

            try:
                with open(self.xvfb) as f:
                    pass
            except IOError:
                raise IOError('No xvfb executable found: "%s"\n'
                              'If this file exists please check that this process can '
                              'read it. Otherwise please install xvfb' % self.xvfb)

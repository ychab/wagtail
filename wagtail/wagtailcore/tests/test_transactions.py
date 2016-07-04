from __future__ import absolute_import, unicode_literals

from django.test import TransactionTestCase

from wagtail.wagtailcore.models import Page


class InitialDataTestCase(TransactionTestCase):

    def setUp(self):
        self.root_page = Page.objects.get(slug='root')

    def test_a(self):
        pass

    def test_b(self):
        pass

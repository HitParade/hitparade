import os

from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured

from hitparade.utils import *
from types import *

from hitparade.tests.helpers import HPUnitTestCase

import sure

class HPUtilTestCase(HPUnitTestCase):


    def test_v_url(self):

        settings.ALLOWED_VERSIONS = ['v1', 'v2']
        v_url("pattern").should.equal(r"^(?P<version>(v1|v2))/pattern")

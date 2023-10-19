# -*- coding: utf-8 -*-
#
# MIT License
# 
# Copyright (c) 2023 Hiway Media
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
from unittest import mock
import requests
from ..constants import *
from httmock import urlmatch, response, HTTMock, all_requests
#
try:
    import unittest
except ImportError:
    import unittest2 as unittest
#
#
class TestConnection(unittest.TestCase):
    #
    def setUp(self):
        self._conn = requests.Session()
    #
    #@all_requests
    #def response_content_success(self, url, request):
    #    headers = {'content-type': 'application/json'}
    #    content = b'response_ok'
    #    return response(200, content, headers, None, 5, request)
    #
    #def test_raw_get(self):
    #    with HTTMock(self.response_content_success):
    #        resp = self._conn.get(TNGRM_BASE_URL + "/health")
    #    self.assertEqual(resp.content, b'response_ok')
    #    self.assertEqual(resp.status_code, 200)
    #
#
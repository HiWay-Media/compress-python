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
    
    @all_requests
    def response_content_success(self, url, request):
        headers = {'content-type': 'application/json'}
        content = b'response_ok'
        return response(200, content, headers, None, 5, request)
    #


    def test_raw_get(self):
        with HTTMock(self.response_content_success):
            resp = self._conn.raw_get("/known_path")
        self.assertEqual(resp.content, b'response_ok')
        self.assertEqual(resp.status_code, 200)

    def test_raw_post(self):
        @urlmatch(path="/known_path", method="post")
        def response_post_success(url, request):
            headers = {'content-type': 'application/json'}
            content = 'response'.encode("utf-8")
            return response(201, content, headers, None, 5, request)

        with HTTMock(response_post_success):
            resp = self._conn.raw_post("/known_path",
                                       {'field': 'value'})
        self.assertEqual(resp.content, b'response')
        self.assertEqual(resp.status_code, 201)

    def test_raw_put(self):
        @urlmatch(netloc="localhost", path="/known_path", method="put")
        def response_put_success(url, request):
            headers = {'content-type': 'application/json'}
            content = 'response'.encode("utf-8")
            return response(200, content, headers, None, 5, request)

        with HTTMock(response_put_success):
            resp = self._conn.raw_put("/known_path",
                                      {'field': 'value'})
        self.assertEqual(resp.content, b'response')
        self.assertEqual(resp.status_code, 200)

    def test_raw_get_fail(self):
        @urlmatch(netloc="localhost", path="/known_path", method="get")
        def response_get_fail(url, request):
            headers = {'content-type': 'application/json'}
            content = "404 page not found".encode("utf-8")
            return response(404, content, headers, None, 5, request)

        with HTTMock(response_get_fail):
            resp = self._conn.raw_get("/known_path")

        self.assertEqual(resp.content, b"404 page not found")
        self.assertEqual(resp.status_code, 404)

    def test_raw_post_fail(self):
        @urlmatch(netloc="localhost", path="/known_path", method="post")
        def response_post_fail(url, request):
            headers = {'content-type': 'application/json'}
            content = str(["Start can't be blank"]).encode("utf-8")
            return response(404, content, headers, None, 5, request)

        with HTTMock(response_post_fail):
            resp = self._conn.raw_post("/known_path",
                                       {'field': 'value'})
        self.assertEqual(resp.content, str(["Start can't be blank"]).encode("utf-8"))
        self.assertEqual(resp.status_code, 404)

    def test_raw_put_fail(self):
        @urlmatch(netloc="localhost", path="/known_path", method="put")
        def response_put_fail(url, request):
            headers = {'content-type': 'application/json'}
            content = str(["Start can't be blank"]).encode("utf-8")
            return response(404, content, headers, None, 5, request)

        with HTTMock(response_put_fail):
            resp = self._conn.raw_put("/known_path",
                                      {'field': 'value'})
        self.assertEqual(resp.content, str(["Start can't be blank"]).encode("utf-8"))
        self.assertEqual(resp.status_code, 404)

    def test_add_param_headers(self):
        self._conn.add_param_headers("test", "value")
        self.assertEqual(self._conn.headers,
                         {"test": "value"})

    def test_del_param_headers(self):
        self._conn.add_param_headers("test", "value")
        self._conn.del_param_headers("test")
        self.assertEqual(self._conn.headers, {})

    def test_clean_param_headers(self):
        self._conn.add_param_headers("test", "value")
        self.assertEqual(self._conn.headers,
                         {"test": "value"})
        self._conn.clean_headers()
        self.assertEqual(self._conn.headers, {})

    def test_exist_param_headers(self):
        self._conn.add_param_headers("test", "value")
        self.assertTrue(self._conn.exist_param_headers("test"))
        self.assertFalse(self._conn.exist_param_headers("test_no"))

    def test_get_param_headers(self):
        self._conn.add_param_headers("test", "value")
        self.assertTrue(self._conn.exist_param_headers("test"))
        self.assertFalse(self._conn.exist_param_headers("test_no"))

    def test_get_headers(self):
        self._conn.add_param_headers("test", "value")
        self.assertEqual(self._conn.headers,
                         {"test": "value"})


#
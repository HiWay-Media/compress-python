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
import requests, json
#
from .constants import *
#from builtins   import isinstance
#from typing     import Dict, List
#
#
class CompressClient:
    #
    api_key: str
    customer_name: str
    client_id : str
    req : requests
    #
    def __init__(self, api_key :str , customer_name : str):
        self.api_key        = api_key
        self.customer_name  = customer_name
        self.req            = requests.Session()
        self.client_id      = customer_name + "_client"
    #
    #/**
    # *
    # * @param {string} apikey
    # * @param {string} customer
    # * @returns in data {
    #      "total": 4608,
    #      "used": 1965
    #  }
    # */
    def get_s3_space(self):
        return self.req.post(TNGRM_BASE_URL + S3_SPACE, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
            }),
        )
    #
    # /**
    # *
    # * @param {string} apikey
    # * @param {string} customer
    # * @returns list of categories of the customer
    # */
    def get_categories(self):
        return self.req.post(TNGRM_BASE_URL + GET_CATEGORIES, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
            })
        )
    #
    #/**
    # *
    # * @param {string} apikey
    # * @param {string} customer
    # * @returns list of categories of the customer
    # */
    def create_category(self, category_name : str): 
        return self.req.post(TNGRM_BASE_URL + GET_CATEGORIES, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
                "category_name": category_name
            })
        )
    #
    #/**
    # * upload video to minio s3 bucket with a presigned PUT url
    # *
    # * videos will not be displayed in compress platform,
    # *
    # * this is just a plain upload to s3 storage
    # * @param {string} destination_folder
    # * @param {string} filename
    # * @param {file} file
    # */
    def upload_s3(self, destination_folder : str, filename : str, filename ):
        file_dest = destination_folder + "/" + filename
        r = self.req.post(TNGRM_BASE_URL + PRESIGNED_URL_S3, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "customer": self.customer_name,
                "filename": file_dest
            })
        )

#
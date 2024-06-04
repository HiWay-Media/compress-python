# -*- coding: utf-8 -*-
#
# MIT License
# 
# Copyright (c) 2023-2024 Hiway Media
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
    def upload_s3(self, destination_folder : str, filename : str, file ):
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
    # /**
    # * @param {file} file_thumb 
    # * @returns 
    # */
    def add_video_thumb(self, file_thumb):
        return self.req.post(TNGRM_BASE_URL + ADD_VIDEO_THUMB, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "client_id": self.client_id,
                "filename": file_thumb
            })
        )
    #
    #/**
    # * upload video with compress encoding
    # *
    # * if destination folder is empty, it will upload to the root of the bucket
    # *
    # * remember to specify the folder (usually upload)
    # *
    # * @param {string} destination_folder 
    # * @param {file} file 
    # * @param {string} title 
    # * @param {string} tags 
    # * @param {string} location_place 
    # * @param {number} category_id 
    # */
    def upload_with_encoding( self, destination_folder : str, file, title : str, tags : str, location_place : str, category_id : str):
        #
        file_dest = destination_folder + "/" + fileName;
        #< wait until the file is uploaded
        print("uploading fileName to minio S3...")
        upload =  self.upload_s3(destination_folder, file, fileName);
        #
        return self.req.post(TNGRM_BASE_URL + CREATE_UPLOAD, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": this.api_key,
                "title": title,
                "tags": tags,
                #"category": parseInt(category_id),
                "location": location_place,
                "filename": file_dest,
                #"size": parseInt(file.size),
                "reporter_email": self.customer_name +"@tngrm.io",
            })
        )
    #
    #/**
    # * 
    # * @param {number} start_from 
    # * @param {number} amount 
    # * @returns restreamer list
    # */
    def get_restreamers(self, start_from :int, amount :int):
        return self.req.post(TNGRM_BASE_URL + GET_RESTREAMERS, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
                "start_from": int(start_from),
                "amount": int(amount)
            })
        )
    #
    #/**
    # * 
    # * @returns restreamer object
    # */
    def get_restreamer(self, instance_name : str):
        return self.req.post(TNGRM_BASE_URL + GET_RUNNING_SINGLE_INSTANCE, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
                "instance_name": instance_name,
            })
        )
    #
    #/**
    # * 
    # * @returns restreamer list running
    # */
    def get_running_instances(self):
        return self.req.post(TNGRM_BASE_URL + GET_RUNNING_INSTANCES, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
            })
        )
        #
    #
    # /**
    # * scale the restreamer to turn it on / off
    # * accept value 0 or 1
    # * @param {string} restreamer_name 
    # * @param {number} scale_value 
    # * @returns 
    # */
    def scale_restreamer(self, restreamer_name : str, scale_value: int): 
        return self.req.post(TNGRM_BASE_URL + SCALE_RESTREAMER, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
                "instance_name": restreamer_name,
                "scale": int(scale_value)
            })
        )
    #
    # /**
    # * hls start
    # * 
	# ApiKey   string `json:"api_key" `
	# ClientId string `json:"client_id" `
	# InstanceName   string `json:"instance_name" `
	# StreamProtocol string `json:"stream_protocol" `
    # * @returns 
    # */
    def hls_start(self, restreamer_name : str, stream_protocol: str ): 
        return self.req.post(TNGRM_BASE_URL + RESTREAMER_HLS_START, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
                "instance_name": restreamer_name,
                "stream_protocol": stream_protocol
            })
        )
    #
    # /**
    # * hls stop
    # * 
	# ApiKey   string `json:"api_key" `
	# ClientId string `json:"client_id" `
	# InstanceName   string `json:"instance_name" `
	# StreamProtocol string `json:"stream_protocol" `
    # * @returns 
    # */
    def hls_stop(self, restreamer_name : str, stream_protocol: str ): 
        return self.req.post(TNGRM_BASE_URL + RESTREAMER_HLS_STOP, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
                "instance_name": restreamer_name,
                "stream_protocol": stream_protocol
            })
        )
    #
    #
    # /** TODO:
    # * restreamer push start
    # * 
	# ApiKey   string `json:"api_key" `
	# ClientId string `json:"client_id" `
	# InstanceName   string `json:"instance_name" `
	# ExternalServers []struct {
	#	ExternalServer string `json:"external_server" `
	#	IngestProtocol string `json:"ingest_protocol" `
	#	AudioChannel   string `json:"audio_channel" `
	#} `json:"external_servers"`
    # * @returns 
    # */
    def push_start(self, restreamer_name : str, external_servers: object ): 
        return self.req.post(TNGRM_BASE_URL + RESTREAMER_PUSH_START, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
                "instance_name": restreamer_name,
            })
        )
    #
    # /** TODO:
    # * restreamer push stop
    # * 
	# ApiKey   string `json:"api_key" `
	# ClientId string `json:"client_id" `
	# InstanceName   string `json:"instance_name" `
	# ExternalServers []struct {
	#	ExternalServer string `json:"external_server" `
	#	IngestProtocol string `json:"ingest_protocol" `
	#	AudioChannel   string `json:"audio_channel" `
	#} `json:"external_servers"`
    # * @returns 
    # */
    def push_stop(self, restreamer_name : str, external_servers: object ): 
        return self.req.post(TNGRM_BASE_URL + RESTREAMER_PUSH_STOP, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
                "instance_name": restreamer_name,
            })
        )
    #
    # /** TODO: need to understand if is used or no 
    # * RESTREAMER_PULL_START push stop
    # * 
	# ApiKey   string `json:"api_key" `
	# ClientId string `json:"client_id" `
	# InstanceName   string `json:"instance_name" `
	# ExternalServers []struct {
	#	ProcessID string `json:"process_id" `
	#} `json:"external_servers"`
    # * @returns 
    # */
    def pull_start(self, restreamer_name : str, external_servers: object ): 
        return self.req.post(TNGRM_BASE_URL + RESTREAMER_PULL_START, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
                "instance_name": restreamer_name,
            })
        )
    #
    # /** TODO: need to understand if is used or no 
    # * RESTREAMER_PULL_START push stop
    # * 
	# ApiKey   string `json:"api_key" `
	# ClientId string `json:"client_id" `
	# InstanceName   string `json:"instance_name" `
	# ExternalServers []struct {
	#	ProcessID string `json:"process_id" `
	#} `json:"external_servers"`
    # * @returns 
    # */
    def pull_start(self, restreamer_name : str, external_servers: object ): 
        return self.req.post(TNGRM_BASE_URL + RESTREAMER_PULL_STOP, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
                "instance_name": restreamer_name,
            })
        )
    #


    #/**
    # * Need to call before upload s3
    # * 
    # * @returns customer_s3
    # */
    def get_zone(self, ):
        return self.req.post(TNGRM_BASE_URL + GET_CUSTOMER_ZONE, 
            headers={
                "Content-Type": "application/json",
            },
            body = json.dumps({
                "api_key": self.api_key,
                "client_id": self.client_id,
            })
        )
#
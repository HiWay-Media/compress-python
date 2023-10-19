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
TNGRM_BASE_URL                 = "https://api.tngrm.io/api/v3.0"
#AUTH_LOGIN                     = "/external/auth/login"
GET_CATEGORIES                 = "/external/upload/categories"
CREATE_CATEGORY                = GET_CATEGORIES + "/create"
#
GET_RESTREAMERS                = "/external/restreamers"
GET_RUNNING_INSTANCES          = GET_RESTREAMERS + "/running_instances"
GET_RUNNING_SINGLE_INSTANCE    = GET_RESTREAMERS + "/single_instance"
SCALE_RESTREAMER               = GET_RESTREAMERS + "/scale_instance"
#
GET_UPLOADS                    = "/external/upload"
GET_SINGLE_UPLOAD              = GET_UPLOADS + "/jobid"
SET_PUBLISHED_UPLOAD           = GET_UPLOADS + "/set_published"
CREATE_UPLOAD                  = GET_UPLOADS + "/create"
PRESIGNED_URL_S3               = GET_UPLOADS + "/presignedUrl"
S3_SPACE                       = GET_UPLOADS + "/s3_space"
ADD_VIDEO_THUMB                = GET_UPLOADS + "/add_thumb"
SIGN_S3_URL                    = GET_UPLOADS + "/sign_s3_url"
#
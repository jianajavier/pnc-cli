#!/usr/bin/env python
"""
BuildconfigsetrecordsApi.py
Copyright 2015 Reverb Technologies, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os
import urllib

from models import *


class BuildconfigsetrecordsApi(object):

    def __init__(self, api_client):
      self.api_client = api_client

    
    def getAll(self, **kwargs):
        """Gets all build config set execution records

        Args:
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            q, str: RSQL query (required)
            
        Returns: 
        """

        all_params = ['pageIndex', 'pageSize', 'sort', 'q']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAll" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/build-config-set-records'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        
        if 'pageIndex' in params:
            query_params['pageIndex'] = self.api_client.to_path_value(params['pageIndex'])
        
        if 'pageSize' in params:
            query_params['pageSize'] = self.api_client.to_path_value(params['pageSize'])
        
        if 'sort' in params:
            query_params['sort'] = self.api_client.to_path_value(params['sort'])
        
        if 'q' in params:
            query_params['q'] = self.api_client.to_path_value(params['q'])
        

        

        

        

        

        post_data = (form_params if form_params else body_param)

        response = self.api_client.callAPI(resource_path, method, query_params,
                                          post_data, header_params, files=files)
        return response

   
    def getSpecific(self, **kwargs):
        """Gets specific build config set execution record

        Args:
            
            id, int: BuildConfigSetRecord id (required)
            
        Returns: 
        """

        all_params = ['id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSpecific" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/build-config-set-records/{id}'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        

        

        
        if 'id' in params:
            replacement = str(self.api_client.to_path_value(params['id']))
            replacement = urllib.quote(replacement)
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)
        

        

        

        post_data = (form_params if form_params else body_param)

        response = self.api_client.callAPI(resource_path, method, query_params,
                                          post_data, header_params, files=files)
        return response

   
    def getBuildRecords(self, **kwargs):
        """Gets the build records associated with this set

        Args:
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            q, str: RSQL query (required)
            
            id, int: Build Config set record id (required)
            
        Returns: 
        """

        all_params = ['pageIndex', 'pageSize', 'sort', 'q', 'id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method getBuildRecords" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/build-config-set-records/{id}/build-records'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        
        if 'pageIndex' in params:
            query_params['pageIndex'] = self.api_client.to_path_value(params['pageIndex'])
        
        if 'pageSize' in params:
            query_params['pageSize'] = self.api_client.to_path_value(params['pageSize'])
        
        if 'sort' in params:
            query_params['sort'] = self.api_client.to_path_value(params['sort'])
        
        if 'q' in params:
            query_params['q'] = self.api_client.to_path_value(params['q'])
        

        

        
        if 'id' in params:
            replacement = str(self.api_client.to_path_value(params['id']))
            replacement = urllib.quote(replacement)
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)
        

        

        

        post_data = (form_params if form_params else body_param)

        response = self.api_client.callAPI(resource_path, method, query_params,
                                          post_data, header_params, files=files)
        return response

   

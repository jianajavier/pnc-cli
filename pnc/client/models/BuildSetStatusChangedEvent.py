#!/usr/bin/env python
"""
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
"""

class BuildSetStatusChangedEvent(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'userId': 'int',
            
            
            'newStatus': 'BuildSetStatus',
            
            
            'buildSetConfigurationId': 'int',
            
            
            'buildSetTaskId': 'int',
            
            
            'oldStatus': 'BuildSetStatus'
            
        }

        self.attributeMap = {
            
            'userId': 'userId',
            
            'newStatus': 'newStatus',
            
            'buildSetConfigurationId': 'buildSetConfigurationId',
            
            'buildSetTaskId': 'buildSetTaskId',
            
            'oldStatus': 'oldStatus'
            
        }       

        
        
        self.userId = None # int
        
        
        self.newStatus = None # BuildSetStatus
        
        
        self.buildSetConfigurationId = None # int
        
        
        self.buildSetTaskId = None # int
        
        
        self.oldStatus = None # BuildSetStatus
        

# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from pprint import pformat
from six import iteritems


class IdRev(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        """
        IdRev - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'rev': 'int',
            'field_handler': 'FieldHandler'
        }

        self.attribute_map = {
            'id': 'id',
            'rev': 'rev',
            'field_handler': 'fieldHandler'
        }

        self._id = None
        self._rev = None
        self._field_handler = None

    @property
    def id(self):
        """
        Gets the id of this IdRev.


        :return: The id of this IdRev.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IdRev.


        :param id: The id of this IdRev.
        :type: int
        """
        self._id = id

    @property
    def rev(self):
        """
        Gets the rev of this IdRev.


        :return: The rev of this IdRev.
        :rtype: int
        """
        return self._rev

    @rev.setter
    def rev(self, rev):
        """
        Sets the rev of this IdRev.


        :param rev: The rev of this IdRev.
        :type: int
        """
        self._rev = rev

    @property
    def field_handler(self):
        """
        Gets the field_handler of this IdRev.


        :return: The field_handler of this IdRev.
        :rtype: FieldHandler
        """
        return self._field_handler

    @field_handler.setter
    def field_handler(self, field_handler):
        """
        Sets the field_handler of this IdRev.


        :param field_handler: The field_handler of this IdRev.
        :type: FieldHandler
        """
        self._field_handler = field_handler

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, datetime):
                result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

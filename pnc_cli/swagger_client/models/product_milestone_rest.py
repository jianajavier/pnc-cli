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


class ProductMilestoneRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        """
        ProductMilestoneRest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'version': 'str',
            'end_date': 'datetime',
            'starting_date': 'datetime',
            'planned_end_date': 'datetime',
            'download_url': 'str',
            'product_version_id': 'int',
            'performed_build_record_set_id': 'int',
            'distributed_build_record_set_id': 'int',
            'product_release_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'version': 'version',
            'end_date': 'endDate',
            'starting_date': 'startingDate',
            'planned_end_date': 'plannedEndDate',
            'download_url': 'downloadUrl',
            'product_version_id': 'productVersionId',
            'performed_build_record_set_id': 'performedBuildRecordSetId',
            'distributed_build_record_set_id': 'distributedBuildRecordSetId',
            'product_release_id': 'productReleaseId'
        }

        self._id = None
        self._version = None
        self._end_date = None
        self._starting_date = None
        self._planned_end_date = None
        self._download_url = None
        self._product_version_id = None
        self._performed_build_record_set_id = None
        self._distributed_build_record_set_id = None
        self._product_release_id = None

    @property
    def id(self):
        """
        Gets the id of this ProductMilestoneRest.


        :return: The id of this ProductMilestoneRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductMilestoneRest.


        :param id: The id of this ProductMilestoneRest.
        :type: int
        """
        self._id = id

    @property
    def version(self):
        """
        Gets the version of this ProductMilestoneRest.


        :return: The version of this ProductMilestoneRest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ProductMilestoneRest.


        :param version: The version of this ProductMilestoneRest.
        :type: str
        """
        self._version = version

    @property
    def end_date(self):
        """
        Gets the end_date of this ProductMilestoneRest.


        :return: The end_date of this ProductMilestoneRest.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this ProductMilestoneRest.


        :param end_date: The end_date of this ProductMilestoneRest.
        :type: datetime
        """
        self._end_date = end_date

    @property
    def starting_date(self):
        """
        Gets the starting_date of this ProductMilestoneRest.


        :return: The starting_date of this ProductMilestoneRest.
        :rtype: datetime
        """
        return self._starting_date

    @starting_date.setter
    def starting_date(self, starting_date):
        """
        Sets the starting_date of this ProductMilestoneRest.


        :param starting_date: The starting_date of this ProductMilestoneRest.
        :type: datetime
        """
        self._starting_date = starting_date

    @property
    def planned_end_date(self):
        """
        Gets the planned_end_date of this ProductMilestoneRest.


        :return: The planned_end_date of this ProductMilestoneRest.
        :rtype: datetime
        """
        return self._planned_end_date

    @planned_end_date.setter
    def planned_end_date(self, planned_end_date):
        """
        Sets the planned_end_date of this ProductMilestoneRest.


        :param planned_end_date: The planned_end_date of this ProductMilestoneRest.
        :type: datetime
        """
        self._planned_end_date = planned_end_date

    @property
    def download_url(self):
        """
        Gets the download_url of this ProductMilestoneRest.


        :return: The download_url of this ProductMilestoneRest.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url of this ProductMilestoneRest.


        :param download_url: The download_url of this ProductMilestoneRest.
        :type: str
        """
        self._download_url = download_url

    @property
    def product_version_id(self):
        """
        Gets the product_version_id of this ProductMilestoneRest.


        :return: The product_version_id of this ProductMilestoneRest.
        :rtype: int
        """
        return self._product_version_id

    @product_version_id.setter
    def product_version_id(self, product_version_id):
        """
        Sets the product_version_id of this ProductMilestoneRest.


        :param product_version_id: The product_version_id of this ProductMilestoneRest.
        :type: int
        """
        self._product_version_id = product_version_id

    @property
    def performed_build_record_set_id(self):
        """
        Gets the performed_build_record_set_id of this ProductMilestoneRest.


        :return: The performed_build_record_set_id of this ProductMilestoneRest.
        :rtype: int
        """
        return self._performed_build_record_set_id

    @performed_build_record_set_id.setter
    def performed_build_record_set_id(self, performed_build_record_set_id):
        """
        Sets the performed_build_record_set_id of this ProductMilestoneRest.


        :param performed_build_record_set_id: The performed_build_record_set_id of this ProductMilestoneRest.
        :type: int
        """
        self._performed_build_record_set_id = performed_build_record_set_id

    @property
    def distributed_build_record_set_id(self):
        """
        Gets the distributed_build_record_set_id of this ProductMilestoneRest.


        :return: The distributed_build_record_set_id of this ProductMilestoneRest.
        :rtype: int
        """
        return self._distributed_build_record_set_id

    @distributed_build_record_set_id.setter
    def distributed_build_record_set_id(self, distributed_build_record_set_id):
        """
        Sets the distributed_build_record_set_id of this ProductMilestoneRest.


        :param distributed_build_record_set_id: The distributed_build_record_set_id of this ProductMilestoneRest.
        :type: int
        """
        self._distributed_build_record_set_id = distributed_build_record_set_id

    @property
    def product_release_id(self):
        """
        Gets the product_release_id of this ProductMilestoneRest.


        :return: The product_release_id of this ProductMilestoneRest.
        :rtype: int
        """
        return self._product_release_id

    @product_release_id.setter
    def product_release_id(self, product_release_id):
        """
        Sets the product_release_id of this ProductMilestoneRest.


        :param product_release_id: The product_release_id of this ProductMilestoneRest.
        :type: int
        """
        self._product_release_id = product_release_id

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

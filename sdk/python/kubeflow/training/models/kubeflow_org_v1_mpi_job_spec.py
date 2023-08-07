# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.training.configuration import Configuration


class KubeflowOrgV1MPIJobSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'clean_pod_policy': 'str',
        'main_container': 'str',
        'mpi_replica_specs': 'dict(str, V1ReplicaSpec)',
        'run_policy': 'V1RunPolicy',
        'slots_per_worker': 'int'
    }

    attribute_map = {
        'clean_pod_policy': 'cleanPodPolicy',
        'main_container': 'mainContainer',
        'mpi_replica_specs': 'mpiReplicaSpecs',
        'run_policy': 'runPolicy',
        'slots_per_worker': 'slotsPerWorker'
    }

    def __init__(self, clean_pod_policy=None, main_container=None, mpi_replica_specs=None, run_policy=None, slots_per_worker=None, local_vars_configuration=None):  # noqa: E501
        """KubeflowOrgV1MPIJobSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._clean_pod_policy = None
        self._main_container = None
        self._mpi_replica_specs = None
        self._run_policy = None
        self._slots_per_worker = None
        self.discriminator = None

        if clean_pod_policy is not None:
            self.clean_pod_policy = clean_pod_policy
        if main_container is not None:
            self.main_container = main_container
        self.mpi_replica_specs = mpi_replica_specs
        if run_policy is not None:
            self.run_policy = run_policy
        if slots_per_worker is not None:
            self.slots_per_worker = slots_per_worker

    @property
    def clean_pod_policy(self):
        """Gets the clean_pod_policy of this KubeflowOrgV1MPIJobSpec.  # noqa: E501

        CleanPodPolicy defines the policy that whether to kill pods after the job completes. Defaults to None.  # noqa: E501

        :return: The clean_pod_policy of this KubeflowOrgV1MPIJobSpec.  # noqa: E501
        :rtype: str
        """
        return self._clean_pod_policy

    @clean_pod_policy.setter
    def clean_pod_policy(self, clean_pod_policy):
        """Sets the clean_pod_policy of this KubeflowOrgV1MPIJobSpec.

        CleanPodPolicy defines the policy that whether to kill pods after the job completes. Defaults to None.  # noqa: E501

        :param clean_pod_policy: The clean_pod_policy of this KubeflowOrgV1MPIJobSpec.  # noqa: E501
        :type: str
        """

        self._clean_pod_policy = clean_pod_policy

    @property
    def main_container(self):
        """Gets the main_container of this KubeflowOrgV1MPIJobSpec.  # noqa: E501

        MainContainer specifies name of the main container which executes the MPI code.  # noqa: E501

        :return: The main_container of this KubeflowOrgV1MPIJobSpec.  # noqa: E501
        :rtype: str
        """
        return self._main_container

    @main_container.setter
    def main_container(self, main_container):
        """Sets the main_container of this KubeflowOrgV1MPIJobSpec.

        MainContainer specifies name of the main container which executes the MPI code.  # noqa: E501

        :param main_container: The main_container of this KubeflowOrgV1MPIJobSpec.  # noqa: E501
        :type: str
        """

        self._main_container = main_container

    @property
    def mpi_replica_specs(self):
        """Gets the mpi_replica_specs of this KubeflowOrgV1MPIJobSpec.  # noqa: E501

        `MPIReplicaSpecs` contains maps from `MPIReplicaType` to `ReplicaSpec` that specify the MPI replicas to run.  # noqa: E501

        :return: The mpi_replica_specs of this KubeflowOrgV1MPIJobSpec.  # noqa: E501
        :rtype: dict(str, V1ReplicaSpec)
        """
        return self._mpi_replica_specs

    @mpi_replica_specs.setter
    def mpi_replica_specs(self, mpi_replica_specs):
        """Sets the mpi_replica_specs of this KubeflowOrgV1MPIJobSpec.

        `MPIReplicaSpecs` contains maps from `MPIReplicaType` to `ReplicaSpec` that specify the MPI replicas to run.  # noqa: E501

        :param mpi_replica_specs: The mpi_replica_specs of this KubeflowOrgV1MPIJobSpec.  # noqa: E501
        :type: dict(str, V1ReplicaSpec)
        """
        if self.local_vars_configuration.client_side_validation and mpi_replica_specs is None:  # noqa: E501
            raise ValueError("Invalid value for `mpi_replica_specs`, must not be `None`")  # noqa: E501

        self._mpi_replica_specs = mpi_replica_specs

    @property
    def run_policy(self):
        """Gets the run_policy of this KubeflowOrgV1MPIJobSpec.  # noqa: E501


        :return: The run_policy of this KubeflowOrgV1MPIJobSpec.  # noqa: E501
        :rtype: V1RunPolicy
        """
        return self._run_policy

    @run_policy.setter
    def run_policy(self, run_policy):
        """Sets the run_policy of this KubeflowOrgV1MPIJobSpec.


        :param run_policy: The run_policy of this KubeflowOrgV1MPIJobSpec.  # noqa: E501
        :type: V1RunPolicy
        """

        self._run_policy = run_policy

    @property
    def slots_per_worker(self):
        """Gets the slots_per_worker of this KubeflowOrgV1MPIJobSpec.  # noqa: E501

        Specifies the number of slots per worker used in hostfile. Defaults to 1.  # noqa: E501

        :return: The slots_per_worker of this KubeflowOrgV1MPIJobSpec.  # noqa: E501
        :rtype: int
        """
        return self._slots_per_worker

    @slots_per_worker.setter
    def slots_per_worker(self, slots_per_worker):
        """Sets the slots_per_worker of this KubeflowOrgV1MPIJobSpec.

        Specifies the number of slots per worker used in hostfile. Defaults to 1.  # noqa: E501

        :param slots_per_worker: The slots_per_worker of this KubeflowOrgV1MPIJobSpec.  # noqa: E501
        :type: int
        """

        self._slots_per_worker = slots_per_worker

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KubeflowOrgV1MPIJobSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubeflowOrgV1MPIJobSpec):
            return True

        return self.to_dict() != other.to_dict()

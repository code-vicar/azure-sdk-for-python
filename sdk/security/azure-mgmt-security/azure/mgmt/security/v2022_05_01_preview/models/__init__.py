# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AWSEnvironmentData
from ._models_py3 import AwsOrganizationalData
from ._models_py3 import AwsOrganizationalDataMaster
from ._models_py3 import AwsOrganizationalDataMember
from ._models_py3 import AzureDevOpsScopeEnvironmentData
from ._models_py3 import AzureTrackedResourceLocation
from ._models_py3 import CloudErrorBody
from ._models_py3 import CloudOffering
from ._models_py3 import CspmMonitorAwsOffering
from ._models_py3 import CspmMonitorAwsOfferingNativeCloudConnection
from ._models_py3 import CspmMonitorAzureDevOpsOffering
from ._models_py3 import CspmMonitorGcpOffering
from ._models_py3 import CspmMonitorGcpOfferingNativeCloudConnection
from ._models_py3 import CspmMonitorGithubOffering
from ._models_py3 import DefenderFoDatabasesAwsOffering
from ._models_py3 import DefenderFoDatabasesAwsOfferingArcAutoProvisioning
from ._models_py3 import DefenderFoDatabasesAwsOfferingArcAutoProvisioningServicePrincipalSecretMetadata
from ._models_py3 import DefenderForContainersAwsOffering
from ._models_py3 import DefenderForContainersAwsOfferingCloudWatchToKinesis
from ._models_py3 import DefenderForContainersAwsOfferingContainerVulnerabilityAssessment
from ._models_py3 import DefenderForContainersAwsOfferingContainerVulnerabilityAssessmentTask
from ._models_py3 import DefenderForContainersAwsOfferingKinesisToS3
from ._models_py3 import DefenderForContainersAwsOfferingKubernetesScubaReader
from ._models_py3 import DefenderForContainersAwsOfferingKubernetesService
from ._models_py3 import DefenderForContainersGcpOffering
from ._models_py3 import DefenderForContainersGcpOfferingDataPipelineNativeCloudConnection
from ._models_py3 import DefenderForContainersGcpOfferingNativeCloudConnection
from ._models_py3 import DefenderForDatabasesGcpOffering
from ._models_py3 import DefenderForDatabasesGcpOfferingArcAutoProvisioning
from ._models_py3 import DefenderForDatabasesGcpOfferingArcAutoProvisioningConfiguration
from ._models_py3 import DefenderForDatabasesGcpOfferingDefenderForDatabasesArcAutoProvisioning
from ._models_py3 import DefenderForServersAwsOffering
from ._models_py3 import DefenderForServersAwsOfferingArcAutoProvisioning
from ._models_py3 import DefenderForServersAwsOfferingArcAutoProvisioningServicePrincipalSecretMetadata
from ._models_py3 import DefenderForServersAwsOfferingDefenderForServers
from ._models_py3 import DefenderForServersAwsOfferingMdeAutoProvisioning
from ._models_py3 import DefenderForServersAwsOfferingSubPlan
from ._models_py3 import DefenderForServersAwsOfferingVaAutoProvisioning
from ._models_py3 import DefenderForServersAwsOfferingVaAutoProvisioningConfiguration
from ._models_py3 import DefenderForServersAwsOfferingVmScanners
from ._models_py3 import DefenderForServersAwsOfferingVmScannersConfiguration
from ._models_py3 import DefenderForServersGcpOffering
from ._models_py3 import DefenderForServersGcpOfferingArcAutoProvisioning
from ._models_py3 import DefenderForServersGcpOfferingArcAutoProvisioningConfiguration
from ._models_py3 import DefenderForServersGcpOfferingDefenderForServers
from ._models_py3 import DefenderForServersGcpOfferingMdeAutoProvisioning
from ._models_py3 import DefenderForServersGcpOfferingSubPlan
from ._models_py3 import DefenderForServersGcpOfferingVaAutoProvisioning
from ._models_py3 import DefenderForServersGcpOfferingVaAutoProvisioningConfiguration
from ._models_py3 import ETag
from ._models_py3 import EnvironmentData
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import GcpOrganizationalData
from ._models_py3 import GcpOrganizationalDataMember
from ._models_py3 import GcpOrganizationalDataOrganization
from ._models_py3 import GcpProjectDetails
from ._models_py3 import GcpProjectEnvironmentData
from ._models_py3 import GithubScopeEnvironmentData
from ._models_py3 import InformationProtectionAwsOffering
from ._models_py3 import InformationProtectionAwsOfferingInformationProtection
from ._models_py3 import Kind
from ._models_py3 import Resource
from ._models_py3 import SecurityConnector
from ._models_py3 import SecurityConnectorsList
from ._models_py3 import SystemData
from ._models_py3 import Tags
from ._models_py3 import TrackedResource

from ._security_center_enums import CloudName
from ._security_center_enums import CreatedByType
from ._security_center_enums import EnvironmentType
from ._security_center_enums import OfferingType
from ._security_center_enums import OrganizationMembershipType
from ._security_center_enums import ScanningMode
from ._security_center_enums import SubPlan
from ._security_center_enums import Type
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AWSEnvironmentData",
    "AwsOrganizationalData",
    "AwsOrganizationalDataMaster",
    "AwsOrganizationalDataMember",
    "AzureDevOpsScopeEnvironmentData",
    "AzureTrackedResourceLocation",
    "CloudErrorBody",
    "CloudOffering",
    "CspmMonitorAwsOffering",
    "CspmMonitorAwsOfferingNativeCloudConnection",
    "CspmMonitorAzureDevOpsOffering",
    "CspmMonitorGcpOffering",
    "CspmMonitorGcpOfferingNativeCloudConnection",
    "CspmMonitorGithubOffering",
    "DefenderFoDatabasesAwsOffering",
    "DefenderFoDatabasesAwsOfferingArcAutoProvisioning",
    "DefenderFoDatabasesAwsOfferingArcAutoProvisioningServicePrincipalSecretMetadata",
    "DefenderForContainersAwsOffering",
    "DefenderForContainersAwsOfferingCloudWatchToKinesis",
    "DefenderForContainersAwsOfferingContainerVulnerabilityAssessment",
    "DefenderForContainersAwsOfferingContainerVulnerabilityAssessmentTask",
    "DefenderForContainersAwsOfferingKinesisToS3",
    "DefenderForContainersAwsOfferingKubernetesScubaReader",
    "DefenderForContainersAwsOfferingKubernetesService",
    "DefenderForContainersGcpOffering",
    "DefenderForContainersGcpOfferingDataPipelineNativeCloudConnection",
    "DefenderForContainersGcpOfferingNativeCloudConnection",
    "DefenderForDatabasesGcpOffering",
    "DefenderForDatabasesGcpOfferingArcAutoProvisioning",
    "DefenderForDatabasesGcpOfferingArcAutoProvisioningConfiguration",
    "DefenderForDatabasesGcpOfferingDefenderForDatabasesArcAutoProvisioning",
    "DefenderForServersAwsOffering",
    "DefenderForServersAwsOfferingArcAutoProvisioning",
    "DefenderForServersAwsOfferingArcAutoProvisioningServicePrincipalSecretMetadata",
    "DefenderForServersAwsOfferingDefenderForServers",
    "DefenderForServersAwsOfferingMdeAutoProvisioning",
    "DefenderForServersAwsOfferingSubPlan",
    "DefenderForServersAwsOfferingVaAutoProvisioning",
    "DefenderForServersAwsOfferingVaAutoProvisioningConfiguration",
    "DefenderForServersAwsOfferingVmScanners",
    "DefenderForServersAwsOfferingVmScannersConfiguration",
    "DefenderForServersGcpOffering",
    "DefenderForServersGcpOfferingArcAutoProvisioning",
    "DefenderForServersGcpOfferingArcAutoProvisioningConfiguration",
    "DefenderForServersGcpOfferingDefenderForServers",
    "DefenderForServersGcpOfferingMdeAutoProvisioning",
    "DefenderForServersGcpOfferingSubPlan",
    "DefenderForServersGcpOfferingVaAutoProvisioning",
    "DefenderForServersGcpOfferingVaAutoProvisioningConfiguration",
    "ETag",
    "EnvironmentData",
    "ErrorAdditionalInfo",
    "GcpOrganizationalData",
    "GcpOrganizationalDataMember",
    "GcpOrganizationalDataOrganization",
    "GcpProjectDetails",
    "GcpProjectEnvironmentData",
    "GithubScopeEnvironmentData",
    "InformationProtectionAwsOffering",
    "InformationProtectionAwsOfferingInformationProtection",
    "Kind",
    "Resource",
    "SecurityConnector",
    "SecurityConnectorsList",
    "SystemData",
    "Tags",
    "TrackedResource",
    "CloudName",
    "CreatedByType",
    "EnvironmentType",
    "OfferingType",
    "OrganizationMembershipType",
    "ScanningMode",
    "SubPlan",
    "Type",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()

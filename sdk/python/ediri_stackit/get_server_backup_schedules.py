# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs

__all__ = [
    'GetServerBackupSchedulesResult',
    'AwaitableGetServerBackupSchedulesResult',
    'get_server_backup_schedules',
    'get_server_backup_schedules_output',
]

@pulumi.output_type
class GetServerBackupSchedulesResult:
    """
    A collection of values returned by getServerBackupSchedules.
    """
    def __init__(__self__, id=None, items=None, project_id=None, region=None, server_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if server_id and not isinstance(server_id, str):
            raise TypeError("Expected argument 'server_id' to be a str")
        pulumi.set(__self__, "server_id", server_id)

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetServerBackupSchedulesItemResult']:
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> builtins.str:
        """
        STACKIT Project ID (UUID) to which the server is associated.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> Optional[builtins.str]:
        """
        The resource region. If not defined, the provider region is used.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> builtins.str:
        """
        Server ID (UUID) to which the backup schedule is associated.
        """
        return pulumi.get(self, "server_id")


class AwaitableGetServerBackupSchedulesResult(GetServerBackupSchedulesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerBackupSchedulesResult(
            id=self.id,
            items=self.items,
            project_id=self.project_id,
            region=self.region,
            server_id=self.server_id)


def get_server_backup_schedules(project_id: Optional[builtins.str] = None,
                                region: Optional[builtins.str] = None,
                                server_id: Optional[builtins.str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerBackupSchedulesResult:
    """
    Server backup schedules datasource schema. Must have a `region` specified in the provider configuration.

    > This resource is in beta and may be subject to breaking changes in the future. Use with caution. See our guide for how to opt-in to use beta resources.

    ## Example Usage


    :param builtins.str project_id: STACKIT Project ID (UUID) to which the server is associated.
    :param builtins.str region: The resource region. If not defined, the provider region is used.
    :param builtins.str server_id: Server ID (UUID) to which the backup schedule is associated.
    """
    __args__ = dict()
    __args__['projectId'] = project_id
    __args__['region'] = region
    __args__['serverId'] = server_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('stackit:index/getServerBackupSchedules:getServerBackupSchedules', __args__, opts=opts, typ=GetServerBackupSchedulesResult).value

    return AwaitableGetServerBackupSchedulesResult(
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        project_id=pulumi.get(__ret__, 'project_id'),
        region=pulumi.get(__ret__, 'region'),
        server_id=pulumi.get(__ret__, 'server_id'))
def get_server_backup_schedules_output(project_id: Optional[pulumi.Input[builtins.str]] = None,
                                       region: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                                       server_id: Optional[pulumi.Input[builtins.str]] = None,
                                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetServerBackupSchedulesResult]:
    """
    Server backup schedules datasource schema. Must have a `region` specified in the provider configuration.

    > This resource is in beta and may be subject to breaking changes in the future. Use with caution. See our guide for how to opt-in to use beta resources.

    ## Example Usage


    :param builtins.str project_id: STACKIT Project ID (UUID) to which the server is associated.
    :param builtins.str region: The resource region. If not defined, the provider region is used.
    :param builtins.str server_id: Server ID (UUID) to which the backup schedule is associated.
    """
    __args__ = dict()
    __args__['projectId'] = project_id
    __args__['region'] = region
    __args__['serverId'] = server_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('stackit:index/getServerBackupSchedules:getServerBackupSchedules', __args__, opts=opts, typ=GetServerBackupSchedulesResult)
    return __ret__.apply(lambda __response__: GetServerBackupSchedulesResult(
        id=pulumi.get(__response__, 'id'),
        items=pulumi.get(__response__, 'items'),
        project_id=pulumi.get(__response__, 'project_id'),
        region=pulumi.get(__response__, 'region'),
        server_id=pulumi.get(__response__, 'server_id')))

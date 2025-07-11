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

__all__ = [
    'GetNetworkInterfaceResult',
    'AwaitableGetNetworkInterfaceResult',
    'get_network_interface',
    'get_network_interface_output',
]

@pulumi.output_type
class GetNetworkInterfaceResult:
    """
    A collection of values returned by getNetworkInterface.
    """
    def __init__(__self__, allowed_addresses=None, device=None, id=None, ipv4=None, labels=None, mac=None, name=None, network_id=None, network_interface_id=None, project_id=None, security=None, security_group_ids=None, type=None):
        if allowed_addresses and not isinstance(allowed_addresses, list):
            raise TypeError("Expected argument 'allowed_addresses' to be a list")
        pulumi.set(__self__, "allowed_addresses", allowed_addresses)
        if device and not isinstance(device, str):
            raise TypeError("Expected argument 'device' to be a str")
        pulumi.set(__self__, "device", device)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv4 and not isinstance(ipv4, str):
            raise TypeError("Expected argument 'ipv4' to be a str")
        pulumi.set(__self__, "ipv4", ipv4)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if mac and not isinstance(mac, str):
            raise TypeError("Expected argument 'mac' to be a str")
        pulumi.set(__self__, "mac", mac)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)
        if network_interface_id and not isinstance(network_interface_id, str):
            raise TypeError("Expected argument 'network_interface_id' to be a str")
        pulumi.set(__self__, "network_interface_id", network_interface_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if security and not isinstance(security, bool):
            raise TypeError("Expected argument 'security' to be a bool")
        pulumi.set(__self__, "security", security)
        if security_group_ids and not isinstance(security_group_ids, list):
            raise TypeError("Expected argument 'security_group_ids' to be a list")
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="allowedAddresses")
    def allowed_addresses(self) -> Sequence[builtins.str]:
        """
        The list of CIDR (Classless Inter-Domain Routing) notations.
        """
        return pulumi.get(self, "allowed_addresses")

    @property
    @pulumi.getter
    def device(self) -> builtins.str:
        """
        The device UUID of the network interface.
        """
        return pulumi.get(self, "device")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ipv4(self) -> builtins.str:
        """
        The IPv4 address.
        """
        return pulumi.get(self, "ipv4")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, builtins.str]:
        """
        Labels are key-value string pairs which can be attached to a network interface.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def mac(self) -> builtins.str:
        """
        The MAC address of network interface.
        """
        return pulumi.get(self, "mac")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the network interface.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> builtins.str:
        """
        The network ID to which the network interface is associated.
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> builtins.str:
        """
        The network interface ID.
        """
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> builtins.str:
        """
        STACKIT project ID to which the network interface is associated.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def security(self) -> builtins.bool:
        """
        The Network Interface Security. If set to false, then no security groups will apply to this network interface.
        """
        return pulumi.get(self, "security")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[builtins.str]:
        """
        The list of security group UUIDs. If security is set to false, setting this field will lead to an error.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        Type of network interface. Some of the possible values are: Supported values are: `server`, `metadata`, `gateway`.
        """
        return pulumi.get(self, "type")


class AwaitableGetNetworkInterfaceResult(GetNetworkInterfaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkInterfaceResult(
            allowed_addresses=self.allowed_addresses,
            device=self.device,
            id=self.id,
            ipv4=self.ipv4,
            labels=self.labels,
            mac=self.mac,
            name=self.name,
            network_id=self.network_id,
            network_interface_id=self.network_interface_id,
            project_id=self.project_id,
            security=self.security,
            security_group_ids=self.security_group_ids,
            type=self.type)


def get_network_interface(network_id: Optional[builtins.str] = None,
                          network_interface_id: Optional[builtins.str] = None,
                          project_id: Optional[builtins.str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkInterfaceResult:
    """
    Network interface datasource schema. Must have a `region` specified in the provider configuration.

    ## Example Usage


    :param builtins.str network_id: The network ID to which the network interface is associated.
    :param builtins.str network_interface_id: The network interface ID.
    :param builtins.str project_id: STACKIT project ID to which the network interface is associated.
    """
    __args__ = dict()
    __args__['networkId'] = network_id
    __args__['networkInterfaceId'] = network_interface_id
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('stackit:index/getNetworkInterface:getNetworkInterface', __args__, opts=opts, typ=GetNetworkInterfaceResult).value

    return AwaitableGetNetworkInterfaceResult(
        allowed_addresses=pulumi.get(__ret__, 'allowed_addresses'),
        device=pulumi.get(__ret__, 'device'),
        id=pulumi.get(__ret__, 'id'),
        ipv4=pulumi.get(__ret__, 'ipv4'),
        labels=pulumi.get(__ret__, 'labels'),
        mac=pulumi.get(__ret__, 'mac'),
        name=pulumi.get(__ret__, 'name'),
        network_id=pulumi.get(__ret__, 'network_id'),
        network_interface_id=pulumi.get(__ret__, 'network_interface_id'),
        project_id=pulumi.get(__ret__, 'project_id'),
        security=pulumi.get(__ret__, 'security'),
        security_group_ids=pulumi.get(__ret__, 'security_group_ids'),
        type=pulumi.get(__ret__, 'type'))
def get_network_interface_output(network_id: Optional[pulumi.Input[builtins.str]] = None,
                                 network_interface_id: Optional[pulumi.Input[builtins.str]] = None,
                                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetNetworkInterfaceResult]:
    """
    Network interface datasource schema. Must have a `region` specified in the provider configuration.

    ## Example Usage


    :param builtins.str network_id: The network ID to which the network interface is associated.
    :param builtins.str network_interface_id: The network interface ID.
    :param builtins.str project_id: STACKIT project ID to which the network interface is associated.
    """
    __args__ = dict()
    __args__['networkId'] = network_id
    __args__['networkInterfaceId'] = network_interface_id
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('stackit:index/getNetworkInterface:getNetworkInterface', __args__, opts=opts, typ=GetNetworkInterfaceResult)
    return __ret__.apply(lambda __response__: GetNetworkInterfaceResult(
        allowed_addresses=pulumi.get(__response__, 'allowed_addresses'),
        device=pulumi.get(__response__, 'device'),
        id=pulumi.get(__response__, 'id'),
        ipv4=pulumi.get(__response__, 'ipv4'),
        labels=pulumi.get(__response__, 'labels'),
        mac=pulumi.get(__response__, 'mac'),
        name=pulumi.get(__response__, 'name'),
        network_id=pulumi.get(__response__, 'network_id'),
        network_interface_id=pulumi.get(__response__, 'network_interface_id'),
        project_id=pulumi.get(__response__, 'project_id'),
        security=pulumi.get(__response__, 'security'),
        security_group_ids=pulumi.get(__response__, 'security_group_ids'),
        type=pulumi.get(__response__, 'type')))

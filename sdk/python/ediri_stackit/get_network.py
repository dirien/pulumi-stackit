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
    'GetNetworkResult',
    'AwaitableGetNetworkResult',
    'get_network',
    'get_network_output',
]

@pulumi.output_type
class GetNetworkResult:
    """
    A collection of values returned by getNetwork.
    """
    def __init__(__self__, id=None, ipv4_gateway=None, ipv4_nameservers=None, ipv4_prefix=None, ipv4_prefix_length=None, ipv4_prefixes=None, ipv6_gateway=None, ipv6_nameservers=None, ipv6_prefix=None, ipv6_prefix_length=None, ipv6_prefixes=None, labels=None, name=None, nameservers=None, network_id=None, prefixes=None, project_id=None, public_ip=None, routed=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv4_gateway and not isinstance(ipv4_gateway, str):
            raise TypeError("Expected argument 'ipv4_gateway' to be a str")
        pulumi.set(__self__, "ipv4_gateway", ipv4_gateway)
        if ipv4_nameservers and not isinstance(ipv4_nameservers, list):
            raise TypeError("Expected argument 'ipv4_nameservers' to be a list")
        pulumi.set(__self__, "ipv4_nameservers", ipv4_nameservers)
        if ipv4_prefix and not isinstance(ipv4_prefix, str):
            raise TypeError("Expected argument 'ipv4_prefix' to be a str")
        pulumi.set(__self__, "ipv4_prefix", ipv4_prefix)
        if ipv4_prefix_length and not isinstance(ipv4_prefix_length, int):
            raise TypeError("Expected argument 'ipv4_prefix_length' to be a int")
        pulumi.set(__self__, "ipv4_prefix_length", ipv4_prefix_length)
        if ipv4_prefixes and not isinstance(ipv4_prefixes, list):
            raise TypeError("Expected argument 'ipv4_prefixes' to be a list")
        pulumi.set(__self__, "ipv4_prefixes", ipv4_prefixes)
        if ipv6_gateway and not isinstance(ipv6_gateway, str):
            raise TypeError("Expected argument 'ipv6_gateway' to be a str")
        pulumi.set(__self__, "ipv6_gateway", ipv6_gateway)
        if ipv6_nameservers and not isinstance(ipv6_nameservers, list):
            raise TypeError("Expected argument 'ipv6_nameservers' to be a list")
        pulumi.set(__self__, "ipv6_nameservers", ipv6_nameservers)
        if ipv6_prefix and not isinstance(ipv6_prefix, str):
            raise TypeError("Expected argument 'ipv6_prefix' to be a str")
        pulumi.set(__self__, "ipv6_prefix", ipv6_prefix)
        if ipv6_prefix_length and not isinstance(ipv6_prefix_length, int):
            raise TypeError("Expected argument 'ipv6_prefix_length' to be a int")
        pulumi.set(__self__, "ipv6_prefix_length", ipv6_prefix_length)
        if ipv6_prefixes and not isinstance(ipv6_prefixes, list):
            raise TypeError("Expected argument 'ipv6_prefixes' to be a list")
        pulumi.set(__self__, "ipv6_prefixes", ipv6_prefixes)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nameservers and not isinstance(nameservers, list):
            raise TypeError("Expected argument 'nameservers' to be a list")
        pulumi.set(__self__, "nameservers", nameservers)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)
        if prefixes and not isinstance(prefixes, list):
            raise TypeError("Expected argument 'prefixes' to be a list")
        pulumi.set(__self__, "prefixes", prefixes)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if public_ip and not isinstance(public_ip, str):
            raise TypeError("Expected argument 'public_ip' to be a str")
        pulumi.set(__self__, "public_ip", public_ip)
        if routed and not isinstance(routed, bool):
            raise TypeError("Expected argument 'routed' to be a bool")
        pulumi.set(__self__, "routed", routed)

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipv4Gateway")
    def ipv4_gateway(self) -> builtins.str:
        """
        The IPv4 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
        """
        return pulumi.get(self, "ipv4_gateway")

    @property
    @pulumi.getter(name="ipv4Nameservers")
    def ipv4_nameservers(self) -> Sequence[builtins.str]:
        """
        The IPv4 nameservers of the network.
        """
        return pulumi.get(self, "ipv4_nameservers")

    @property
    @pulumi.getter(name="ipv4Prefix")
    @_utilities.deprecated("""The API supports reading multiple prefixes. So using the attribute 'ipv4_prefixes` should be preferred. This attribute will be populated with the first element from the list""")
    def ipv4_prefix(self) -> builtins.str:
        """
        The IPv4 prefix of the network (CIDR).
        """
        return pulumi.get(self, "ipv4_prefix")

    @property
    @pulumi.getter(name="ipv4PrefixLength")
    def ipv4_prefix_length(self) -> builtins.int:
        """
        The IPv4 prefix length of the network.
        """
        return pulumi.get(self, "ipv4_prefix_length")

    @property
    @pulumi.getter(name="ipv4Prefixes")
    def ipv4_prefixes(self) -> Sequence[builtins.str]:
        """
        The IPv4 prefixes of the network.
        """
        return pulumi.get(self, "ipv4_prefixes")

    @property
    @pulumi.getter(name="ipv6Gateway")
    def ipv6_gateway(self) -> builtins.str:
        """
        The IPv6 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
        """
        return pulumi.get(self, "ipv6_gateway")

    @property
    @pulumi.getter(name="ipv6Nameservers")
    def ipv6_nameservers(self) -> Sequence[builtins.str]:
        """
        The IPv6 nameservers of the network.
        """
        return pulumi.get(self, "ipv6_nameservers")

    @property
    @pulumi.getter(name="ipv6Prefix")
    @_utilities.deprecated("""The API supports reading multiple prefixes. So using the attribute 'ipv6_prefixes` should be preferred. This attribute will be populated with the first element from the list""")
    def ipv6_prefix(self) -> builtins.str:
        """
        The IPv6 prefix of the network (CIDR).
        """
        return pulumi.get(self, "ipv6_prefix")

    @property
    @pulumi.getter(name="ipv6PrefixLength")
    def ipv6_prefix_length(self) -> builtins.int:
        """
        The IPv6 prefix length of the network.
        """
        return pulumi.get(self, "ipv6_prefix_length")

    @property
    @pulumi.getter(name="ipv6Prefixes")
    def ipv6_prefixes(self) -> Sequence[builtins.str]:
        """
        The IPv6 prefixes of the network.
        """
        return pulumi.get(self, "ipv6_prefixes")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, builtins.str]:
        """
        Labels are key-value string pairs which can be attached to a resource container
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the network.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    @_utilities.deprecated("""Use `ipv4_nameservers` to configure the nameservers for IPv4.""")
    def nameservers(self) -> Sequence[builtins.str]:
        """
        The nameservers of the network. This field is deprecated and will be removed soon, use `ipv4_nameservers` to configure the nameservers for IPv4.
        """
        return pulumi.get(self, "nameservers")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> builtins.str:
        """
        The network ID.
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    @_utilities.deprecated("""Use `ipv4_prefixes` to read the prefixes of the IPv4 networks.""")
    def prefixes(self) -> Sequence[builtins.str]:
        """
        The prefixes of the network. This field is deprecated and will be removed soon, use `ipv4_prefixes` to read the prefixes of the IPv4 networks.
        """
        return pulumi.get(self, "prefixes")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> builtins.str:
        """
        STACKIT project ID to which the network is associated.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> builtins.str:
        """
        The public IP of the network.
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter
    def routed(self) -> builtins.bool:
        """
        Shows if the network is routed and therefore accessible from other networks.
        """
        return pulumi.get(self, "routed")


class AwaitableGetNetworkResult(GetNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkResult(
            id=self.id,
            ipv4_gateway=self.ipv4_gateway,
            ipv4_nameservers=self.ipv4_nameservers,
            ipv4_prefix=self.ipv4_prefix,
            ipv4_prefix_length=self.ipv4_prefix_length,
            ipv4_prefixes=self.ipv4_prefixes,
            ipv6_gateway=self.ipv6_gateway,
            ipv6_nameservers=self.ipv6_nameservers,
            ipv6_prefix=self.ipv6_prefix,
            ipv6_prefix_length=self.ipv6_prefix_length,
            ipv6_prefixes=self.ipv6_prefixes,
            labels=self.labels,
            name=self.name,
            nameservers=self.nameservers,
            network_id=self.network_id,
            prefixes=self.prefixes,
            project_id=self.project_id,
            public_ip=self.public_ip,
            routed=self.routed)


def get_network(network_id: Optional[builtins.str] = None,
                project_id: Optional[builtins.str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkResult:
    """
    Network resource schema. Must have a `region` specified in the provider configuration.

    ## Example Usage


    :param builtins.str network_id: The network ID.
    :param builtins.str project_id: STACKIT project ID to which the network is associated.
    """
    __args__ = dict()
    __args__['networkId'] = network_id
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('stackit:index/getNetwork:getNetwork', __args__, opts=opts, typ=GetNetworkResult).value

    return AwaitableGetNetworkResult(
        id=pulumi.get(__ret__, 'id'),
        ipv4_gateway=pulumi.get(__ret__, 'ipv4_gateway'),
        ipv4_nameservers=pulumi.get(__ret__, 'ipv4_nameservers'),
        ipv4_prefix=pulumi.get(__ret__, 'ipv4_prefix'),
        ipv4_prefix_length=pulumi.get(__ret__, 'ipv4_prefix_length'),
        ipv4_prefixes=pulumi.get(__ret__, 'ipv4_prefixes'),
        ipv6_gateway=pulumi.get(__ret__, 'ipv6_gateway'),
        ipv6_nameservers=pulumi.get(__ret__, 'ipv6_nameservers'),
        ipv6_prefix=pulumi.get(__ret__, 'ipv6_prefix'),
        ipv6_prefix_length=pulumi.get(__ret__, 'ipv6_prefix_length'),
        ipv6_prefixes=pulumi.get(__ret__, 'ipv6_prefixes'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        nameservers=pulumi.get(__ret__, 'nameservers'),
        network_id=pulumi.get(__ret__, 'network_id'),
        prefixes=pulumi.get(__ret__, 'prefixes'),
        project_id=pulumi.get(__ret__, 'project_id'),
        public_ip=pulumi.get(__ret__, 'public_ip'),
        routed=pulumi.get(__ret__, 'routed'))
def get_network_output(network_id: Optional[pulumi.Input[builtins.str]] = None,
                       project_id: Optional[pulumi.Input[builtins.str]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetNetworkResult]:
    """
    Network resource schema. Must have a `region` specified in the provider configuration.

    ## Example Usage


    :param builtins.str network_id: The network ID.
    :param builtins.str project_id: STACKIT project ID to which the network is associated.
    """
    __args__ = dict()
    __args__['networkId'] = network_id
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('stackit:index/getNetwork:getNetwork', __args__, opts=opts, typ=GetNetworkResult)
    return __ret__.apply(lambda __response__: GetNetworkResult(
        id=pulumi.get(__response__, 'id'),
        ipv4_gateway=pulumi.get(__response__, 'ipv4_gateway'),
        ipv4_nameservers=pulumi.get(__response__, 'ipv4_nameservers'),
        ipv4_prefix=pulumi.get(__response__, 'ipv4_prefix'),
        ipv4_prefix_length=pulumi.get(__response__, 'ipv4_prefix_length'),
        ipv4_prefixes=pulumi.get(__response__, 'ipv4_prefixes'),
        ipv6_gateway=pulumi.get(__response__, 'ipv6_gateway'),
        ipv6_nameservers=pulumi.get(__response__, 'ipv6_nameservers'),
        ipv6_prefix=pulumi.get(__response__, 'ipv6_prefix'),
        ipv6_prefix_length=pulumi.get(__response__, 'ipv6_prefix_length'),
        ipv6_prefixes=pulumi.get(__response__, 'ipv6_prefixes'),
        labels=pulumi.get(__response__, 'labels'),
        name=pulumi.get(__response__, 'name'),
        nameservers=pulumi.get(__response__, 'nameservers'),
        network_id=pulumi.get(__response__, 'network_id'),
        prefixes=pulumi.get(__response__, 'prefixes'),
        project_id=pulumi.get(__response__, 'project_id'),
        public_ip=pulumi.get(__response__, 'public_ip'),
        routed=pulumi.get(__response__, 'routed')))

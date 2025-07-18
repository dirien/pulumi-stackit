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

__all__ = ['NetworkInterfaceArgs', 'NetworkInterface']

@pulumi.input_type
class NetworkInterfaceArgs:
    def __init__(__self__, *,
                 network_id: pulumi.Input[builtins.str],
                 project_id: pulumi.Input[builtins.str],
                 allowed_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 ipv4: Optional[pulumi.Input[builtins.str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 security: Optional[pulumi.Input[builtins.bool]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a NetworkInterface resource.
        :param pulumi.Input[builtins.str] network_id: The network ID to which the network interface is associated.
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the network is associated.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] allowed_addresses: The list of CIDR (Classless Inter-Domain Routing) notations.
        :param pulumi.Input[builtins.str] ipv4: The IPv4 address.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a network interface.
        :param pulumi.Input[builtins.str] name: The name of the network interface.
        :param pulumi.Input[builtins.bool] security: The Network Interface Security. If set to false, then no security groups will apply to this network interface.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] security_group_ids: The list of security group UUIDs. If security is set to false, setting this field will lead to an error.
        """
        pulumi.set(__self__, "network_id", network_id)
        pulumi.set(__self__, "project_id", project_id)
        if allowed_addresses is not None:
            pulumi.set(__self__, "allowed_addresses", allowed_addresses)
        if ipv4 is not None:
            pulumi.set(__self__, "ipv4", ipv4)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if security is not None:
            pulumi.set(__self__, "security", security)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[builtins.str]:
        """
        The network ID to which the network interface is associated.
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[builtins.str]:
        """
        STACKIT project ID to which the network is associated.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="allowedAddresses")
    def allowed_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        The list of CIDR (Classless Inter-Domain Routing) notations.
        """
        return pulumi.get(self, "allowed_addresses")

    @allowed_addresses.setter
    def allowed_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "allowed_addresses", value)

    @property
    @pulumi.getter
    def ipv4(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The IPv4 address.
        """
        return pulumi.get(self, "ipv4")

    @ipv4.setter
    def ipv4(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "ipv4", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Labels are key-value string pairs which can be attached to a network interface.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the network interface.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def security(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        The Network Interface Security. If set to false, then no security groups will apply to this network interface.
        """
        return pulumi.get(self, "security")

    @security.setter
    def security(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "security", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        The list of security group UUIDs. If security is set to false, setting this field will lead to an error.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "security_group_ids", value)


@pulumi.input_type
class _NetworkInterfaceState:
    def __init__(__self__, *,
                 allowed_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 device: Optional[pulumi.Input[builtins.str]] = None,
                 ipv4: Optional[pulumi.Input[builtins.str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 mac: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 network_id: Optional[pulumi.Input[builtins.str]] = None,
                 network_interface_id: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 security: Optional[pulumi.Input[builtins.bool]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 type: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering NetworkInterface resources.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] allowed_addresses: The list of CIDR (Classless Inter-Domain Routing) notations.
        :param pulumi.Input[builtins.str] device: The device UUID of the network interface.
        :param pulumi.Input[builtins.str] ipv4: The IPv4 address.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a network interface.
        :param pulumi.Input[builtins.str] mac: The MAC address of network interface.
        :param pulumi.Input[builtins.str] name: The name of the network interface.
        :param pulumi.Input[builtins.str] network_id: The network ID to which the network interface is associated.
        :param pulumi.Input[builtins.str] network_interface_id: The network interface ID.
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the network is associated.
        :param pulumi.Input[builtins.bool] security: The Network Interface Security. If set to false, then no security groups will apply to this network interface.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] security_group_ids: The list of security group UUIDs. If security is set to false, setting this field will lead to an error.
        :param pulumi.Input[builtins.str] type: Type of network interface. Some of the possible values are: Supported values are: `server`, `metadata`, `gateway`.
        """
        if allowed_addresses is not None:
            pulumi.set(__self__, "allowed_addresses", allowed_addresses)
        if device is not None:
            pulumi.set(__self__, "device", device)
        if ipv4 is not None:
            pulumi.set(__self__, "ipv4", ipv4)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if mac is not None:
            pulumi.set(__self__, "mac", mac)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if network_interface_id is not None:
            pulumi.set(__self__, "network_interface_id", network_interface_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if security is not None:
            pulumi.set(__self__, "security", security)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="allowedAddresses")
    def allowed_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        The list of CIDR (Classless Inter-Domain Routing) notations.
        """
        return pulumi.get(self, "allowed_addresses")

    @allowed_addresses.setter
    def allowed_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "allowed_addresses", value)

    @property
    @pulumi.getter
    def device(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The device UUID of the network interface.
        """
        return pulumi.get(self, "device")

    @device.setter
    def device(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "device", value)

    @property
    @pulumi.getter
    def ipv4(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The IPv4 address.
        """
        return pulumi.get(self, "ipv4")

    @ipv4.setter
    def ipv4(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "ipv4", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Labels are key-value string pairs which can be attached to a network interface.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def mac(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The MAC address of network interface.
        """
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "mac", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the network interface.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The network ID to which the network interface is associated.
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The network interface ID.
        """
        return pulumi.get(self, "network_interface_id")

    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "network_interface_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        STACKIT project ID to which the network is associated.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def security(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        The Network Interface Security. If set to false, then no security groups will apply to this network interface.
        """
        return pulumi.get(self, "security")

    @security.setter
    def security(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "security", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        The list of security group UUIDs. If security is set to false, setting this field will lead to an error.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Type of network interface. Some of the possible values are: Supported values are: `server`, `metadata`, `gateway`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "type", value)


@pulumi.type_token("stackit:index/networkInterface:NetworkInterface")
class NetworkInterface(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 ipv4: Optional[pulumi.Input[builtins.str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 network_id: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 security: Optional[pulumi.Input[builtins.bool]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        Network interface resource schema. Must have a `region` specified in the provider configuration.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] allowed_addresses: The list of CIDR (Classless Inter-Domain Routing) notations.
        :param pulumi.Input[builtins.str] ipv4: The IPv4 address.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a network interface.
        :param pulumi.Input[builtins.str] name: The name of the network interface.
        :param pulumi.Input[builtins.str] network_id: The network ID to which the network interface is associated.
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the network is associated.
        :param pulumi.Input[builtins.bool] security: The Network Interface Security. If set to false, then no security groups will apply to this network interface.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] security_group_ids: The list of security group UUIDs. If security is set to false, setting this field will lead to an error.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkInterfaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Network interface resource schema. Must have a `region` specified in the provider configuration.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param NetworkInterfaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInterfaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 ipv4: Optional[pulumi.Input[builtins.str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 network_id: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 security: Optional[pulumi.Input[builtins.bool]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkInterfaceArgs.__new__(NetworkInterfaceArgs)

            __props__.__dict__["allowed_addresses"] = allowed_addresses
            __props__.__dict__["ipv4"] = ipv4
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["security"] = security
            __props__.__dict__["security_group_ids"] = security_group_ids
            __props__.__dict__["device"] = None
            __props__.__dict__["mac"] = None
            __props__.__dict__["network_interface_id"] = None
            __props__.__dict__["type"] = None
        super(NetworkInterface, __self__).__init__(
            'stackit:index/networkInterface:NetworkInterface',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allowed_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
            device: Optional[pulumi.Input[builtins.str]] = None,
            ipv4: Optional[pulumi.Input[builtins.str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
            mac: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            network_id: Optional[pulumi.Input[builtins.str]] = None,
            network_interface_id: Optional[pulumi.Input[builtins.str]] = None,
            project_id: Optional[pulumi.Input[builtins.str]] = None,
            security: Optional[pulumi.Input[builtins.bool]] = None,
            security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
            type: Optional[pulumi.Input[builtins.str]] = None) -> 'NetworkInterface':
        """
        Get an existing NetworkInterface resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] allowed_addresses: The list of CIDR (Classless Inter-Domain Routing) notations.
        :param pulumi.Input[builtins.str] device: The device UUID of the network interface.
        :param pulumi.Input[builtins.str] ipv4: The IPv4 address.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a network interface.
        :param pulumi.Input[builtins.str] mac: The MAC address of network interface.
        :param pulumi.Input[builtins.str] name: The name of the network interface.
        :param pulumi.Input[builtins.str] network_id: The network ID to which the network interface is associated.
        :param pulumi.Input[builtins.str] network_interface_id: The network interface ID.
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the network is associated.
        :param pulumi.Input[builtins.bool] security: The Network Interface Security. If set to false, then no security groups will apply to this network interface.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] security_group_ids: The list of security group UUIDs. If security is set to false, setting this field will lead to an error.
        :param pulumi.Input[builtins.str] type: Type of network interface. Some of the possible values are: Supported values are: `server`, `metadata`, `gateway`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkInterfaceState.__new__(_NetworkInterfaceState)

        __props__.__dict__["allowed_addresses"] = allowed_addresses
        __props__.__dict__["device"] = device
        __props__.__dict__["ipv4"] = ipv4
        __props__.__dict__["labels"] = labels
        __props__.__dict__["mac"] = mac
        __props__.__dict__["name"] = name
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["network_interface_id"] = network_interface_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["security"] = security
        __props__.__dict__["security_group_ids"] = security_group_ids
        __props__.__dict__["type"] = type
        return NetworkInterface(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedAddresses")
    def allowed_addresses(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        The list of CIDR (Classless Inter-Domain Routing) notations.
        """
        return pulumi.get(self, "allowed_addresses")

    @property
    @pulumi.getter
    def device(self) -> pulumi.Output[builtins.str]:
        """
        The device UUID of the network interface.
        """
        return pulumi.get(self, "device")

    @property
    @pulumi.getter
    def ipv4(self) -> pulumi.Output[builtins.str]:
        """
        The IPv4 address.
        """
        return pulumi.get(self, "ipv4")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        Labels are key-value string pairs which can be attached to a network interface.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def mac(self) -> pulumi.Output[builtins.str]:
        """
        The MAC address of network interface.
        """
        return pulumi.get(self, "mac")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the network interface.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[builtins.str]:
        """
        The network ID to which the network interface is associated.
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[builtins.str]:
        """
        The network interface ID.
        """
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[builtins.str]:
        """
        STACKIT project ID to which the network is associated.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def security(self) -> pulumi.Output[builtins.bool]:
        """
        The Network Interface Security. If set to false, then no security groups will apply to this network interface.
        """
        return pulumi.get(self, "security")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        The list of security group UUIDs. If security is set to false, setting this field will lead to an error.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        Type of network interface. Some of the possible values are: Supported values are: `server`, `metadata`, `gateway`.
        """
        return pulumi.get(self, "type")


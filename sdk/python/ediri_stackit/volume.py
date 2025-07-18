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
from ._inputs import *

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 availability_zone: pulumi.Input[builtins.str],
                 project_id: pulumi.Input[builtins.str],
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 performance_class: Optional[pulumi.Input[builtins.str]] = None,
                 size: Optional[pulumi.Input[builtins.int]] = None,
                 source: Optional[pulumi.Input['VolumeSourceArgs']] = None):
        """
        The set of arguments for constructing a Volume resource.
        :param pulumi.Input[builtins.str] availability_zone: The availability zone of the volume.
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the volume is associated.
        :param pulumi.Input[builtins.str] description: The description of the volume.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a resource container
        :param pulumi.Input[builtins.str] name: The name of the volume.
        :param pulumi.Input[builtins.str] performance_class: The performance class of the volume. Possible values are documented in [Service plans BlockStorage](https://docs.stackit.cloud/stackit/en/service-plans-blockstorage-75137974.html#ServiceplansBlockStorage-CurrentlyavailableServicePlans%28performanceclasses%29)
        :param pulumi.Input[builtins.int] size: The size of the volume in GB. It can only be updated to a larger value than the current size. Either `size` or `source` must be provided
        :param pulumi.Input['VolumeSourceArgs'] source: The source of the volume. It can be either a volume, an image, a snapshot or a backup. Either `size` or `source` must be provided
        """
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "project_id", project_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if performance_class is not None:
            pulumi.set(__self__, "performance_class", performance_class)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if source is not None:
            pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Input[builtins.str]:
        """
        The availability zone of the volume.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[builtins.str]:
        """
        STACKIT project ID to which the volume is associated.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the volume.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Labels are key-value string pairs which can be attached to a resource container
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the volume.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="performanceClass")
    def performance_class(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The performance class of the volume. Possible values are documented in [Service plans BlockStorage](https://docs.stackit.cloud/stackit/en/service-plans-blockstorage-75137974.html#ServiceplansBlockStorage-CurrentlyavailableServicePlans%28performanceclasses%29)
        """
        return pulumi.get(self, "performance_class")

    @performance_class.setter
    def performance_class(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "performance_class", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        The size of the volume in GB. It can only be updated to a larger value than the current size. Either `size` or `source` must be provided
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input['VolumeSourceArgs']]:
        """
        The source of the volume. It can be either a volume, an image, a snapshot or a backup. Either `size` or `source` must be provided
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input['VolumeSourceArgs']]):
        pulumi.set(self, "source", value)


@pulumi.input_type
class _VolumeState:
    def __init__(__self__, *,
                 availability_zone: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 performance_class: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 server_id: Optional[pulumi.Input[builtins.str]] = None,
                 size: Optional[pulumi.Input[builtins.int]] = None,
                 source: Optional[pulumi.Input['VolumeSourceArgs']] = None,
                 volume_id: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering Volume resources.
        :param pulumi.Input[builtins.str] availability_zone: The availability zone of the volume.
        :param pulumi.Input[builtins.str] description: The description of the volume.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a resource container
        :param pulumi.Input[builtins.str] name: The name of the volume.
        :param pulumi.Input[builtins.str] performance_class: The performance class of the volume. Possible values are documented in [Service plans BlockStorage](https://docs.stackit.cloud/stackit/en/service-plans-blockstorage-75137974.html#ServiceplansBlockStorage-CurrentlyavailableServicePlans%28performanceclasses%29)
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the volume is associated.
        :param pulumi.Input[builtins.str] server_id: The server ID of the server to which the volume is attached to.
        :param pulumi.Input[builtins.int] size: The size of the volume in GB. It can only be updated to a larger value than the current size. Either `size` or `source` must be provided
        :param pulumi.Input['VolumeSourceArgs'] source: The source of the volume. It can be either a volume, an image, a snapshot or a backup. Either `size` or `source` must be provided
        :param pulumi.Input[builtins.str] volume_id: The volume ID.
        """
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if performance_class is not None:
            pulumi.set(__self__, "performance_class", performance_class)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if volume_id is not None:
            pulumi.set(__self__, "volume_id", volume_id)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The availability zone of the volume.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the volume.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Labels are key-value string pairs which can be attached to a resource container
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the volume.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="performanceClass")
    def performance_class(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The performance class of the volume. Possible values are documented in [Service plans BlockStorage](https://docs.stackit.cloud/stackit/en/service-plans-blockstorage-75137974.html#ServiceplansBlockStorage-CurrentlyavailableServicePlans%28performanceclasses%29)
        """
        return pulumi.get(self, "performance_class")

    @performance_class.setter
    def performance_class(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "performance_class", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        STACKIT project ID to which the volume is associated.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The server ID of the server to which the volume is attached to.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        The size of the volume in GB. It can only be updated to a larger value than the current size. Either `size` or `source` must be provided
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input['VolumeSourceArgs']]:
        """
        The source of the volume. It can be either a volume, an image, a snapshot or a backup. Either `size` or `source` must be provided
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input['VolumeSourceArgs']]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The volume ID.
        """
        return pulumi.get(self, "volume_id")

    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "volume_id", value)


@pulumi.type_token("stackit:index/volume:Volume")
class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 performance_class: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 size: Optional[pulumi.Input[builtins.int]] = None,
                 source: Optional[pulumi.Input[Union['VolumeSourceArgs', 'VolumeSourceArgsDict']]] = None,
                 __props__=None):
        """
        Volume resource schema. Must have a `region` specified in the provider configuration.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] availability_zone: The availability zone of the volume.
        :param pulumi.Input[builtins.str] description: The description of the volume.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a resource container
        :param pulumi.Input[builtins.str] name: The name of the volume.
        :param pulumi.Input[builtins.str] performance_class: The performance class of the volume. Possible values are documented in [Service plans BlockStorage](https://docs.stackit.cloud/stackit/en/service-plans-blockstorage-75137974.html#ServiceplansBlockStorage-CurrentlyavailableServicePlans%28performanceclasses%29)
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the volume is associated.
        :param pulumi.Input[builtins.int] size: The size of the volume in GB. It can only be updated to a larger value than the current size. Either `size` or `source` must be provided
        :param pulumi.Input[Union['VolumeSourceArgs', 'VolumeSourceArgsDict']] source: The source of the volume. It can be either a volume, an image, a snapshot or a backup. Either `size` or `source` must be provided
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Volume resource schema. Must have a `region` specified in the provider configuration.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 performance_class: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 size: Optional[pulumi.Input[builtins.int]] = None,
                 source: Optional[pulumi.Input[Union['VolumeSourceArgs', 'VolumeSourceArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeArgs.__new__(VolumeArgs)

            if availability_zone is None and not opts.urn:
                raise TypeError("Missing required property 'availability_zone'")
            __props__.__dict__["availability_zone"] = availability_zone
            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            __props__.__dict__["performance_class"] = performance_class
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["size"] = size
            __props__.__dict__["source"] = source
            __props__.__dict__["server_id"] = None
            __props__.__dict__["volume_id"] = None
        super(Volume, __self__).__init__(
            'stackit:index/volume:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            availability_zone: Optional[pulumi.Input[builtins.str]] = None,
            description: Optional[pulumi.Input[builtins.str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            performance_class: Optional[pulumi.Input[builtins.str]] = None,
            project_id: Optional[pulumi.Input[builtins.str]] = None,
            server_id: Optional[pulumi.Input[builtins.str]] = None,
            size: Optional[pulumi.Input[builtins.int]] = None,
            source: Optional[pulumi.Input[Union['VolumeSourceArgs', 'VolumeSourceArgsDict']]] = None,
            volume_id: Optional[pulumi.Input[builtins.str]] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] availability_zone: The availability zone of the volume.
        :param pulumi.Input[builtins.str] description: The description of the volume.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a resource container
        :param pulumi.Input[builtins.str] name: The name of the volume.
        :param pulumi.Input[builtins.str] performance_class: The performance class of the volume. Possible values are documented in [Service plans BlockStorage](https://docs.stackit.cloud/stackit/en/service-plans-blockstorage-75137974.html#ServiceplansBlockStorage-CurrentlyavailableServicePlans%28performanceclasses%29)
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the volume is associated.
        :param pulumi.Input[builtins.str] server_id: The server ID of the server to which the volume is attached to.
        :param pulumi.Input[builtins.int] size: The size of the volume in GB. It can only be updated to a larger value than the current size. Either `size` or `source` must be provided
        :param pulumi.Input[Union['VolumeSourceArgs', 'VolumeSourceArgsDict']] source: The source of the volume. It can be either a volume, an image, a snapshot or a backup. Either `size` or `source` must be provided
        :param pulumi.Input[builtins.str] volume_id: The volume ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VolumeState.__new__(_VolumeState)

        __props__.__dict__["availability_zone"] = availability_zone
        __props__.__dict__["description"] = description
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["performance_class"] = performance_class
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["server_id"] = server_id
        __props__.__dict__["size"] = size
        __props__.__dict__["source"] = source
        __props__.__dict__["volume_id"] = volume_id
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[builtins.str]:
        """
        The availability zone of the volume.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[builtins.str]:
        """
        The description of the volume.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        Labels are key-value string pairs which can be attached to a resource container
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the volume.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="performanceClass")
    def performance_class(self) -> pulumi.Output[builtins.str]:
        """
        The performance class of the volume. Possible values are documented in [Service plans BlockStorage](https://docs.stackit.cloud/stackit/en/service-plans-blockstorage-75137974.html#ServiceplansBlockStorage-CurrentlyavailableServicePlans%28performanceclasses%29)
        """
        return pulumi.get(self, "performance_class")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[builtins.str]:
        """
        STACKIT project ID to which the volume is associated.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[builtins.str]:
        """
        The server ID of the server to which the volume is attached to.
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[builtins.int]:
        """
        The size of the volume in GB. It can only be updated to a larger value than the current size. Either `size` or `source` must be provided
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional['outputs.VolumeSource']]:
        """
        The source of the volume. It can be either a volume, an image, a snapshot or a backup. Either `size` or `source` must be provided
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Output[builtins.str]:
        """
        The volume ID.
        """
        return pulumi.get(self, "volume_id")


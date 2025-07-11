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

__all__ = ['ResourcemanagerProjectArgs', 'ResourcemanagerProject']

@pulumi.input_type
class ResourcemanagerProjectArgs:
    def __init__(__self__, *,
                 owner_email: pulumi.Input[builtins.str],
                 parent_container_id: pulumi.Input[builtins.str],
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a ResourcemanagerProject resource.
        :param pulumi.Input[builtins.str] owner_email: Email address of the owner of the project. This value is only considered during creation. Changing it afterwards will have no effect.
        :param pulumi.Input[builtins.str] parent_container_id: Parent resource identifier. Both container ID (user-friendly) and UUID are supported
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a resource container. A label key must match the regex [A-ZÄÜÖa-zäüöß0-9*-]{1,64}. A label value must match the regex ^$|[A-ZÄÜÖa-zäüöß0-9*-]{1,64}. To add a project to a STACKIT Network Area, setting the label `networkArea=<networkAreaID>` is required.
        :param pulumi.Input[builtins.str] name: Project name.
        """
        pulumi.set(__self__, "owner_email", owner_email)
        pulumi.set(__self__, "parent_container_id", parent_container_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="ownerEmail")
    def owner_email(self) -> pulumi.Input[builtins.str]:
        """
        Email address of the owner of the project. This value is only considered during creation. Changing it afterwards will have no effect.
        """
        return pulumi.get(self, "owner_email")

    @owner_email.setter
    def owner_email(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "owner_email", value)

    @property
    @pulumi.getter(name="parentContainerId")
    def parent_container_id(self) -> pulumi.Input[builtins.str]:
        """
        Parent resource identifier. Both container ID (user-friendly) and UUID are supported
        """
        return pulumi.get(self, "parent_container_id")

    @parent_container_id.setter
    def parent_container_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "parent_container_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Labels are key-value string pairs which can be attached to a resource container. A label key must match the regex [A-ZÄÜÖa-zäüöß0-9*-]{1,64}. A label value must match the regex ^$|[A-ZÄÜÖa-zäüöß0-9*-]{1,64}. To add a project to a STACKIT Network Area, setting the label `networkArea=<networkAreaID>` is required.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Project name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ResourcemanagerProjectState:
    def __init__(__self__, *,
                 container_id: Optional[pulumi.Input[builtins.str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 owner_email: Optional[pulumi.Input[builtins.str]] = None,
                 parent_container_id: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering ResourcemanagerProject resources.
        :param pulumi.Input[builtins.str] container_id: Project container ID. Globally unique, user-friendly identifier.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a resource container. A label key must match the regex [A-ZÄÜÖa-zäüöß0-9*-]{1,64}. A label value must match the regex ^$|[A-ZÄÜÖa-zäüöß0-9*-]{1,64}. To add a project to a STACKIT Network Area, setting the label `networkArea=<networkAreaID>` is required.
        :param pulumi.Input[builtins.str] name: Project name.
        :param pulumi.Input[builtins.str] owner_email: Email address of the owner of the project. This value is only considered during creation. Changing it afterwards will have no effect.
        :param pulumi.Input[builtins.str] parent_container_id: Parent resource identifier. Both container ID (user-friendly) and UUID are supported
        :param pulumi.Input[builtins.str] project_id: Project UUID identifier. This is the ID that can be used in most of the other resources to identify the project.
        """
        if container_id is not None:
            pulumi.set(__self__, "container_id", container_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner_email is not None:
            pulumi.set(__self__, "owner_email", owner_email)
        if parent_container_id is not None:
            pulumi.set(__self__, "parent_container_id", parent_container_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Project container ID. Globally unique, user-friendly identifier.
        """
        return pulumi.get(self, "container_id")

    @container_id.setter
    def container_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "container_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Labels are key-value string pairs which can be attached to a resource container. A label key must match the regex [A-ZÄÜÖa-zäüöß0-9*-]{1,64}. A label value must match the regex ^$|[A-ZÄÜÖa-zäüöß0-9*-]{1,64}. To add a project to a STACKIT Network Area, setting the label `networkArea=<networkAreaID>` is required.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Project name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ownerEmail")
    def owner_email(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Email address of the owner of the project. This value is only considered during creation. Changing it afterwards will have no effect.
        """
        return pulumi.get(self, "owner_email")

    @owner_email.setter
    def owner_email(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "owner_email", value)

    @property
    @pulumi.getter(name="parentContainerId")
    def parent_container_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Parent resource identifier. Both container ID (user-friendly) and UUID are supported
        """
        return pulumi.get(self, "parent_container_id")

    @parent_container_id.setter
    def parent_container_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "parent_container_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Project UUID identifier. This is the ID that can be used in most of the other resources to identify the project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "project_id", value)


@pulumi.type_token("stackit:index/resourcemanagerProject:ResourcemanagerProject")
class ResourcemanagerProject(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 owner_email: Optional[pulumi.Input[builtins.str]] = None,
                 parent_container_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a resource container. A label key must match the regex [A-ZÄÜÖa-zäüöß0-9*-]{1,64}. A label value must match the regex ^$|[A-ZÄÜÖa-zäüöß0-9*-]{1,64}. To add a project to a STACKIT Network Area, setting the label `networkArea=<networkAreaID>` is required.
        :param pulumi.Input[builtins.str] name: Project name.
        :param pulumi.Input[builtins.str] owner_email: Email address of the owner of the project. This value is only considered during creation. Changing it afterwards will have no effect.
        :param pulumi.Input[builtins.str] parent_container_id: Parent resource identifier. Both container ID (user-friendly) and UUID are supported
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourcemanagerProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        :param str resource_name: The name of the resource.
        :param ResourcemanagerProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourcemanagerProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 owner_email: Optional[pulumi.Input[builtins.str]] = None,
                 parent_container_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResourcemanagerProjectArgs.__new__(ResourcemanagerProjectArgs)

            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            if owner_email is None and not opts.urn:
                raise TypeError("Missing required property 'owner_email'")
            __props__.__dict__["owner_email"] = owner_email
            if parent_container_id is None and not opts.urn:
                raise TypeError("Missing required property 'parent_container_id'")
            __props__.__dict__["parent_container_id"] = parent_container_id
            __props__.__dict__["container_id"] = None
            __props__.__dict__["project_id"] = None
        super(ResourcemanagerProject, __self__).__init__(
            'stackit:index/resourcemanagerProject:ResourcemanagerProject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            container_id: Optional[pulumi.Input[builtins.str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            owner_email: Optional[pulumi.Input[builtins.str]] = None,
            parent_container_id: Optional[pulumi.Input[builtins.str]] = None,
            project_id: Optional[pulumi.Input[builtins.str]] = None) -> 'ResourcemanagerProject':
        """
        Get an existing ResourcemanagerProject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] container_id: Project container ID. Globally unique, user-friendly identifier.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] labels: Labels are key-value string pairs which can be attached to a resource container. A label key must match the regex [A-ZÄÜÖa-zäüöß0-9*-]{1,64}. A label value must match the regex ^$|[A-ZÄÜÖa-zäüöß0-9*-]{1,64}. To add a project to a STACKIT Network Area, setting the label `networkArea=<networkAreaID>` is required.
        :param pulumi.Input[builtins.str] name: Project name.
        :param pulumi.Input[builtins.str] owner_email: Email address of the owner of the project. This value is only considered during creation. Changing it afterwards will have no effect.
        :param pulumi.Input[builtins.str] parent_container_id: Parent resource identifier. Both container ID (user-friendly) and UUID are supported
        :param pulumi.Input[builtins.str] project_id: Project UUID identifier. This is the ID that can be used in most of the other resources to identify the project.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ResourcemanagerProjectState.__new__(_ResourcemanagerProjectState)

        __props__.__dict__["container_id"] = container_id
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["owner_email"] = owner_email
        __props__.__dict__["parent_container_id"] = parent_container_id
        __props__.__dict__["project_id"] = project_id
        return ResourcemanagerProject(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> pulumi.Output[builtins.str]:
        """
        Project container ID. Globally unique, user-friendly identifier.
        """
        return pulumi.get(self, "container_id")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        Labels are key-value string pairs which can be attached to a resource container. A label key must match the regex [A-ZÄÜÖa-zäüöß0-9*-]{1,64}. A label value must match the regex ^$|[A-ZÄÜÖa-zäüöß0-9*-]{1,64}. To add a project to a STACKIT Network Area, setting the label `networkArea=<networkAreaID>` is required.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        Project name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerEmail")
    def owner_email(self) -> pulumi.Output[builtins.str]:
        """
        Email address of the owner of the project. This value is only considered during creation. Changing it afterwards will have no effect.
        """
        return pulumi.get(self, "owner_email")

    @property
    @pulumi.getter(name="parentContainerId")
    def parent_container_id(self) -> pulumi.Output[builtins.str]:
        """
        Parent resource identifier. Both container ID (user-friendly) and UUID are supported
        """
        return pulumi.get(self, "parent_container_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[builtins.str]:
        """
        Project UUID identifier. This is the ID that can be used in most of the other resources to identify the project.
        """
        return pulumi.get(self, "project_id")


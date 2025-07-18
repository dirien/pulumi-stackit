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

__all__ = ['AuthorizationProjectRoleAssignmentArgs', 'AuthorizationProjectRoleAssignment']

@pulumi.input_type
class AuthorizationProjectRoleAssignmentArgs:
    def __init__(__self__, *,
                 resource_id: pulumi.Input[builtins.str],
                 role: pulumi.Input[builtins.str],
                 subject: pulumi.Input[builtins.str]):
        """
        The set of arguments for constructing a AuthorizationProjectRoleAssignment resource.
        :param pulumi.Input[builtins.str] resource_id: project Resource to assign the role to.
        :param pulumi.Input[builtins.str] role: Role to be assigned
        :param pulumi.Input[builtins.str] subject: Identifier of user, service account or client. Usually email address or name in case of clients
        """
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "role", role)
        pulumi.set(__self__, "subject", subject)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[builtins.str]:
        """
        project Resource to assign the role to.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[builtins.str]:
        """
        Role to be assigned
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Input[builtins.str]:
        """
        Identifier of user, service account or client. Usually email address or name in case of clients
        """
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "subject", value)


@pulumi.input_type
class _AuthorizationProjectRoleAssignmentState:
    def __init__(__self__, *,
                 resource_id: Optional[pulumi.Input[builtins.str]] = None,
                 role: Optional[pulumi.Input[builtins.str]] = None,
                 subject: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering AuthorizationProjectRoleAssignment resources.
        :param pulumi.Input[builtins.str] resource_id: project Resource to assign the role to.
        :param pulumi.Input[builtins.str] role: Role to be assigned
        :param pulumi.Input[builtins.str] subject: Identifier of user, service account or client. Usually email address or name in case of clients
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if subject is not None:
            pulumi.set(__self__, "subject", subject)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        project Resource to assign the role to.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Role to be assigned
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Identifier of user, service account or client. Usually email address or name in case of clients
        """
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "subject", value)


@pulumi.type_token("stackit:index/authorizationProjectRoleAssignment:AuthorizationProjectRoleAssignment")
class AuthorizationProjectRoleAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_id: Optional[pulumi.Input[builtins.str]] = None,
                 role: Optional[pulumi.Input[builtins.str]] = None,
                 subject: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        project Role Assignment resource schema.

        > This resource is part of the iam experiment and is likely going to undergo significant changes or be removed in the future. Use it at your own discretion.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] resource_id: project Resource to assign the role to.
        :param pulumi.Input[builtins.str] role: Role to be assigned
        :param pulumi.Input[builtins.str] subject: Identifier of user, service account or client. Usually email address or name in case of clients
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuthorizationProjectRoleAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        project Role Assignment resource schema.

        > This resource is part of the iam experiment and is likely going to undergo significant changes or be removed in the future. Use it at your own discretion.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param AuthorizationProjectRoleAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuthorizationProjectRoleAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_id: Optional[pulumi.Input[builtins.str]] = None,
                 role: Optional[pulumi.Input[builtins.str]] = None,
                 subject: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AuthorizationProjectRoleAssignmentArgs.__new__(AuthorizationProjectRoleAssignmentArgs)

            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            if subject is None and not opts.urn:
                raise TypeError("Missing required property 'subject'")
            __props__.__dict__["subject"] = subject
        super(AuthorizationProjectRoleAssignment, __self__).__init__(
            'stackit:index/authorizationProjectRoleAssignment:AuthorizationProjectRoleAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            resource_id: Optional[pulumi.Input[builtins.str]] = None,
            role: Optional[pulumi.Input[builtins.str]] = None,
            subject: Optional[pulumi.Input[builtins.str]] = None) -> 'AuthorizationProjectRoleAssignment':
        """
        Get an existing AuthorizationProjectRoleAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] resource_id: project Resource to assign the role to.
        :param pulumi.Input[builtins.str] role: Role to be assigned
        :param pulumi.Input[builtins.str] subject: Identifier of user, service account or client. Usually email address or name in case of clients
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AuthorizationProjectRoleAssignmentState.__new__(_AuthorizationProjectRoleAssignmentState)

        __props__.__dict__["resource_id"] = resource_id
        __props__.__dict__["role"] = role
        __props__.__dict__["subject"] = subject
        return AuthorizationProjectRoleAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[builtins.str]:
        """
        project Resource to assign the role to.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[builtins.str]:
        """
        Role to be assigned
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Output[builtins.str]:
        """
        Identifier of user, service account or client. Usually email address or name in case of clients
        """
        return pulumi.get(self, "subject")


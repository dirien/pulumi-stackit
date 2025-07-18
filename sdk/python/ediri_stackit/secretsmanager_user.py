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

__all__ = ['SecretsmanagerUserArgs', 'SecretsmanagerUser']

@pulumi.input_type
class SecretsmanagerUserArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[builtins.str],
                 instance_id: pulumi.Input[builtins.str],
                 project_id: pulumi.Input[builtins.str],
                 write_enabled: pulumi.Input[builtins.bool]):
        """
        The set of arguments for constructing a SecretsmanagerUser resource.
        :param pulumi.Input[builtins.str] description: A user chosen description to differentiate between multiple users. Can't be changed after creation.
        :param pulumi.Input[builtins.str] instance_id: ID of the Secrets Manager instance.
        :param pulumi.Input[builtins.str] project_id: STACKIT Project ID to which the instance is associated.
        :param pulumi.Input[builtins.bool] write_enabled: If true, the user has writeaccess to the secrets engine.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "write_enabled", write_enabled)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[builtins.str]:
        """
        A user chosen description to differentiate between multiple users. Can't be changed after creation.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[builtins.str]:
        """
        ID of the Secrets Manager instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[builtins.str]:
        """
        STACKIT Project ID to which the instance is associated.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="writeEnabled")
    def write_enabled(self) -> pulumi.Input[builtins.bool]:
        """
        If true, the user has writeaccess to the secrets engine.
        """
        return pulumi.get(self, "write_enabled")

    @write_enabled.setter
    def write_enabled(self, value: pulumi.Input[builtins.bool]):
        pulumi.set(self, "write_enabled", value)


@pulumi.input_type
class _SecretsmanagerUserState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 instance_id: Optional[pulumi.Input[builtins.str]] = None,
                 password: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 user_id: Optional[pulumi.Input[builtins.str]] = None,
                 username: Optional[pulumi.Input[builtins.str]] = None,
                 write_enabled: Optional[pulumi.Input[builtins.bool]] = None):
        """
        Input properties used for looking up and filtering SecretsmanagerUser resources.
        :param pulumi.Input[builtins.str] description: A user chosen description to differentiate between multiple users. Can't be changed after creation.
        :param pulumi.Input[builtins.str] instance_id: ID of the Secrets Manager instance.
        :param pulumi.Input[builtins.str] password: An auto-generated password.
        :param pulumi.Input[builtins.str] project_id: STACKIT Project ID to which the instance is associated.
        :param pulumi.Input[builtins.str] user_id: The user's ID.
        :param pulumi.Input[builtins.str] username: An auto-generated user name.
        :param pulumi.Input[builtins.bool] write_enabled: If true, the user has writeaccess to the secrets engine.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)
        if username is not None:
            pulumi.set(__self__, "username", username)
        if write_enabled is not None:
            pulumi.set(__self__, "write_enabled", write_enabled)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A user chosen description to differentiate between multiple users. Can't be changed after creation.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        ID of the Secrets Manager instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        An auto-generated password.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        STACKIT Project ID to which the instance is associated.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The user's ID.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        An auto-generated user name.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="writeEnabled")
    def write_enabled(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        If true, the user has writeaccess to the secrets engine.
        """
        return pulumi.get(self, "write_enabled")

    @write_enabled.setter
    def write_enabled(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "write_enabled", value)


@pulumi.type_token("stackit:index/secretsmanagerUser:SecretsmanagerUser")
class SecretsmanagerUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 instance_id: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 write_enabled: Optional[pulumi.Input[builtins.bool]] = None,
                 __props__=None):
        """
        Secrets Manager user resource schema. Must have a `region` specified in the provider configuration.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] description: A user chosen description to differentiate between multiple users. Can't be changed after creation.
        :param pulumi.Input[builtins.str] instance_id: ID of the Secrets Manager instance.
        :param pulumi.Input[builtins.str] project_id: STACKIT Project ID to which the instance is associated.
        :param pulumi.Input[builtins.bool] write_enabled: If true, the user has writeaccess to the secrets engine.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecretsmanagerUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Secrets Manager user resource schema. Must have a `region` specified in the provider configuration.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param SecretsmanagerUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecretsmanagerUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 instance_id: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 write_enabled: Optional[pulumi.Input[builtins.bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecretsmanagerUserArgs.__new__(SecretsmanagerUserArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            if write_enabled is None and not opts.urn:
                raise TypeError("Missing required property 'write_enabled'")
            __props__.__dict__["write_enabled"] = write_enabled
            __props__.__dict__["password"] = None
            __props__.__dict__["user_id"] = None
            __props__.__dict__["username"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(SecretsmanagerUser, __self__).__init__(
            'stackit:index/secretsmanagerUser:SecretsmanagerUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[builtins.str]] = None,
            instance_id: Optional[pulumi.Input[builtins.str]] = None,
            password: Optional[pulumi.Input[builtins.str]] = None,
            project_id: Optional[pulumi.Input[builtins.str]] = None,
            user_id: Optional[pulumi.Input[builtins.str]] = None,
            username: Optional[pulumi.Input[builtins.str]] = None,
            write_enabled: Optional[pulumi.Input[builtins.bool]] = None) -> 'SecretsmanagerUser':
        """
        Get an existing SecretsmanagerUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] description: A user chosen description to differentiate between multiple users. Can't be changed after creation.
        :param pulumi.Input[builtins.str] instance_id: ID of the Secrets Manager instance.
        :param pulumi.Input[builtins.str] password: An auto-generated password.
        :param pulumi.Input[builtins.str] project_id: STACKIT Project ID to which the instance is associated.
        :param pulumi.Input[builtins.str] user_id: The user's ID.
        :param pulumi.Input[builtins.str] username: An auto-generated user name.
        :param pulumi.Input[builtins.bool] write_enabled: If true, the user has writeaccess to the secrets engine.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecretsmanagerUserState.__new__(_SecretsmanagerUserState)

        __props__.__dict__["description"] = description
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["password"] = password
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["user_id"] = user_id
        __props__.__dict__["username"] = username
        __props__.__dict__["write_enabled"] = write_enabled
        return SecretsmanagerUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[builtins.str]:
        """
        A user chosen description to differentiate between multiple users. Can't be changed after creation.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[builtins.str]:
        """
        ID of the Secrets Manager instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[builtins.str]:
        """
        An auto-generated password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[builtins.str]:
        """
        STACKIT Project ID to which the instance is associated.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[builtins.str]:
        """
        The user's ID.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[builtins.str]:
        """
        An auto-generated user name.
        """
        return pulumi.get(self, "username")

    @property
    @pulumi.getter(name="writeEnabled")
    def write_enabled(self) -> pulumi.Output[builtins.bool]:
        """
        If true, the user has writeaccess to the secrets engine.
        """
        return pulumi.get(self, "write_enabled")


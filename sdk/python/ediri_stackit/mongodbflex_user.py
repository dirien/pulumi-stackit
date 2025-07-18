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

__all__ = ['MongodbflexUserArgs', 'MongodbflexUser']

@pulumi.input_type
class MongodbflexUserArgs:
    def __init__(__self__, *,
                 database: pulumi.Input[builtins.str],
                 instance_id: pulumi.Input[builtins.str],
                 project_id: pulumi.Input[builtins.str],
                 roles: pulumi.Input[Sequence[pulumi.Input[builtins.str]]],
                 username: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a MongodbflexUser resource.
        :param pulumi.Input[builtins.str] instance_id: ID of the MongoDB Flex instance.
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the instance is associated.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] roles: Database access levels for the user. Some of the possible values are: [`read`, `readWrite`, `readWriteAnyDatabase`]
        """
        pulumi.set(__self__, "database", database)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "roles", roles)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[builtins.str]:
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[builtins.str]:
        """
        ID of the MongoDB Flex instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[builtins.str]:
        """
        STACKIT project ID to which the instance is associated.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Input[Sequence[pulumi.Input[builtins.str]]]:
        """
        Database access levels for the user. Some of the possible values are: [`read`, `readWrite`, `readWriteAnyDatabase`]
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: pulumi.Input[Sequence[pulumi.Input[builtins.str]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class _MongodbflexUserState:
    def __init__(__self__, *,
                 database: Optional[pulumi.Input[builtins.str]] = None,
                 host: Optional[pulumi.Input[builtins.str]] = None,
                 instance_id: Optional[pulumi.Input[builtins.str]] = None,
                 password: Optional[pulumi.Input[builtins.str]] = None,
                 port: Optional[pulumi.Input[builtins.int]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 uri: Optional[pulumi.Input[builtins.str]] = None,
                 user_id: Optional[pulumi.Input[builtins.str]] = None,
                 username: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering MongodbflexUser resources.
        :param pulumi.Input[builtins.str] instance_id: ID of the MongoDB Flex instance.
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the instance is associated.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] roles: Database access levels for the user. Some of the possible values are: [`read`, `readWrite`, `readWriteAnyDatabase`]
        :param pulumi.Input[builtins.str] user_id: User ID.
        """
        if database is not None:
            pulumi.set(__self__, "database", database)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        ID of the MongoDB Flex instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        STACKIT project ID to which the instance is associated.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        Database access levels for the user. Some of the possible values are: [`read`, `readWrite`, `readWriteAnyDatabase`]
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        User ID.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "username", value)


@pulumi.type_token("stackit:index/mongodbflexUser:MongodbflexUser")
class MongodbflexUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database: Optional[pulumi.Input[builtins.str]] = None,
                 instance_id: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 username: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        MongoDB Flex user resource schema. Must have a `region` specified in the provider configuration.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] instance_id: ID of the MongoDB Flex instance.
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the instance is associated.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] roles: Database access levels for the user. Some of the possible values are: [`read`, `readWrite`, `readWriteAnyDatabase`]
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MongodbflexUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        MongoDB Flex user resource schema. Must have a `region` specified in the provider configuration.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param MongodbflexUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MongodbflexUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database: Optional[pulumi.Input[builtins.str]] = None,
                 instance_id: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 username: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MongodbflexUserArgs.__new__(MongodbflexUserArgs)

            if database is None and not opts.urn:
                raise TypeError("Missing required property 'database'")
            __props__.__dict__["database"] = database
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            if roles is None and not opts.urn:
                raise TypeError("Missing required property 'roles'")
            __props__.__dict__["roles"] = roles
            __props__.__dict__["username"] = username
            __props__.__dict__["host"] = None
            __props__.__dict__["password"] = None
            __props__.__dict__["port"] = None
            __props__.__dict__["uri"] = None
            __props__.__dict__["user_id"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password", "uri"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(MongodbflexUser, __self__).__init__(
            'stackit:index/mongodbflexUser:MongodbflexUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            database: Optional[pulumi.Input[builtins.str]] = None,
            host: Optional[pulumi.Input[builtins.str]] = None,
            instance_id: Optional[pulumi.Input[builtins.str]] = None,
            password: Optional[pulumi.Input[builtins.str]] = None,
            port: Optional[pulumi.Input[builtins.int]] = None,
            project_id: Optional[pulumi.Input[builtins.str]] = None,
            roles: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
            uri: Optional[pulumi.Input[builtins.str]] = None,
            user_id: Optional[pulumi.Input[builtins.str]] = None,
            username: Optional[pulumi.Input[builtins.str]] = None) -> 'MongodbflexUser':
        """
        Get an existing MongodbflexUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] instance_id: ID of the MongoDB Flex instance.
        :param pulumi.Input[builtins.str] project_id: STACKIT project ID to which the instance is associated.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] roles: Database access levels for the user. Some of the possible values are: [`read`, `readWrite`, `readWriteAnyDatabase`]
        :param pulumi.Input[builtins.str] user_id: User ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MongodbflexUserState.__new__(_MongodbflexUserState)

        __props__.__dict__["database"] = database
        __props__.__dict__["host"] = host
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["password"] = password
        __props__.__dict__["port"] = port
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["roles"] = roles
        __props__.__dict__["uri"] = uri
        __props__.__dict__["user_id"] = user_id
        __props__.__dict__["username"] = username
        return MongodbflexUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output[builtins.str]:
        return pulumi.get(self, "database")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[builtins.str]:
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[builtins.str]:
        """
        ID of the MongoDB Flex instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[builtins.str]:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[builtins.int]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[builtins.str]:
        """
        STACKIT project ID to which the instance is associated.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        Database access levels for the user. Some of the possible values are: [`read`, `readWrite`, `readWriteAnyDatabase`]
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[builtins.str]:
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[builtins.str]:
        """
        User ID.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[builtins.str]:
        return pulumi.get(self, "username")


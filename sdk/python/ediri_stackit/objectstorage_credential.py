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

__all__ = ['ObjectstorageCredentialArgs', 'ObjectstorageCredential']

@pulumi.input_type
class ObjectstorageCredentialArgs:
    def __init__(__self__, *,
                 credentials_group_id: pulumi.Input[builtins.str],
                 project_id: pulumi.Input[builtins.str],
                 expiration_timestamp: Optional[pulumi.Input[builtins.str]] = None,
                 region: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a ObjectstorageCredential resource.
        :param pulumi.Input[builtins.str] credentials_group_id: The credential group ID.
        :param pulumi.Input[builtins.str] project_id: STACKIT Project ID to which the credential group is associated.
        :param pulumi.Input[builtins.str] expiration_timestamp: Expiration timestamp, in RFC339 format without fractional seconds. Example: "2025-01-01T00:00:00Z". If not set, the credential never expires.
        :param pulumi.Input[builtins.str] region: The resource region. If not defined, the provider region is used.
        """
        pulumi.set(__self__, "credentials_group_id", credentials_group_id)
        pulumi.set(__self__, "project_id", project_id)
        if expiration_timestamp is not None:
            pulumi.set(__self__, "expiration_timestamp", expiration_timestamp)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="credentialsGroupId")
    def credentials_group_id(self) -> pulumi.Input[builtins.str]:
        """
        The credential group ID.
        """
        return pulumi.get(self, "credentials_group_id")

    @credentials_group_id.setter
    def credentials_group_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "credentials_group_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[builtins.str]:
        """
        STACKIT Project ID to which the credential group is associated.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="expirationTimestamp")
    def expiration_timestamp(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Expiration timestamp, in RFC339 format without fractional seconds. Example: "2025-01-01T00:00:00Z". If not set, the credential never expires.
        """
        return pulumi.get(self, "expiration_timestamp")

    @expiration_timestamp.setter
    def expiration_timestamp(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "expiration_timestamp", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The resource region. If not defined, the provider region is used.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _ObjectstorageCredentialState:
    def __init__(__self__, *,
                 access_key: Optional[pulumi.Input[builtins.str]] = None,
                 credential_id: Optional[pulumi.Input[builtins.str]] = None,
                 credentials_group_id: Optional[pulumi.Input[builtins.str]] = None,
                 expiration_timestamp: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 region: Optional[pulumi.Input[builtins.str]] = None,
                 secret_access_key: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering ObjectstorageCredential resources.
        :param pulumi.Input[builtins.str] credential_id: The credential ID.
        :param pulumi.Input[builtins.str] credentials_group_id: The credential group ID.
        :param pulumi.Input[builtins.str] expiration_timestamp: Expiration timestamp, in RFC339 format without fractional seconds. Example: "2025-01-01T00:00:00Z". If not set, the credential never expires.
        :param pulumi.Input[builtins.str] project_id: STACKIT Project ID to which the credential group is associated.
        :param pulumi.Input[builtins.str] region: The resource region. If not defined, the provider region is used.
        """
        if access_key is not None:
            pulumi.set(__self__, "access_key", access_key)
        if credential_id is not None:
            pulumi.set(__self__, "credential_id", credential_id)
        if credentials_group_id is not None:
            pulumi.set(__self__, "credentials_group_id", credentials_group_id)
        if expiration_timestamp is not None:
            pulumi.set(__self__, "expiration_timestamp", expiration_timestamp)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if secret_access_key is not None:
            pulumi.set(__self__, "secret_access_key", secret_access_key)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "access_key")

    @access_key.setter
    def access_key(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "access_key", value)

    @property
    @pulumi.getter(name="credentialId")
    def credential_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The credential ID.
        """
        return pulumi.get(self, "credential_id")

    @credential_id.setter
    def credential_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "credential_id", value)

    @property
    @pulumi.getter(name="credentialsGroupId")
    def credentials_group_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The credential group ID.
        """
        return pulumi.get(self, "credentials_group_id")

    @credentials_group_id.setter
    def credentials_group_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "credentials_group_id", value)

    @property
    @pulumi.getter(name="expirationTimestamp")
    def expiration_timestamp(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Expiration timestamp, in RFC339 format without fractional seconds. Example: "2025-01-01T00:00:00Z". If not set, the credential never expires.
        """
        return pulumi.get(self, "expiration_timestamp")

    @expiration_timestamp.setter
    def expiration_timestamp(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "expiration_timestamp", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        STACKIT Project ID to which the credential group is associated.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The resource region. If not defined, the provider region is used.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "secret_access_key")

    @secret_access_key.setter
    def secret_access_key(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "secret_access_key", value)


@pulumi.type_token("stackit:index/objectstorageCredential:ObjectstorageCredential")
class ObjectstorageCredential(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials_group_id: Optional[pulumi.Input[builtins.str]] = None,
                 expiration_timestamp: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 region: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        ObjectStorage credential resource schema. Must have a `region` specified in the provider configuration.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] credentials_group_id: The credential group ID.
        :param pulumi.Input[builtins.str] expiration_timestamp: Expiration timestamp, in RFC339 format without fractional seconds. Example: "2025-01-01T00:00:00Z". If not set, the credential never expires.
        :param pulumi.Input[builtins.str] project_id: STACKIT Project ID to which the credential group is associated.
        :param pulumi.Input[builtins.str] region: The resource region. If not defined, the provider region is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ObjectstorageCredentialArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ObjectStorage credential resource schema. Must have a `region` specified in the provider configuration.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param ObjectstorageCredentialArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ObjectstorageCredentialArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials_group_id: Optional[pulumi.Input[builtins.str]] = None,
                 expiration_timestamp: Optional[pulumi.Input[builtins.str]] = None,
                 project_id: Optional[pulumi.Input[builtins.str]] = None,
                 region: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ObjectstorageCredentialArgs.__new__(ObjectstorageCredentialArgs)

            if credentials_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'credentials_group_id'")
            __props__.__dict__["credentials_group_id"] = credentials_group_id
            __props__.__dict__["expiration_timestamp"] = expiration_timestamp
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["region"] = region
            __props__.__dict__["access_key"] = None
            __props__.__dict__["credential_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["secret_access_key"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["secretAccessKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ObjectstorageCredential, __self__).__init__(
            'stackit:index/objectstorageCredential:ObjectstorageCredential',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_key: Optional[pulumi.Input[builtins.str]] = None,
            credential_id: Optional[pulumi.Input[builtins.str]] = None,
            credentials_group_id: Optional[pulumi.Input[builtins.str]] = None,
            expiration_timestamp: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            project_id: Optional[pulumi.Input[builtins.str]] = None,
            region: Optional[pulumi.Input[builtins.str]] = None,
            secret_access_key: Optional[pulumi.Input[builtins.str]] = None) -> 'ObjectstorageCredential':
        """
        Get an existing ObjectstorageCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] credential_id: The credential ID.
        :param pulumi.Input[builtins.str] credentials_group_id: The credential group ID.
        :param pulumi.Input[builtins.str] expiration_timestamp: Expiration timestamp, in RFC339 format without fractional seconds. Example: "2025-01-01T00:00:00Z". If not set, the credential never expires.
        :param pulumi.Input[builtins.str] project_id: STACKIT Project ID to which the credential group is associated.
        :param pulumi.Input[builtins.str] region: The resource region. If not defined, the provider region is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ObjectstorageCredentialState.__new__(_ObjectstorageCredentialState)

        __props__.__dict__["access_key"] = access_key
        __props__.__dict__["credential_id"] = credential_id
        __props__.__dict__["credentials_group_id"] = credentials_group_id
        __props__.__dict__["expiration_timestamp"] = expiration_timestamp
        __props__.__dict__["name"] = name
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["region"] = region
        __props__.__dict__["secret_access_key"] = secret_access_key
        return ObjectstorageCredential(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Output[builtins.str]:
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter(name="credentialId")
    def credential_id(self) -> pulumi.Output[builtins.str]:
        """
        The credential ID.
        """
        return pulumi.get(self, "credential_id")

    @property
    @pulumi.getter(name="credentialsGroupId")
    def credentials_group_id(self) -> pulumi.Output[builtins.str]:
        """
        The credential group ID.
        """
        return pulumi.get(self, "credentials_group_id")

    @property
    @pulumi.getter(name="expirationTimestamp")
    def expiration_timestamp(self) -> pulumi.Output[builtins.str]:
        """
        Expiration timestamp, in RFC339 format without fractional seconds. Example: "2025-01-01T00:00:00Z". If not set, the credential never expires.
        """
        return pulumi.get(self, "expiration_timestamp")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[builtins.str]:
        """
        STACKIT Project ID to which the credential group is associated.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[builtins.str]:
        """
        The resource region. If not defined, the provider region is used.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> pulumi.Output[builtins.str]:
        return pulumi.get(self, "secret_access_key")


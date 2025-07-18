// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Stackit
{
    public static class GetObjectstorageCredential
    {
        /// <summary>
        /// ObjectStorage credential data source schema. Must have a `region` specified in the provider configuration.
        /// 
        /// ## Example Usage
        /// 
        /// ```terraform
        /// data "stackit_objectstorage_credential" "example" {
        ///   project_id           = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ///   credentials_group_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ///   credential_id        = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        /// }
        /// ```
        /// </summary>
        public static Task<GetObjectstorageCredentialResult> InvokeAsync(GetObjectstorageCredentialArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetObjectstorageCredentialResult>("stackit:index/getObjectstorageCredential:getObjectstorageCredential", args ?? new GetObjectstorageCredentialArgs(), options.WithDefaults());

        /// <summary>
        /// ObjectStorage credential data source schema. Must have a `region` specified in the provider configuration.
        /// 
        /// ## Example Usage
        /// 
        /// ```terraform
        /// data "stackit_objectstorage_credential" "example" {
        ///   project_id           = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ///   credentials_group_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ///   credential_id        = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        /// }
        /// ```
        /// </summary>
        public static Output<GetObjectstorageCredentialResult> Invoke(GetObjectstorageCredentialInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetObjectstorageCredentialResult>("stackit:index/getObjectstorageCredential:getObjectstorageCredential", args ?? new GetObjectstorageCredentialInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// ObjectStorage credential data source schema. Must have a `region` specified in the provider configuration.
        /// 
        /// ## Example Usage
        /// 
        /// ```terraform
        /// data "stackit_objectstorage_credential" "example" {
        ///   project_id           = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ///   credentials_group_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ///   credential_id        = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        /// }
        /// ```
        /// </summary>
        public static Output<GetObjectstorageCredentialResult> Invoke(GetObjectstorageCredentialInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetObjectstorageCredentialResult>("stackit:index/getObjectstorageCredential:getObjectstorageCredential", args ?? new GetObjectstorageCredentialInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetObjectstorageCredentialArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The credential ID.
        /// </summary>
        [Input("credentialId", required: true)]
        public string CredentialId { get; set; } = null!;

        /// <summary>
        /// The credential group ID.
        /// </summary>
        [Input("credentialsGroupId", required: true)]
        public string CredentialsGroupId { get; set; } = null!;

        /// <summary>
        /// STACKIT Project ID to which the credential group is associated.
        /// </summary>
        [Input("projectId", required: true)]
        public string ProjectId { get; set; } = null!;

        /// <summary>
        /// The resource region. If not defined, the provider region is used.
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        public GetObjectstorageCredentialArgs()
        {
        }
        public static new GetObjectstorageCredentialArgs Empty => new GetObjectstorageCredentialArgs();
    }

    public sealed class GetObjectstorageCredentialInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The credential ID.
        /// </summary>
        [Input("credentialId", required: true)]
        public Input<string> CredentialId { get; set; } = null!;

        /// <summary>
        /// The credential group ID.
        /// </summary>
        [Input("credentialsGroupId", required: true)]
        public Input<string> CredentialsGroupId { get; set; } = null!;

        /// <summary>
        /// STACKIT Project ID to which the credential group is associated.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        /// <summary>
        /// The resource region. If not defined, the provider region is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public GetObjectstorageCredentialInvokeArgs()
        {
        }
        public static new GetObjectstorageCredentialInvokeArgs Empty => new GetObjectstorageCredentialInvokeArgs();
    }


    [OutputType]
    public sealed class GetObjectstorageCredentialResult
    {
        /// <summary>
        /// The credential ID.
        /// </summary>
        public readonly string CredentialId;
        /// <summary>
        /// The credential group ID.
        /// </summary>
        public readonly string CredentialsGroupId;
        public readonly string ExpirationTimestamp;
        public readonly string Id;
        public readonly string Name;
        /// <summary>
        /// STACKIT Project ID to which the credential group is associated.
        /// </summary>
        public readonly string ProjectId;
        /// <summary>
        /// The resource region. If not defined, the provider region is used.
        /// </summary>
        public readonly string? Region;

        [OutputConstructor]
        private GetObjectstorageCredentialResult(
            string credentialId,

            string credentialsGroupId,

            string expirationTimestamp,

            string id,

            string name,

            string projectId,

            string? region)
        {
            CredentialId = credentialId;
            CredentialsGroupId = credentialsGroupId;
            ExpirationTimestamp = expirationTimestamp;
            Id = id;
            Name = name;
            ProjectId = projectId;
            Region = region;
        }
    }
}

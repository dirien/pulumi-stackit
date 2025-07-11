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
    /// <summary>
    /// Service account resource schema.
    /// 
    /// ## Example Usage
    /// </summary>
    [StackitResourceType("stackit:index/serviceAccount:ServiceAccount")]
    public partial class ServiceAccount : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Email of the service account.
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// Name of the service account.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// STACKIT project ID to which the service account is associated.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;


        /// <summary>
        /// Create a ServiceAccount resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServiceAccount(string name, ServiceAccountArgs args, CustomResourceOptions? options = null)
            : base("stackit:index/serviceAccount:ServiceAccount", name, args ?? new ServiceAccountArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServiceAccount(string name, Input<string> id, ServiceAccountState? state = null, CustomResourceOptions? options = null)
            : base("stackit:index/serviceAccount:ServiceAccount", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/dirien/pulumi-stackit",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ServiceAccount resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServiceAccount Get(string name, Input<string> id, ServiceAccountState? state = null, CustomResourceOptions? options = null)
        {
            return new ServiceAccount(name, id, state, options);
        }
    }

    public sealed class ServiceAccountArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the service account.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// STACKIT project ID to which the service account is associated.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        public ServiceAccountArgs()
        {
        }
        public static new ServiceAccountArgs Empty => new ServiceAccountArgs();
    }

    public sealed class ServiceAccountState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Email of the service account.
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// Name of the service account.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// STACKIT project ID to which the service account is associated.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        public ServiceAccountState()
        {
        }
        public static new ServiceAccountState Empty => new ServiceAccountState();
    }
}

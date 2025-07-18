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
    /// SKE kubeconfig resource schema. Must have a `region` specified in the provider configuration.
    /// 
    /// ## Example Usage
    /// </summary>
    [StackitResourceType("stackit:index/skeKubeconfig:SkeKubeconfig")]
    public partial class SkeKubeconfig : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Name of the SKE cluster.
        /// </summary>
        [Output("clusterName")]
        public Output<string> ClusterName { get; private set; } = null!;

        /// <summary>
        /// Date-time when the kubeconfig was created
        /// </summary>
        [Output("creationTime")]
        public Output<string> CreationTime { get; private set; } = null!;

        /// <summary>
        /// Expiration time of the kubeconfig, in seconds. Defaults to `3600`
        /// </summary>
        [Output("expiration")]
        public Output<int> Expiration { get; private set; } = null!;

        /// <summary>
        /// Timestamp when the kubeconfig expires
        /// </summary>
        [Output("expiresAt")]
        public Output<string> ExpiresAt { get; private set; } = null!;

        /// <summary>
        /// Raw short-lived admin kubeconfig.
        /// </summary>
        [Output("kubeConfig")]
        public Output<string> KubeConfig { get; private set; } = null!;

        [Output("kubeConfigId")]
        public Output<string> KubeConfigId { get; private set; } = null!;

        /// <summary>
        /// STACKIT project ID to which the cluster is associated.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// If set to true, the provider will check if the kubeconfig has expired and will generated a new valid one in-place
        /// </summary>
        [Output("refresh")]
        public Output<bool?> Refresh { get; private set; } = null!;


        /// <summary>
        /// Create a SkeKubeconfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SkeKubeconfig(string name, SkeKubeconfigArgs args, CustomResourceOptions? options = null)
            : base("stackit:index/skeKubeconfig:SkeKubeconfig", name, args ?? new SkeKubeconfigArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SkeKubeconfig(string name, Input<string> id, SkeKubeconfigState? state = null, CustomResourceOptions? options = null)
            : base("stackit:index/skeKubeconfig:SkeKubeconfig", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/dirien/pulumi-stackit",
                AdditionalSecretOutputs =
                {
                    "kubeConfig",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SkeKubeconfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SkeKubeconfig Get(string name, Input<string> id, SkeKubeconfigState? state = null, CustomResourceOptions? options = null)
        {
            return new SkeKubeconfig(name, id, state, options);
        }
    }

    public sealed class SkeKubeconfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the SKE cluster.
        /// </summary>
        [Input("clusterName", required: true)]
        public Input<string> ClusterName { get; set; } = null!;

        /// <summary>
        /// Expiration time of the kubeconfig, in seconds. Defaults to `3600`
        /// </summary>
        [Input("expiration")]
        public Input<int>? Expiration { get; set; }

        /// <summary>
        /// STACKIT project ID to which the cluster is associated.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        /// <summary>
        /// If set to true, the provider will check if the kubeconfig has expired and will generated a new valid one in-place
        /// </summary>
        [Input("refresh")]
        public Input<bool>? Refresh { get; set; }

        public SkeKubeconfigArgs()
        {
        }
        public static new SkeKubeconfigArgs Empty => new SkeKubeconfigArgs();
    }

    public sealed class SkeKubeconfigState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the SKE cluster.
        /// </summary>
        [Input("clusterName")]
        public Input<string>? ClusterName { get; set; }

        /// <summary>
        /// Date-time when the kubeconfig was created
        /// </summary>
        [Input("creationTime")]
        public Input<string>? CreationTime { get; set; }

        /// <summary>
        /// Expiration time of the kubeconfig, in seconds. Defaults to `3600`
        /// </summary>
        [Input("expiration")]
        public Input<int>? Expiration { get; set; }

        /// <summary>
        /// Timestamp when the kubeconfig expires
        /// </summary>
        [Input("expiresAt")]
        public Input<string>? ExpiresAt { get; set; }

        [Input("kubeConfig")]
        private Input<string>? _kubeConfig;

        /// <summary>
        /// Raw short-lived admin kubeconfig.
        /// </summary>
        public Input<string>? KubeConfig
        {
            get => _kubeConfig;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _kubeConfig = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("kubeConfigId")]
        public Input<string>? KubeConfigId { get; set; }

        /// <summary>
        /// STACKIT project ID to which the cluster is associated.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// If set to true, the provider will check if the kubeconfig has expired and will generated a new valid one in-place
        /// </summary>
        [Input("refresh")]
        public Input<bool>? Refresh { get; set; }

        public SkeKubeconfigState()
        {
        }
        public static new SkeKubeconfigState Empty => new SkeKubeconfigState();
    }
}

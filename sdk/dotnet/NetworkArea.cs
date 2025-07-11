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
    /// Network area resource schema. Must have a `region` specified in the provider configuration.
    /// 
    /// ## Example Usage
    /// </summary>
    [StackitResourceType("stackit:index/networkArea:NetworkArea")]
    public partial class NetworkArea : global::Pulumi.CustomResource
    {
        /// <summary>
        /// List of DNS Servers/Nameservers.
        /// </summary>
        [Output("defaultNameservers")]
        public Output<ImmutableArray<string>> DefaultNameservers { get; private set; } = null!;

        /// <summary>
        /// The default prefix length for networks in the network area.
        /// </summary>
        [Output("defaultPrefixLength")]
        public Output<int> DefaultPrefixLength { get; private set; } = null!;

        /// <summary>
        /// Labels are key-value string pairs which can be attached to a resource container
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// The maximal prefix length for networks in the network area.
        /// </summary>
        [Output("maxPrefixLength")]
        public Output<int> MaxPrefixLength { get; private set; } = null!;

        /// <summary>
        /// The minimal prefix length for networks in the network area.
        /// </summary>
        [Output("minPrefixLength")]
        public Output<int> MinPrefixLength { get; private set; } = null!;

        /// <summary>
        /// The name of the network area.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The network area ID.
        /// </summary>
        [Output("networkAreaId")]
        public Output<string> NetworkAreaId { get; private set; } = null!;

        /// <summary>
        /// List of Network ranges.
        /// </summary>
        [Output("networkRanges")]
        public Output<ImmutableArray<Outputs.NetworkAreaNetworkRange>> NetworkRanges { get; private set; } = null!;

        /// <summary>
        /// STACKIT organization ID to which the network area is associated.
        /// </summary>
        [Output("organizationId")]
        public Output<string> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// The amount of projects currently referencing this area.
        /// </summary>
        [Output("projectCount")]
        public Output<int> ProjectCount { get; private set; } = null!;

        /// <summary>
        /// Classless Inter-Domain Routing (CIDR).
        /// </summary>
        [Output("transferNetwork")]
        public Output<string> TransferNetwork { get; private set; } = null!;


        /// <summary>
        /// Create a NetworkArea resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NetworkArea(string name, NetworkAreaArgs args, CustomResourceOptions? options = null)
            : base("stackit:index/networkArea:NetworkArea", name, args ?? new NetworkAreaArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NetworkArea(string name, Input<string> id, NetworkAreaState? state = null, CustomResourceOptions? options = null)
            : base("stackit:index/networkArea:NetworkArea", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing NetworkArea resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NetworkArea Get(string name, Input<string> id, NetworkAreaState? state = null, CustomResourceOptions? options = null)
        {
            return new NetworkArea(name, id, state, options);
        }
    }

    public sealed class NetworkAreaArgs : global::Pulumi.ResourceArgs
    {
        [Input("defaultNameservers")]
        private InputList<string>? _defaultNameservers;

        /// <summary>
        /// List of DNS Servers/Nameservers.
        /// </summary>
        public InputList<string> DefaultNameservers
        {
            get => _defaultNameservers ?? (_defaultNameservers = new InputList<string>());
            set => _defaultNameservers = value;
        }

        /// <summary>
        /// The default prefix length for networks in the network area.
        /// </summary>
        [Input("defaultPrefixLength")]
        public Input<int>? DefaultPrefixLength { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Labels are key-value string pairs which can be attached to a resource container
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The maximal prefix length for networks in the network area.
        /// </summary>
        [Input("maxPrefixLength")]
        public Input<int>? MaxPrefixLength { get; set; }

        /// <summary>
        /// The minimal prefix length for networks in the network area.
        /// </summary>
        [Input("minPrefixLength")]
        public Input<int>? MinPrefixLength { get; set; }

        /// <summary>
        /// The name of the network area.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networkRanges", required: true)]
        private InputList<Inputs.NetworkAreaNetworkRangeArgs>? _networkRanges;

        /// <summary>
        /// List of Network ranges.
        /// </summary>
        public InputList<Inputs.NetworkAreaNetworkRangeArgs> NetworkRanges
        {
            get => _networkRanges ?? (_networkRanges = new InputList<Inputs.NetworkAreaNetworkRangeArgs>());
            set => _networkRanges = value;
        }

        /// <summary>
        /// STACKIT organization ID to which the network area is associated.
        /// </summary>
        [Input("organizationId", required: true)]
        public Input<string> OrganizationId { get; set; } = null!;

        /// <summary>
        /// Classless Inter-Domain Routing (CIDR).
        /// </summary>
        [Input("transferNetwork", required: true)]
        public Input<string> TransferNetwork { get; set; } = null!;

        public NetworkAreaArgs()
        {
        }
        public static new NetworkAreaArgs Empty => new NetworkAreaArgs();
    }

    public sealed class NetworkAreaState : global::Pulumi.ResourceArgs
    {
        [Input("defaultNameservers")]
        private InputList<string>? _defaultNameservers;

        /// <summary>
        /// List of DNS Servers/Nameservers.
        /// </summary>
        public InputList<string> DefaultNameservers
        {
            get => _defaultNameservers ?? (_defaultNameservers = new InputList<string>());
            set => _defaultNameservers = value;
        }

        /// <summary>
        /// The default prefix length for networks in the network area.
        /// </summary>
        [Input("defaultPrefixLength")]
        public Input<int>? DefaultPrefixLength { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Labels are key-value string pairs which can be attached to a resource container
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The maximal prefix length for networks in the network area.
        /// </summary>
        [Input("maxPrefixLength")]
        public Input<int>? MaxPrefixLength { get; set; }

        /// <summary>
        /// The minimal prefix length for networks in the network area.
        /// </summary>
        [Input("minPrefixLength")]
        public Input<int>? MinPrefixLength { get; set; }

        /// <summary>
        /// The name of the network area.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The network area ID.
        /// </summary>
        [Input("networkAreaId")]
        public Input<string>? NetworkAreaId { get; set; }

        [Input("networkRanges")]
        private InputList<Inputs.NetworkAreaNetworkRangeGetArgs>? _networkRanges;

        /// <summary>
        /// List of Network ranges.
        /// </summary>
        public InputList<Inputs.NetworkAreaNetworkRangeGetArgs> NetworkRanges
        {
            get => _networkRanges ?? (_networkRanges = new InputList<Inputs.NetworkAreaNetworkRangeGetArgs>());
            set => _networkRanges = value;
        }

        /// <summary>
        /// STACKIT organization ID to which the network area is associated.
        /// </summary>
        [Input("organizationId")]
        public Input<string>? OrganizationId { get; set; }

        /// <summary>
        /// The amount of projects currently referencing this area.
        /// </summary>
        [Input("projectCount")]
        public Input<int>? ProjectCount { get; set; }

        /// <summary>
        /// Classless Inter-Domain Routing (CIDR).
        /// </summary>
        [Input("transferNetwork")]
        public Input<string>? TransferNetwork { get; set; }

        public NetworkAreaState()
        {
        }
        public static new NetworkAreaState Empty => new NetworkAreaState();
    }
}

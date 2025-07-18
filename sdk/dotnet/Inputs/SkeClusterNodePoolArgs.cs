// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Stackit.Inputs
{

    public sealed class SkeClusterNodePoolArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Allow system components to run on this node pool.
        /// </summary>
        [Input("allowSystemComponents")]
        public Input<bool>? AllowSystemComponents { get; set; }

        [Input("availabilityZones", required: true)]
        private InputList<string>? _availabilityZones;

        /// <summary>
        /// Specify a list of availability zones. E.g. `eu01-m`
        /// </summary>
        public InputList<string> AvailabilityZones
        {
            get => _availabilityZones ?? (_availabilityZones = new InputList<string>());
            set => _availabilityZones = value;
        }

        /// <summary>
        /// Specifies the container runtime. Defaults to `containerd`
        /// </summary>
        [Input("cri")]
        public Input<string>? Cri { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Labels to add to each node.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The machine type.
        /// </summary>
        [Input("machineType", required: true)]
        public Input<string> MachineType { get; set; } = null!;

        /// <summary>
        /// Maximum number of additional VMs that are created during an update. If set (larger than 0), then it must be at least the amount of zones configured for the nodepool. The `max_surge` and `max_unavailable` fields cannot both be unset at the same time.
        /// </summary>
        [Input("maxSurge")]
        public Input<int>? MaxSurge { get; set; }

        /// <summary>
        /// Maximum number of VMs that that can be unavailable during an update. If set (larger than 0), then it must be at least the amount of zones configured for the nodepool. The `max_surge` and `max_unavailable` fields cannot both be unset at the same time.
        /// </summary>
        [Input("maxUnavailable")]
        public Input<int>? MaxUnavailable { get; set; }

        /// <summary>
        /// Maximum number of nodes in the pool.
        /// </summary>
        [Input("maximum", required: true)]
        public Input<int> Maximum { get; set; } = null!;

        /// <summary>
        /// Minimum number of nodes in the pool.
        /// </summary>
        [Input("minimum", required: true)]
        public Input<int> Minimum { get; set; } = null!;

        /// <summary>
        /// Specifies the name of the node pool.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The name of the OS image. Defaults to `flatcar`.
        /// </summary>
        [Input("osName")]
        public Input<string>? OsName { get; set; }

        /// <summary>
        /// This field is deprecated, use `os_version_min` to configure the version and `os_version_used` to get the currently used version instead.
        /// </summary>
        [Input("osVersion")]
        public Input<string>? OsVersion { get; set; }

        /// <summary>
        /// The minimum OS image version. This field will be used to set the minimum OS image version on creation/update of the cluster. If unset, the latest supported OS image version will be used. SKE automatically updates the cluster Kubernetes version if you have set `maintenance.enable_kubernetes_version_updates` to true or if there is a mandatory update, as described in [Updates for Kubernetes versions and Operating System versions in SKE](https://docs.stackit.cloud/stackit/en/version-updates-in-ske-10125631.html). To get the current OS image version being used for the node pool, use the read-only `os_version_used` field.
        /// </summary>
        [Input("osVersionMin")]
        public Input<string>? OsVersionMin { get; set; }

        /// <summary>
        /// Full OS image version used. For example, if 3815.2 was set in `os_version_min`, this value may result to 3815.2.2. SKE automatically updates the cluster Kubernetes version if you have set `maintenance.enable_kubernetes_version_updates` to true or if there is a mandatory update, as described in [Updates for Kubernetes versions and Operating System versions in SKE](https://docs.stackit.cloud/stackit/en/version-updates-in-ske-10125631.html).
        /// </summary>
        [Input("osVersionUsed")]
        public Input<string>? OsVersionUsed { get; set; }

        [Input("taints")]
        private InputList<Inputs.SkeClusterNodePoolTaintArgs>? _taints;

        /// <summary>
        /// Specifies a taint list as defined below.
        /// </summary>
        public InputList<Inputs.SkeClusterNodePoolTaintArgs> Taints
        {
            get => _taints ?? (_taints = new InputList<Inputs.SkeClusterNodePoolTaintArgs>());
            set => _taints = value;
        }

        /// <summary>
        /// The volume size in GB. Defaults to `20`
        /// </summary>
        [Input("volumeSize")]
        public Input<int>? VolumeSize { get; set; }

        /// <summary>
        /// Specifies the volume type. Defaults to `storage_premium_perf1`.
        /// </summary>
        [Input("volumeType")]
        public Input<string>? VolumeType { get; set; }

        public SkeClusterNodePoolArgs()
        {
        }
        public static new SkeClusterNodePoolArgs Empty => new SkeClusterNodePoolArgs();
    }
}

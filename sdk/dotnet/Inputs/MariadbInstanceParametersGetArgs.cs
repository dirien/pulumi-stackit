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

    public sealed class MariadbInstanceParametersGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enable monitoring.
        /// </summary>
        [Input("enableMonitoring")]
        public Input<bool>? EnableMonitoring { get; set; }

        /// <summary>
        /// Graphite server URL (host and port). If set, monitoring with Graphite will be enabled.
        /// </summary>
        [Input("graphite")]
        public Input<string>? Graphite { get; set; }

        /// <summary>
        /// The maximum disk threshold in MB. If the disk usage exceeds this threshold, the instance will be stopped.
        /// </summary>
        [Input("maxDiskThreshold")]
        public Input<int>? MaxDiskThreshold { get; set; }

        /// <summary>
        /// The frequency in seconds at which metrics are emitted.
        /// </summary>
        [Input("metricsFrequency")]
        public Input<int>? MetricsFrequency { get; set; }

        /// <summary>
        /// The prefix for the metrics. Could be useful when using Graphite monitoring to prefix the metrics with a certain value, like an API key
        /// </summary>
        [Input("metricsPrefix")]
        public Input<string>? MetricsPrefix { get; set; }

        /// <summary>
        /// The ID of the STACKIT monitoring instance. Monitoring instances with the plan "Observability-Monitoring-Starter" are not supported.
        /// </summary>
        [Input("monitoringInstanceId")]
        public Input<string>? MonitoringInstanceId { get; set; }

        /// <summary>
        /// Comma separated list of IP networks in CIDR notation which are allowed to access this instance.
        /// </summary>
        [Input("sgwAcl")]
        public Input<string>? SgwAcl { get; set; }

        [Input("syslogs")]
        private InputList<string>? _syslogs;

        /// <summary>
        /// List of syslog servers to send logs to.
        /// </summary>
        public InputList<string> Syslogs
        {
            get => _syslogs ?? (_syslogs = new InputList<string>());
            set => _syslogs = value;
        }

        public MariadbInstanceParametersGetArgs()
        {
        }
        public static new MariadbInstanceParametersGetArgs Empty => new MariadbInstanceParametersGetArgs();
    }
}

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

    public sealed class LoadbalancerTargetPoolSessionPersistenceGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// If true then all connections from one source IP address are redirected to the same target. This setting changes the load balancing algorithm to Maglev.
        /// </summary>
        [Input("useSourceIpAddress")]
        public Input<bool>? UseSourceIpAddress { get; set; }

        public LoadbalancerTargetPoolSessionPersistenceGetArgs()
        {
        }
        public static new LoadbalancerTargetPoolSessionPersistenceGetArgs Empty => new LoadbalancerTargetPoolSessionPersistenceGetArgs();
    }
}

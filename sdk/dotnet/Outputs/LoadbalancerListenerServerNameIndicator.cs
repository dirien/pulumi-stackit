// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Stackit.Outputs
{

    [OutputType]
    public sealed class LoadbalancerListenerServerNameIndicator
    {
        /// <summary>
        /// A domain name to match in order to pass TLS traffic to the target pool in the current listener
        /// </summary>
        public readonly string? Name;

        [OutputConstructor]
        private LoadbalancerListenerServerNameIndicator(string? name)
        {
            Name = name;
        }
    }
}

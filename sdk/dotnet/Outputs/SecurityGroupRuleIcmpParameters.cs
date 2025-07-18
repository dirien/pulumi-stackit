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
    public sealed class SecurityGroupRuleIcmpParameters
    {
        /// <summary>
        /// ICMP code. Can be set if the protocol is ICMP.
        /// </summary>
        public readonly int Code;
        /// <summary>
        /// ICMP type. Can be set if the protocol is ICMP.
        /// </summary>
        public readonly int Type;

        [OutputConstructor]
        private SecurityGroupRuleIcmpParameters(
            int code,

            int type)
        {
            Code = code;
            Type = type;
        }
    }
}

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

    public sealed class SkeClusterExtensionsAclGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("allowedCidrs", required: true)]
        private InputList<string>? _allowedCidrs;

        /// <summary>
        /// Specify a list of CIDRs to whitelist.
        /// </summary>
        public InputList<string> AllowedCidrs
        {
            get => _allowedCidrs ?? (_allowedCidrs = new InputList<string>());
            set => _allowedCidrs = value;
        }

        /// <summary>
        /// Is ACL enabled?
        /// </summary>
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        public SkeClusterExtensionsAclGetArgs()
        {
        }
        public static new SkeClusterExtensionsAclGetArgs Empty => new SkeClusterExtensionsAclGetArgs();
    }
}
